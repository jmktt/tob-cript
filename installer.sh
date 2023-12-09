#!/bin/bash

# ANSI COLORS
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'  # no color

# verify root
if [[ $EUID -ne 0 ]]; then
    echo -e "${RED}This script needs to be run as root. Run with sudo.${NC}"
    exit 1
fi

# dir script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# verify python3
command -v python3 >/dev/null 2>&1 || { echo -e "${RED}Python3 is not installed. Please install Python3.${NC}"; exit 1; }

# intall requirements silently
pip3 install --quiet -r "$DIR/requirements.txt" >/dev/null 2>&1
echo -e "'requirements.txt'${GREEN} installation done.${NC}"

# create dir
mkdir -p /usr/bin/tob-cript

# copy tob
cp -ru "$DIR"/* /usr/bin/tob-cript/

# permission
chmod +x /usr/bin/tob-cript/tob.py

# add to bash for the current session
export PATH=$PATH:/usr/bin/tob-cript/

# add to bashrc for permanent change
echo "export PATH=\$PATH:/usr/local/bin/tob-cript/" >> "$HOME/.bashrc"

# link tob.py to tob if the link doesn't already exist
if [ -e /usr/bin/tob-cript/tob ]; then
    echo -e "${YELLOW}Link ${NC}'tob'${YELLOW} already exists."
else
    ln -s /usr/bin/tob-cript/tob.py /usr/bin/tob-cript/tob
    echo -e "${GREEN}Link ${NC}'tob' ${GREEN}created."
fi

echo -e "${GREEN}Installation complete. Now you can run${NC} 'tob'."
echo -e "${YELLOW}Note: Please restart your terminal for the changes to take effect.${NC}"

exit 0
