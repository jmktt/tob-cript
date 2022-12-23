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