pyinstaller --noconsole --noconfirm --onefile --windowed --icon "preferences/icon.ico" --name "TheMurk" --upx-dir "../upx-4.2.1-win64" --version-file "preferences/version.py" --add-data "manager;manager/" --add-data "preferences;preferences/" --add-data "targets;targets/" --add-data "progress.py;."  "The_Murk.py"

rmdir /s /q __pycache__
rmdir /s /q build
del TheMurk.spec
pause