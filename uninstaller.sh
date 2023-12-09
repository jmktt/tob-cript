#!/bin/bash

# ANSI COLORS
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'  # no color

# verify root
if [[ $EUID -ne 0 ]]; then
    echo -e "${RED}This script needs to be run as root. Run with sudo.${NC}"
    exit 1
fi

# dir script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# tob dir
INSTALL_DIR="/usr/bin/tob-cript"

# verify dir
if [ -d "$INSTALL_DIR" ]; then
    # remove dir
    rm -rf "$INSTALL_DIR"
    echo -e "${GREEN}Text-Object Basic Cript files were deleted.${NC}"
else
    echo -e "${YELLOW}Text-Object Basic Cript files not found. Nothing to uninstall.${NC}"
fi

# remove .bashrc
sed -i '/tob-cript/d' "$HOME/.bashrc"

echo -e "${GREEN}Uninstallation complete.${NC}"

exit 0
