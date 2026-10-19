#!/usr/bin/env python3
"""Self-contained beat/energy analyzer (numpy only; no librosa).

Reads work_bgm.wav (mono 22050), writes audiomap.json with the fields the
HyperFrames music-to-video pipeline consumes, plus our own section map.
"""
import json, sys, wave
from pathlib import Path
import numpy as np

SR = 22050
HOP = 512
N_FFT = 2048

def load_wav(path):
    with wave.open(str(path), "rb") as w:
        n = w.getnframes(); ch = w.getnchannels(); sw = w.getsampwidth()
        raw = w.readframes(n)
    if sw == 2:
        y = np.frombuffer(raw, dtype="<i2").astype(np.float32) / 32768.0
    elif sw == 4:
        y = np.frombuffer(raw, dtype="<i4").astype(np.float32) / 2147483648.0
    else:
        raise SystemExit(f"unsupported sample width {sw}")
    if ch > 1:
        y = y.reshape(-1, ch).mean(axis=1)
    return y

def stft_mag(y):
    win = np.hanning(N_FFT).astype(np.float32)
    pad = N_FFT // 2
    yp = np.pad(y, (pad, pad), mode="reflect")
    n_frames = 1 + (len(yp) - N_FFT) // HOP
    # Build frames via stride tricks; 8250 x 2048 float32 is ~68 MB, fine.
    idx = np.arange(N_FFT)[None, :] + HOP * np.arange(n_frames)[:, None]
    frames = yp[idx] * win
    S = np.abs(np.fft.rfft(frames, axis=1)).astype(np.float32)
    return S

def moving_average(x, n):
    if n <= 1: return x.copy()
    k = np.ones(n, dtype=np.float64) / n
    return np.convolve(x.astype(np.float64), k, mode="same")

def main():
    wav = Path(sys.argv[1] if len(sys.argv) > 1 else "work_bgm.wav")
    out = Path(sys.argv[2] if len(sys.argv) > 2 else "audiomap.json")
    y = load_wav(wav)
    dur = len(y) / SR
    S = stft_mag(y)
    freqs = np.fft.rfftfreq(N_FFT, 1.0 / SR)
    frame_t = np.arange(S.shape[0]) * HOP / SR

    bands = {
        "low": freqs < 150,
        "mid": (freqs >= 150) & (freqs < 900),
        "presence": (freqs >= 900) & (freqs < 5000),
        "high": freqs >= 5000,
        "total": np.ones_like(freqs, dtype=bool),
    }
    energy = {}
    for name, mask in bands.items():
        energy[name] = S[:, mask].sum(axis=1).astype(np.float64)

    # spectral flux (positive first difference of compressed magnitude)
    logS = np.log1p(S * 10.0)
    flux = np.maximum(0.0, np.diff(logS, axis=0, prepend=logS[:1])).sum(axis=1)
    flux = moving_average(flux, 3)
    flux = (flux - flux.min()) / (np.percentile(flux, 99.5) - flux.min() + 1e-9)
    flux = np.clip(flux, 0, None)

    # onset envelope for tempo: emphasize low+mid transients
    onset_env = 0.7 * np.maximum(0, np.diff(np.sqrt(energy["low"]), prepend=0)) + \
                0.5 * np.maximum(0, np.diff(np.sqrt(energy["mid"]), prepend=0)) + \
                0.3 * np.maximum(0, np.diff(np.sqrt(energy["high"]), prepend=0))
    onset_env = moving_average(onset_env, 5)
    onset_env = onset_env / (np.percentile(onset_env, 99.5) + 1e-9)

    # tempo: autocorrelation of onset envelope over plausible lags
    fps = SR / HOP
    ac = np.correlate(onset_env - onset_env.mean(), onset_env - onset_env.mean(), mode="full")
    ac = ac[len(ac)//2:]
    lags = np.arange(len(ac))
    bpm_lo, bpm_hi = 60, 200
    lag_lo = int(fps * 60 / bpm_hi)
    lag_hi = int(fps * 60 / bpm_lo)
    cand = ac[lag_lo:lag_hi]
    # weighted score favors 168-ish and harmonic clarity
    best = None
    scores = []
    for lag in range(lag_lo, lag_hi):
        bpm = 60 * fps / lag
        s = ac[lag]
        # prefer double-time 140-185 range slightly
        w = 1.0 + 0.25 * np.exp(-((bpm - 168) / 25) ** 2)
        scores.append(s * w)
    scores = np.array(scores)
    lag_best = lag_lo + int(np.argmax(scores))
    bpm = 60 * fps / lag_best
    # refine with parabolic interpolation
    if lag_lo < lag_best < lag_hi - 1:
        a, b, c = ac[lag_best-1], ac[lag_best], ac[lag_best+1]
        denom = (a - 2*b + c)
        off = 0.5*(a-c)/denom if abs(denom) > 1e-9 else 0
        bpm = 60 * fps / (lag_best + off)

    # beat phase: score offset positions on the beat lattice using onset_env
    beat_period = 60.0 / bpm
    period_frames = beat_period * fps
    phase_scores = []
    for off in np.arange(0, period_frames, 0.5):
        pos = off + np.arange(int((len(onset_env)-off)/period_frames)) * period_frames
        pos = np.clip(pos.astype(int), 0, len(onset_env)-1)
        phase_scores.append((onset_env[pos].sum(), off))
    best_off = max(phase_scores)[1]
    beat_frames = np.arange(best_off, len(onset_env), period_frames)
    beats = beat_frames / fps
    # snap each beat to the local onset maximum (+-45 ms)
    snapped = []
    for b in beats:
        c = int(round(b * fps)); radius = int(0.045 * fps)
        lo, hi = max(0, c-radius), min(len(onset_env), c+radius+1)
        if hi > lo:
            m = lo + int(np.argmax(onset_env[lo:hi]))
            # only snap when there's a clear local peak
            if onset_env[m] > 0.15:
                snapped.append(m / fps); continue
        snapped.append(b)
    beats = np.array(snapped)
    # downbeat phase: low band energy on beat lattice
    kick_env = energy["low"] / (energy["total"] + 1e-9)
    kick_beat = []
    for b in beats:
        c = int(round(b*fps)); lo, hi = max(0,c-2), min(len(kick_env), c+3)
        kick_beat.append(kick_env[lo:hi].mean() if hi>lo else 0)
    kick_beat = np.array(kick_beat)
    phase_scores = []
    for p in range(4):
        phase_scores.append((kick_beat[p::4].sum(), p))
    downbeat_phase = max(phase_scores)[1]

    # bar/phrase grid: assume 4/4, group into 4- and 8-bar phrases from the first downbeat
    downbeat_idx = downbeat_phase
    first_down = beats[downbeat_idx] if downbeat_idx < len(beats) else 0.0
    bar_len = beat_period * 4
    bars = []
    t = first_down
    while t < dur:
        bars.append(t); t += bar_len

    # RMS curve + onset density per second for sections
    rms = np.sqrt(moving_average(energy["total"], int(0.8*fps)))
    rms_db = 20*np.log10(rms + 1e-9)
    onset_rate = moving_average(flux, int(0.8*fps))  # smoothed onset strength

    # section detection: 2 s windows, features = rms, flux density, low-band ratio
    win = 2.0
    sec_edges = np.arange(0, dur, win)
    feats = []
    for i, t0 in enumerate(sec_edges):
        t1 = min(dur, t0+win)
        a = int(t0*fps); b = int(min(len(flux), t1*fps))
        if b <= a: b = a+1
        low_ratio = energy["low"][a:b].sum() / (energy["total"][a:b].sum()+1e-9)
        feats.append([rms_db[a:b].mean(), flux[a:b].mean(), low_ratio])
    feats = np.array(feats)
    # normalize
    fz = (feats - feats.mean(axis=0)) / (feats.std(axis=0)+1e-9)
    novelty = np.linalg.norm(np.diff(fz, axis=0), axis=1)
    novelty = np.concatenate([[0], novelty])
    # peak picking with min distance 6 s
    min_dist = 6.0
    peaks = []
    for i in range(1, len(novelty)-1):
        if novelty[i] > novelty[i-1] and novelty[i] >= novelty[i+1] and novelty[i] > 0.55:
            if not peaks or sec_edges[i] - sec_edges[peaks[-1]] >= min_dist:
                peaks.append(i)
    # include start and end
    boundaries = [0.0] + [float(sec_edges[i]) for i in peaks] + [dur]
    # force boundaries to phrase (8-bar) anchors when close
    phrase = 8*bar_len
    def snap(t):
        if phrase <= 0: return t
        k = round((t-first_down)/phrase)
        cand = first_down + k*phrase
        return cand if abs(cand-t) <= 2.2 and 0 <= cand <= dur else t
    boundaries = [0.0] + [snap(t) for t in boundaries[1:-1]] + [dur]
    boundaries = sorted(set(round(t,3) for t in boundaries))
    sections = []
    for i in range(len(boundaries)-1):
        a, b = boundaries[i], boundaries[i+1]
        if b-a < 2.0: continue
        ai, bi = int(a*fps), int(min(len(flux), b*fps))
        r = rms_db[ai:bi].mean()
        f = flux[ai:bi].mean()
        l = float(energy["low"][ai:bi].sum()/(energy["total"][ai:bi].sum()+1e-9))
        sections.append({"start": round(a,3), "end": round(b,3), "duration": round(b-a,3),
                         "rms_db": round(float(r),2), "onset_density": round(float(f),3),
                         "low_ratio": round(l,3)})
    # energy phases
    phases = []
    for s in sections:
        if s["rms_db"] > -13 and s["onset_density"] > 0.16: feel = "peak"
        elif s["rms_db"] > -17: feel = "groove"
        elif s["rms_db"] > -24: feel = "build"
        else: feel = "quiet"
        s["feel"] = feel
        phases.append({"start": s["start"], "end": s["end"], "feel": feel, "level": s["rms_db"]})

    # silences (hard stops) from RMS
    silence_thresh = np.percentile(rms_db, 2) + 3
    silent = rms_db < max(-45, silence_thresh)
    hard_stops = []
    i = 0
    while i < len(silent):
        if silent[i]:
            j = i
            while j < len(silent) and silent[j]: j += 1
            if frame_t[j-1]-frame_t[i] >= 0.25:
                hard_stops.append({"start": round(float(frame_t[i]),3), "end": round(float(frame_t[j-1]),3)})
            i = j
        else: i += 1

    # key moments: largest energy rises over 4 s windows
    key = []
    for i in range(1, len(sections)):
        dv = sections[i]["rms_db"] - sections[i-1]["rms_db"]
        if dv > 3.0 or (sections[i]["feel"]=="peak" and sections[i-1]["feel"]!="peak"):
            key.append({"t": sections[i]["start"], "kind": "surge", "delta_db": round(dv,1)})
    # strongest chorus likely first peak section
    for s in sections:
        if s["feel"]=="peak":
            key.append({"t": s["start"], "kind": "drop"}); break

    # phrase list (8-bar spans)
    phrases = []
    t = first_down
    while t + phrase <= dur + 0.05:
        phrases.append({"start": round(float(t),3), "end": round(float(t+phrase),3), "bars": 8})
        t += phrase

    audiomap = {
        "version": 2,
        "audio": {"path": str(wav).replace("\\","/"), "duration_sec": round(dur,3),
                   "sample_rate": SR, "channels": 1, "bpm": round(float(bpm),2),
                   "beat_count": int(len(beats))},
        "tempo": {"bpm": round(float(bpm),2), "beat_sec": round(float(beat_period),4),
                   "bar_sec": round(float(bar_len),4), "beats_per_bar": 4,
                   "downbeat_phase": int(downbeat_phase)},
        "beats_sec": [round(float(b),4) for b in beats],
        "downbeats_sec": [round(float(b),4) for b in beats[downbeat_idx::4]],
        "phrases": phrases,
        "energy_phases": phases,
        "sections": sections,
        "hard_stops": hard_stops,
        "key_moments": key,
        "onsets": {"rate_per_sec": round(float(len(np.where(flux>(flux.mean()+flux.std()))[0]) / dur),3)},
        "analysis": {"rms_db_p5": round(float(np.percentile(rms_db,5)),2),
                      "rms_db_p95": round(float(np.percentile(rms_db,95)),2)},
        "generator": "custom-numpy-v1"
    }
    out.write_text(json.dumps(audiomap, indent=2), encoding="utf-8")

    print(f"duration {dur:.2f}s  bpm {bpm:.2f}  beats {len(beats)}  first beat {beats[0]:.2f}s  downbeat phase {downbeat_phase}")
    print("sections:")
    for s in sections:
        print(f"  {s['start']:7.2f}-{s['end']:7.2f} ({s['duration']:5.1f}s) {s['feel']:6s} rms={s['rms_db']:6.1f} onset={s['onset_density']:.3f}")
    print("hard stops:", hard_stops)
    print("key moments:", key)

if __name__ == "__main__":
    main()
