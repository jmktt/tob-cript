#!/bin/bash

# verify root
if [[ $EUID -ne 0 ]]; then
    echo "This script needs to be run as root. Run with sudo."
    exit 1
fi

# dir script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# verify python3
command -v python3 >/dev/null 2>&1 || { echo >&2 "Python3 is not installed. Please install Python3."; exit 1; }

# intall requirements
pip3 install -r "$DIR/requirements.txt"

# create dir
mkdir -p /usr/local/bin/tob-cript

# copy tob
cp -ru "$DIR"/* /usr/local/bin/tob-cript/

# permission
chmod +x /usr/local/bin/tob-cript/tob.py

# add to bash
echo "export PATH=\$PATH:/usr/local/bin/tob-cript/" >> "$HOME/.bashrc"

# link tob.py to tob
ln -s /usr/local/bin/tob-cript/tob.py /usr/local/bin/tob-cript/tob

echo "Installation complete. Now you can run 'tob'."

exit 0
