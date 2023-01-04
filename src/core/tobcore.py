import os
import datetime
from pystyle import Colors, Colorate, Write

def check_os():
    if os.name == "nt": #windows
        operating_system = "0"
    if os.name == "posix": #unix
        operating_system = "1"
    return(operating_system)

class bcolors:
    YELLOW = '\033[1;33m'
    RESET = '\033[0;0m'

now = datetime.datetime.now()
def write(encrypted_text):
    w = open("criptout.txt", "a")
    w.write("\n Cript Text({0}): {1}".format(now,encrypted_text))
    w.close()


### banners
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

cname = Colorate.Horizontal(Colors.red_to_blue, "JMKTT",1)
version= Colorate.Horizontal(Colors.red_to_blue, "1.2",1)
### invalid mansages
invoption_text = ("\n\033[;1m\x1b[31m There is no such option...\033[0;0m\n")
invkey_text = ("\n\033[;1m\x1b[31m This key is not valid...\033[0;0m")