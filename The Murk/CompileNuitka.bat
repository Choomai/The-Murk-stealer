@echo off

nuitka --windows-disable-console --follow-imports --remove-output --product-name="Murk" --file-version="9.0.0.0" --product-version="9.0.0.0" --onefile --windows-icon-from-ico=icon.ico TheMurk.py

rmdir /s /q TheMurk.build
del /s /q TheMurk.cmd
rmdir /s /q __pycache__
rmdir /s /q build
del /s /q TheMurk.spec
:cmd
pause null