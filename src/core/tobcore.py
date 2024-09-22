#!/usr/bin/env python3

import os
import datetime
import requests
import zipfile
import io
from pystyle import *

def check_os():
    if os.name == "nt": #windows
        operating_system = "0"
    if os.name == "posix": #unix
        operating_system = "1"
    return(operating_system)

#################################### check up date versions
repo_owner = "jmktt"
repo_name = "tob-cript"

def get_latest_release():
    try:
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
        response = requests.get(url)
        response.raise_for_status()
        latest_release = response.json()["tag_name"]
        return latest_release
    except Exception as e:
        print(Col.red+"[!]Error getting latest release:"+bcolors.RESET, e)
        return None

def get_local_version():
    try:
        with open("VERSION", "r") as version_file:
            local_version = version_file.read().strip()
            return local_version
    except Exception as e:
        print(Col.red+"[!]Error getting local version:"+bcolors.RESET, e)
        return None

def update_tob(version):
    try:
        print("[-]Downloading the latest version...")
        url = f"https://github.com/{repo_owner}/{repo_name}/archive/{version}.zip"
        response = requests.get(url)
        response.raise_for_status()
        
        print("[-]Unzipping the ZIP file...")
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
            zip_file.extractall(".")
        
        with open("VERSION", "w") as version_file:
            version_file.write(version)
        
        print(Col.green+"[!]TOB updated successfully!"+bcolors.RESET)
    except Exception as e:
        print(Col.red+"[!]Error updating TOB:"+bcolors.RESET, e)

def check_update():
    try:
        latest_release = get_latest_release()
        local_version = get_local_version()
        
        if local_version == latest_release:
            print(Col.green+"[-]TOB is up to date."+bcolors.RESET)
        else:
            print(Col.red+"[!]There is a newer version available:"+bcolors.RESET, latest_release)
            update_tob(latest_release)
    except Exception as e:
        print(Col.red+"[!]Error checking for update:"+bcolors.RESET, e)

def check_status():
    url = "https://api.github.com"
    try:
        response = requests.head(url, timeout=3)
        response.raise_for_status()
        print(net_online)
        check_update()
    except requests.RequestException:
        print(net_offline)
##############################################################

operating_system = check_os()
def disp_clean():
    if (operating_system == "1"):
        os.system("clear")
    elif (operating_system == "0"):
        os.system("cls")
    else:
        print("[!]UNIDENTIFIED OS")
###############################################################
class bcolors:
    YELLOW = '\033[1;33m'
    BLUE = '\033[1;36m'
    RESET = '\033[0;0m'

############################################################### write
now = datetime.datetime.now()
def write(encrypted_text):
    file = open("criptout.txt", "a",encoding="utf-8")
    file.write("\n Cript Text({0}): {1}".format(now,encrypted_text))
    file.close()


############### banners
menu_banner = '''
    ooooooooooooo   .oooooo.   oooooooooo.
   8'   888   `8  d8P'  `Y8b  `888'   `Y8b
        888      888      888  888     888
        888      888      888  888oooo888'
        888      888      888  888    `88b
        888      888      888  888    `88b
        888      `88b    d88'  888    .88P
       o888o      `Y8bood8P'  o888bood8P '''

menu_banner_1 = '''
       ________   ______   _______  
      |        \ /      \ |       \ 
       \$$$$$$$$|  $$$$$$\| $$$$$$$
         | $$   | $$  | $$| $$__/ $$
         | $$   | $$  | $$| $$    $$
         | $$   | $$  | $$| $$$$$$$
         | $$   | $$__/ $$| $$__/ $$
         | $$    \$$    $$| $$    $$
          \$$     \$$$$$$  \$$$$$$$'''

menu_banner_2 = '''

         ████████╗ ██████╗ ██████╗ 
        ╚══██╔══╝██╔═══██╗██╔══██╗
           ██║   ██║   ██║██████╔╝
           ██║   ██║   ██║██╔══██╗
           ██║   ╚██████╔╝██████╔╝
           ╚═╝    ╚═════╝ ╚═════╝'''

menu_banner_3 = '''
            .-""-.
           / .--. \'
          / /    \ \'
          | |    | |
          | |.-""-.|
         ///`.::::.`\'
        ||| ::/  \:: ;  010101000100111101000010
        ||; ::\__/:: ;
         \\\ '::::' /
     tob  `=':-..-'`'''

menu_banner_4 = '''
                  __gggrgM**M#mggg__
            __wgNN@"B*P""mp""@d#"@N#Nw__
          _g#@0F_a*F#  _*F9m_ ,F9*__9NG#g_
       _mN#F  aM"    #p"    !q@    9NL "9#Qu_
      g#MF _pP"L  _g@"9L_  _g""#__  g"9w_ 0N#p
    _0F jL*"   7_wF     #_gF     9gjF   "bJ  9h_
   j#  gAF    _@NL     _g@#_      J@u_    2#_  #_
  ,FF_#" 9_ _#"  "b_  g@   "hg  _#"  !q_ jF "*_09_
  F N"    #p"      Ng@       `#g"      "w@    "# t
 j p#    g"9_     g@"9_      gP"#_     gF"q    Pb L
 0J  k _@   9g_ j#"┏┳┓"b_  j#"┳┓ "b_ _d"   q_ g  ##
 #F  `NF     "#g"   ┃  "Md"   ┣┫   5N#      9W"  j#
 #k  jFb_    g@"q_  ┻ _*"9m_  ┻┛  _*"R_    _#Np  J#
 tApjF  9g  J"   9M_ _m" ┏┓ 9%_ _*"   "#  gF  9_jNF
  k`N    "q#       9g@   ┃┃   #gF       ##"    #"j
  `_0q_   #"q_    _&"9p_ ┗┛ _g"`L_    _*"#   jAF,'
   9# "b_j   "b_ g"    *g _gF    9_ g#"  "L_*"qNF
    "b_ "#_    "NL      _B#      _I@     j#" _#"
      NM_0"*g_ j""9u_  gP  q_  _w@ ]_ _g*"F_g@
       "NNh_ !w#_   9#g"    "m*"   _#*" _dN@"
          9##g_0@q__ #"4_  j*"k __*NF_g#@P"
            "9NN#gIPNL_ "b@" _2M"Lg#N@F"
                ""P@*NN#gEZgNN@#@P"" 
'''

banners = [menu_banner, menu_banner_1, menu_banner_2, menu_banner_3, menu_banner_4]

cript_banner='''
      .--------.
     / .------. 1
    / /        \ 1
    | |        | |
   _| |________| |_            
 .' |_|        |_| '.
 '._____ ____ _____.'
 |     .'____'.     |
 '.__.'.'    '.'.__.'
 '.__  | CTOB |  __.'
 |   '.'.____.'.'   |
 '.____'.____.'____.'
 '.________________.'
'''

decript_banner='''
      .--------.
     / .------. 1
    / /        \ 1
    | |        | |
    | |        | |
    | |        --- 
   _| |____________
 .' |_|            '.
 '._____ ____ _____.'
 |     .'____'.     |
 '.__.'.'    '.'.__.'
 '.__  | DTOB |  __.'
 |   '.'.____.'.'   |
 '.____'.____.'____.'
 '.________________.'
'''
key_banner='''
          8 8 8 8                     ,ooo.     
          8a8 8a8                    oP   ?b    
         d888a888zzzzzzzzzzzzzzzzzzzz8     8b   
          `ii^ii'                    ?o___oP'  
'''

john='''

 ▐▄▄▄       ▄ .▄ ▐ ▄      ▄▄· ▄▄▄  ▄▄▄ .▄▄▌ ▐ ▄▌
  ·██▪     ██▪▐█•█▌▐█    ▐█ ▌▪▀▄ █·▀▄.▀·██· █▌▐█
▪▄ ██ ▄█▀▄ ██▀▐█▐█▐▐▌    ██ ▄▄▐▀▀▄ ▐▀▀▪▄██▪▐█▐▐▌
▐▌▐█▌▐█▌.▐▌██▌▐▀██▐█▌    ▐███▌▐█•█▌▐█▄▄▌▐█▌██▐█▌
 ▀▀▀• ▀█▄▀▪▀▀▀ ·▀▀ █▪    ·▀▀▀ .▀  ▀ ▀▀▀  ▀▀▀▀ ▀▪
  
'''
bit_logo='''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⣶⣶⣶⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣤⣾⣿⡿⠿⠛⠛⠛⠛⠛⠛⠻⢿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣼⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣷⣄⠀⠀⠀⠀
⠀⠀⠀⣰⣿⡿⠋⠀⠀⠀⠀⠀⣿⡇⠀⢸⣿⡇⠀⠀⠀⠀⠀⠈⢿⣿⣦⡀⠀⠀
⠀⠀⣸⣿⡿⠀⠀⠀⠸⠿⣿⣿⣿⡿⠿⠿⣿⣿⣿⣶⣄⠀⠀⠀⠀⢹⣿⣷⠀⠀
⠀⢠⣿⡿⠁⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠈⣿⣿⣿⠀⠀⠀⠀⠀⢹⣿⣧⠀
⠀⣾⣿⡇⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⢀⣠⣿⣿⠟⠀⠀⠀⠀⠀⠈⣿⣿⠀
⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⢸⣿⣿⡿⠿⠿⠿⣿⣿⣥⣄⠀⠀⠀⠀⠀⠀⣿⣿⠀
⠀⢿⣿⡇⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⢻⣿⣿⣧⠀⠀⠀⠀⢀⣿⣿⠀
⠀⠘⣿⣷⡀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⣼⣿⣿⡿⠀⠀⠀⠀⣸⣿⡟⠀
⠀⠀⢹⣿⣷⡀⠀⠀⢰⣶⣿⣿⣿⣷⣶⣶⣾⣿⣿⠿⠛⠁⠀⠀⠀⣸⣿⡿⠀⠀
⠀⠀⠀⠹⣿⣷⣄⠀⠀⠀⠀⠀⣿⡇⠀⢸⣿⡇⠀⠀⠀⠀⠀⢀⣾⣿⠟⠁⠀⠀
⠀⠀⠀⠀⠘⢻⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⡿⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣷⣶⣤⣤⣤⣤⣤⣤⣴⣾⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠿⠿⠿⠿⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''

funny='''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡿⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡶⠶⢖⠦⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣷⡀⠀⠀⠀⠀⠀⠐⠋⠉⠉⠛⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⠁⠀⠀⢀⠇⠈⢳⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠋⠀⠀⠀⢀⣀⣠⠤⠤⠤⠤⠤⠤⠤⢌⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⢻⠀⠀⠀⠀⠈⠀⠀⢸⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⣠⠤⠒⣋⡭⠤⠒⠒⠉⠉⡩⢟⣣⣤⣀⡢⣬⣉⠒⠤⣄⠀⠀⠀⠀⠀⠀⠀⠀⢼⠈⠃⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⣉⠴⠒⠉⠀⠀⠀⠀⠀⢀⣞⣴⠟⠋⠉⠛⢿⣾⣎⠑⢤⡀⠙⠢⣄⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⣸⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⢋⡤⢊⣁⡀⠀⠀⠀⠀⠀⠀⠀⣞⣾⠃⠀⠀⠀⠀⠀⠹⣿⡄⠀⠱⡄⠀⠈⠑⣄⠀⠀⢀⣠⣽⠶⠶⠶⠒⠒⠒⠛⢤⣄⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠋⡴⢋⢔⣭⣴⣿⣷⣤⠀⠀⠀⠀⠰⣽⠃⠀⠀⠀⠀⠀⠀⠀⢹⣇⠀⠀⠘⡄⠀⠀⠈⢳⣶⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠯⠻⣦⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡜⢡⠎⢠⢯⣿⠋⠁⠀⠈⠻⣷⠀⠀⠀⠀⡏⠀⠀⠀⠐⢷⢶⣄⠀⠀⣿⠀⠀⠐⠁⠀⠀⢰⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠪⠙⣆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⢠⠃⠀⣮⡿⠁⠀⠀⠀⠀⠀⠻⣇⠀⠀⢸⡇⠀⠀⢀⠀⣸⣷⣻⡄⠀⣿⠀⠀⠀⠀⠀⠀⣏⠓⠒⢀⣀⣀⣀⣀⣀⣀⣀⣀⠀⢠⠖⠀⠀⠀⠘⡄
⠀⠀⣀⣠⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⢀⠇⠀⢰⣿⠇⠀⠀⠀⠀⠶⣶⡄⢹⠀⠀⠀⡇⠀⠀⣾⢹⣿⣿⣏⡇⠀⣿⠀⠀⣀⣤⡤⠤⣼⣶⠿⠛⠉⠀⠀⠀⠀⠀⠀⠉⠙⡇⠀⠀⠀⠀⠀⠀
⣠⢾⠋⠀⠀⠈⠻⡷⣄⠀⠀⠀⠀⠀⠀⢰⠁⠸⠀⠀⠸⣿⠀⠀⠀⠀⣄⣀⣷⣽⣸⠀⠀⠀⣇⠀⠀⠸⣞⣿⣅⣽⠁⢀⣇⣴⠞⠋⠁⠀⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⠀⠀⠀⠀⠀⠀
⡇⠘⠂⠀⠀⠀⠀⠁⠘⡆⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⢰⣿⠀⠀⠀⠀⣇⣿⣿⣿⣿⠀⠀⠀⠸⡄⠀⠀⠙⠧⠽⠃⠀⡼⠋⠀⠀⠀⠀⠀⣯⠦⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀
⢳⡀⠀⠀⠀⠀⠀⠀⢀⣹⣤⣤⣤⣤⣄⡇⠀⠰⠀⠀⠀⣿⠀⠀⠀⠀⢻⡽⠿⣾⢹⠀⠀⠀⠀⠻⡄⠀⠀⠀⠀⢠⠞⠁⠀⣀⣀⡀⠀⠀⠘⢧⡀⣠⣤⡶⠖⠛⠛⠛⠒⠒⡞⠀⠀⠀⠀⠀⠀⢀⠀
⠀⠉⠳⣄⠀⢀⡤⡺⠛⠉⠀⠀⠀⠀⠈⣻⢦⠀⠀⠀⠀⢻⡆⠀⠀⠀⠈⠻⠟⢁⡎⠀⠀⠀⠀⠀⠙⠦⣄⣀⣤⠟⠀⠀⠉⣀⣀⣀⡉⠂⠀⠀⣽⣏⠁⠀⠀⠀⠀⠀⠀⠀⢇⠀⠀⠀⠀⠀⢠⡞⠀
⠀⠀⠀⢈⣷⠋⠀⠁⠀⠀⠀⠀⠀⢈⣩⣤⣼⣧⣤⡀⠀⠀⠻⡄⠀⠀⠀⠀⢀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⣈⣭⠵⠒⠋⠉⠂⠀⠀⠹⡌⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀
⠀⠀⠀⣾⠋⠀⠀⠀⠀⠀⢀⡤⠞⠉⠉⠀⠀⠀⠈⣻⡆⠀⣀⣙⡦⠤⣀⣤⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠋⣡⡏⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⣄⡀⠀⠀⠀⠀⠀⠀⣀⣠⠴⠋⠁⠀⠀⠀
⠀⠀⢸⠇⠀⠀⠀⠀⢀⡶⠉⠀⠀⠀⠀⠀⠀⠀⠈⠁⡧⠋⠉⠁⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠚⠉⠀⢀⣴⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠁⠈⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⠀⠀⠀⠉⠑⢏⠀⠀⠀⠀⠀⠀⣀⣤⠶⠶⠾⣧⡀⠀⠀⠀⠀⠀⣤⣤⣤⣤⡤⠒⠒⠉⠁⠀⠀⣀⣤⣶⠿⢿⡿⠀⠀⠀⠀⠀⠀⠀⠀⢀⡶⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⡆⠀⠀⠀⠀⠈⠇⠀⠀⢀⡤⠚⠉⠀⠀⠀⠐⠁⡇⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣶⣶⣶⣶⣾⠿⣿⡟⠁⠀⣼⠃⠀⠀⠀⠀⠀⣠⠞⣠⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠹⡄⠀⠀⠀⠀⠀⠀⠉⠻⡄⠀⠀⠀⠀⠀⠀⣰⠁⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⠃⣠⠏⠀⠀⣰⠏⠀⠀⠀⠀⠠⠞⢁⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⣄⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⢀⡴⠋⠳⢄⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⠁⠊⠀⠀⢀⡰⠋⠀⠀⠀⠀⠀⣠⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠑⠦⣀⡀⠀⠀⠀⠀⠀⣀⡠⠖⠋⠀⠀⠀⠀⠙⠢⢄⡀⠀⠀⠀⠀⠈⠛⢿⣇⣀⣀⣠⠴⠋⠀⠀⠀⢀⣀⠤⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠒⠒⠚⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠒⠤⢤⣀⣀⣀⣀⣀⣀⣀⣀⡠⠤⠖⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''

     
def display_key_box(key):
    key_box =Box.DoubleCube("     YOUR KEY IS : {}     ".format(key))
    print("\n{}".format(key_box))


tname = Colorate.Horizontal(Colors.yellow_to_red, "TOB",1)
cname = Colorate.Horizontal(Colors.red_to_blue, "JMKTT",2)
version= Colorate.Horizontal(Colors.red_to_blue, "1.5",2)
###############################################################

### invalid mensages
invoption_text = (Col.red+"\nThere is no such option...\033[0;0m\n")
invkey_text = (Col.red+"\n This key is not valid...\033[0;0m")
invfile_text = (Col.red+"\n File not found...\033[0;0m")
### status mensages
net_online = (bcolors.YELLOW+"[+]Internet Status: Online"+bcolors.RESET)
net_offline = (bcolors.YELLOW+"[-]Internet Status: Offline"+bcolors.RESET)
### bye message
bye_message = (bcolors.BLUE+"Thank you for using Text-Object Basic Cript...\ngoodbye;)"+bcolors.RESET)
###############
def credit_text():
    print("Криптография с древних времен до наших дней необходима")
    print("для защиты наших коммуникаций и обеспечения того,")
    print("чтобы только нужные получатели могли понять их контент,")
    print("играя жизненно важную роль в информационной безопасности и ")
    print("сохранении конфиденциальности.")
    print("Языки со своими нюансами и разнообразием отражают красоту человеческой коммуникации.")
    print("В то же время, конфиденциальность и анонимность являются основой индивидуальной свободы.")
    print("Таким образом, криптография становится важным мостом между этими элементами,")
    print("обеспечивая безопасность и конфиденциальность наших коммуникаций в океане данных.")
    print("В мире, где нас постоянно наблюдают глаза и уши,")
    print("криптография превращается в наш новый неизвестный язык и туман информации,")
    print("непонятный для тех, кто не имеет ключа к его расшифровке.")
    print("[!]signati: jm..")

######################## loading bar

def loading_bar(iteration, total, prefix='', suffix='', decimals=0, length=100, fill=Colorate.Vertical(Colors.red_to_purple, "_",1)):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + ' ' * (length - filled_length)
    print(f'\r{prefix} {bar} {percent}% {suffix}', end='\r')
    # Print New Line on Complete
    if iteration == total:
        print()

#Author JMCG