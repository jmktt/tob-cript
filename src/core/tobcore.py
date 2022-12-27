import os
def check_os():
    if os.name == "nt": #windows
        operating_system = "0"
    if os.name == "posix": #unix
        operating_system = "1"
    return(operating_system)

class bcolors:
    YELLOW = '\033[1;33m'
    RESET = '\033[0;0m'

def write(encrypted_text):
    w = open("criptout.txt", "a")
    w.write("\n Cript Text: {0}".format(encrypted_text))
    w.close()



### invalid mansages
invoption_text = ("\n\033[;1m\x1b[31m There is no such option...\033[0;0m\n")
invkey_text = ("\n\033[;1m\x1b[31m This key is not valid...\033[0;0m")