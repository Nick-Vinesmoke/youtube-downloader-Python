@echo off


pyinstaller --onefile --windowed --icon "ico.ico"  "main.py"

rmdir /s /q __pycache__
rmdir /s /q build

:cmd
pause null