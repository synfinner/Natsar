# README.md

This python script is designed to pull Telegram bot update information, such as each user that is issuing updates. 

Part of the fun of this script is that I wanted to see if it could be done entirely--or limited in intervention--with GitHub CoPilot. 

Installation: 

```
pip3 install -r requirements.txt
```

This is an ongoing project, please feel free to keep checking back as I add functions and more!

## Output

```
./natsar.py 32xxxxxxx2:BANHunxxxxxxxxxxxxxxx0Bt2
This script will get data from the telegram bot updates.
It will then get the profile URLs of the users.
Do you want to continue? (y/n): y
Validating the telegram bot token...
Telegram bot token is valid.

############################################
Bot Name: xxxxx
Bot Username: https://t.me/xxxxxxx
Bot ID: 15xxxxxxx
############################################

Getting user profile URLs...


37 user profiles found:
https://t.me/Dxxx
https://t.me/Oxxx
https://t.me/vxxx
https://t.me/xxxx
...

Extracting Telegram profile data:
https://t.me/Dxxx	REDACTED	Redacted profile description
https://t.me/Oxxx	REDACTED	Redacted profile description
https://t.me/vxxx	REDACTED	Redacted profile description
https://t.me/xxxx	REDACTED	Redacted profile description
...
```
