pyinstaller --noconfirm --onefile --icon "icon.ico" --name "TheMurkBuilder" --upx-dir "../upx-4.2.1-win64" --version-file "version.py" "TheMurkBuilder.py"

rmdir /s /q __pycache__
rmdir /s /q build
del TheMurkBuilder.spec
pause