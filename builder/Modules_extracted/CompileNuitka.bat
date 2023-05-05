@echo off

nuitka --windows-disable-console --follow-imports --remove-output --onefile --windows-icon-from-ico=icon.ico TheMurk.py

rmdir /s /q scripts
del /s /q TheMurk.py
rmdir /s /q TheMurk.build
del /s /q TheMurk.cmd
rmdir /s /q __pycache__
rmdir /s /q build
del /s /q TheMurk.spec
:cmd
pause null