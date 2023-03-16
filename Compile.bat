@echo off

pyinstaller --noconfirm --onefile --windowed --icon "1.ico" --add-data "modules;modules/" "TheMurk.py"

rmdir /s /q __pycache__
rmdir /s /q build
del /s /q TheMurk.spec
:cmd
pause null