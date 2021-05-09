#!/bin/bash

APT_PACKAGES='build-essential python3 python3-pip'
YUM_PACKAGES='wget curl tcpdump gcc gcc-c++ make python3-devel python3 python3-pip'
PIP_PACKAGES='scapy ipinfo'
has_apt() {
         apt update && apt upgrade -y; apt-get install $APT_PACKAGES -y && pip3 install $PIP_PACKAGES; echo "alias pull='python3 pypull.py'" >> ~/.bashrc && echo "alias pull='python3 ~/pypull/pypull.py'" >> ~/.bashrc;
}

has_yum() {
         yum update -y; yum install $YUM_PACKAGES -y && pip3 install $PIP_PACKAGES; echo "alias pull='python3 pypull.py'" >> ~/.bashrc && echo "alias pull='python3 ~/pypull/pypull.py'" >> ~/.bashrc;
}

package() {
    [ -x "$(which $1)" ]
}

if package apt-get ; then has_apt
elif package yum ; then has_yum
else
    echo 'Unknown package manager! Manual dependency installation required.'
    exit 2
fi
