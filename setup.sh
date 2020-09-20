#!/bin/sh
apt update -y;
apt upgrade -y;
apt install python3 -y;
apt install python3-pip -y;
pip3 install scapy;
pip3 install ipinfo;
echo "alias pull='python3 pypull.py'" >> ~/.bashrc
echo "alias pull='python3 pypull/pypull.py'" >> ~/.bashrc
alias pull='python3 pypull.py'
