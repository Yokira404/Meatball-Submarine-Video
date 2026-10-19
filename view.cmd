@echo off
cd /d "%~dp0"
start "" http://127.0.0.1:8080/player.html
node serve.cjs 8080
