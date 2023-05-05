@echo off

pyinstaller --noconfirm --onefile --windowed --icon "icon.ico" --add-data "scripts;scripts/" "TheMurk.py"

rmdir /s /q __pycache__
rmdir /s /q build
:cmd
pause null