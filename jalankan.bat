@echo off
cd /d "%~dp0"
where py >nul 2>nul && (py jalankan.py & goto :eof)
where python >nul 2>nul && (python jalankan.py & goto :eof)
echo Python belum terpasang. Unduh di https://www.python.org/downloads/ lalu jalankan file ini lagi.
pause
