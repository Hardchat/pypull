#!/bin/sh
apt update -y;
apt upgrade -y;
apt install python3 -y;
apt install python3-pip -y;
pip3 install scapy;