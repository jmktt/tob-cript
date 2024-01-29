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
    RESET = '\033[0;0m'

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
def display_key_box(key):
    key_box =Box.DoubleCube("     YOUR KEY IS : {}     ".format(key))
    print("\n{}".format(key_box))


tname = Colorate.Horizontal(Colors.yellow_to_red, "TOB",1)
cname = Colorate.Horizontal(Colors.red_to_blue, "JMKTT",2)
version= Colorate.Horizontal(Colors.red_to_blue, "1.4",2)
###############################################################

### invalid mensages
invoption_text = (Col.red+"\nThere is no such option...\033[0;0m\n")
invkey_text = (Col.red+"\n This key is not valid...\033[0;0m")
invfile_text = (Col.red+"\n File not found...\033[0;0m")
### status mensages
net_online = (bcolors.YELLOW+"[+]Internet Status: Online"+bcolors.RESET)
net_offline = (bcolors.YELLOW+"[-]Internet Status: Offline"+bcolors.RESET)



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