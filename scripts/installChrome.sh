#!/bin/bash
set -ex
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
wget -O firefox-stable.exe https://download.mozilla.org/?product=firefox-latest&os=win64&lang=en-US
sudo apt install ./google-chrome-stable_current_amd64.deb
sudo apt-get install wine
sudo wine ./firefox-stable.exe
