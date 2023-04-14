nuitka --windows-disable-console --onefile --follow-imports --enable-plugin=tk-inter --remove-output --windows-icon-from-ico=icon.ico TheMurkBuilder.py

rmdir /s /q build

:cmd
pause null