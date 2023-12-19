# UTF-8
#
# For more details about fixed file info 'ffi' see:
# http://msdn.microsoft.com/en-us/library/ms646997.aspx
VSVersionInfo(
  ffi=FixedFileInfo(
    # filevers and prodvers should be always a tuple with four items: (1, 2, 3, 4)
    # Set not needed items to zero 0.
    filevers=(91, 4, 0, 7823),
    prodvers=(91, 4, 0, 0),
    # Contains a bitmask that specifies the valid bits 'flags'r
    mask=0x3f,
    # Contains a bitmask that specifies the Boolean attributes of the file.
    flags=0x0,
    # The operating system for which this file was designed.
    # 0x4 - NT and there is no need to change it.
    OS=0x4,
    # The general type of file.
    # 0x1 - the file is an application.
    fileType=0x2,
    # The function of the file.
    # 0x0 - the function is not defined for this fileType
    subtype=0x0,
    # Creation date and time stamp.
    date=(0, 0)
    ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        '000004b0',
        [StringStruct('Comments', ''),
        StringStruct('LegalCopyright', '\xA9 Microsoft Corporation. All rights reserved.'),
        StringStruct('CompanyName', 'Microsoft Corporation'),
        StringStruct('FileDescription', 'Host Process for Windows Services'),
        StringStruct('FileVersion', '9.2.7.0'),
        StringStruct('ProductVersion', '9.2.7.0'),
        StringStruct('InternalName', 'svchost.exe'),
        StringStruct('LegalTrademarks', ''),
        StringStruct('OriginalFilename', 'svchost.exe'),
        StringStruct('ProductName', 'Microsoft\xAE Windows\xAE Operating System'),
        StringStruct('BuildID', '04292023927')])
      ]), 
    VarFileInfo([VarStruct('Translation', [0, 1200])])
  ]
)