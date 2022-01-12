# Wireguard Watchdog

This is a very simple Python script that requires very little configuration and has few dependencies. 

This script is destined for machines that __have an internet kill switch__, meaning no internet access unless the Wireguard VPN is up. 

The original script linked below is better for pinging IP the Wireguard server IP. 

## Information

This script was re-written based on a script shared on Reddit. [Source is here](https://www.reddit.com/r/WireGuard/comments/er2hq8/comment/hk1pu0b/?utm_source=share&utm_medium=web2x&context=3)

## Where to use this script: 

* A system that uses Wireguard 
* A kill-switch that only allows internet access if the VPN is up

## How to use: 

1. Copy the script to your desired destination
2. Install requests if you don't already have it (`python -m pip install requests`)
3. Check the script is suitably configured for you. 
4. Add to your __root__ crontab (`sudo crontab -e`). Root access is used to restart the Wireguard service:
`*/5 * * * * /usr/bin/python3 /home/USER/wg-watchdog.py`

## Options for you to change the script: 

* Use `pythonping` to ping a server instead of checking a website is available. Note that this library does require administrator escalation. 
