#!/bin/bash
set -ex
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
wget -O firefox-stable.tar.bz2 https://download.mozilla.org/?product=firefox-latest&os=linux&lang=en-US
sudo apt install ./google-chrome-stable_current_amd64.deb
sudo apt install ./firefox-stable.tar.bz2
sudo apt install firefox-stable.tar.bz2
