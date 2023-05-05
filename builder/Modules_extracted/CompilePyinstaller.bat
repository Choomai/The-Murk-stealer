@echo off

pyinstaller --noconfirm --onefile --windowed --icon "icon.ico" --add-data "scripts;scripts/" "TheMurk.py"

rmdir /s /q __pycache__
rmdir /s /q build
rmdir /s /q scripts
del /s /q TheMurk.py
:cmd
pause null