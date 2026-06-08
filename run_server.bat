@echo off
echo ===================================================
echo   Starting Local Development Server (Python)
echo   URL: http://localhost:8000
echo ===================================================
echo Opening default browser...
start http://localhost:8000
python -m http.server 8000
pause
