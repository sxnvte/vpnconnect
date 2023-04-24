#!/bin/bash

echo "Welcome to vpnconnect instllaer!"

SCRIPT_NAME="vpnconnect.py"

SCRIPT_PATH=$(realpath $SCRIPT_NAME)

if [ ! -f "$SCRIPT_PATH" ]; then
  echo "cannot find $SCRIPT_NAME"
  exit 1
fi 

INSTALL_PATH="/usr/bin/vpnconnect"

sudo cp "$SCRIPT_PATH" "$INSTALL_PATH"

sudo chmod +x "$INSTALL_PATH"

echo "vpnconnect has been installed in $INSTALL_PATH"
