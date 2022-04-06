#!/bin/bash
set -ex
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb

set -ex
wget -O firefox-stable.tar.bz2 https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=en-US
sudo apt install ./firefox-stable.tar.bz2