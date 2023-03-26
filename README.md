# README.md

**Update:** 25 March, 2023 -- Doing a small rewrite of this and how it functions. 

This python script is designed to pull Telegram bot update information, such as each user that is issuing updates. 

Part of the fun of this script is that I wanted to see if it could be done entirely--or limited in intervention--with GitHub CoPilot. 

## Installation and Setup

**Install Dependencies:**

```
pip3 install -r requirements.txt
```

**Get Telegram client API keys:**

Login copy the app_id and app_hash values from:  

* https://my.telegram.org

**Add Telegram API data to env**

Put the app_id and app_hash into a .env file, feel free to rename `.env_sample` to `.env`. First run will ask for you to login to Telegram. This is to create the necessary session file for Telethon. If you copy your cloned repo somewhere, ensure you do not accidentially include your `.session` file to an untrusted third party. 

This is an ongoing project, please feel free to keep checking back as I add functions and more!

## What this script does

* Pulls the Telegram Bot ID, Username, and Name
* Extracts the users that are sending bot updates
* Pulls user profile name and description
* Attempts to pull downloadable file links contained within bot updates
* Use Telethon to grab profile (phone, language code, online status)

## Output

```
./natsar.py 32xxxxxxx2:BANHunxxxxxxxxxxxxxxx0Bt2
##############+Bot info+####################
Bot ID: xxxx[REDACTED]xxxxx
Bot Username: notxxxx[REDACTED]xxxxxbot
Bot Name: xxxx[REDACTED]xxxxx
############################################

##############+Bot Users+###################
-------------------------------------------
User ID: 49xxxx[REDACTED]xxxxx
Username: xxxx[REDACTED]xxxxx
Profile Link: https://t.me/xxxx[REDACTED]xxxxx
Profile Title: xxxx[REDACTED]xxxxx
Profile Description: xxxx[REDACTED]xxxxx.
User Phone: None
User Language Code: None
User Status: Online
-------------------------------------------
User ID: 61xxxx[REDACTED]xxxxx5
Username: xxxx[REDACTED]xxxxx
Profile Link: https://t.me/xxxx[REDACTED]xxxxx
Profile Title: xxxx[REDACTED]xxxxx
Profile Description: xxxx[REDACTED]xxxxx.
User Phone: +1xxxxxxxxxx
User Language Code: None
User Status: Online
-------------------------------------------
############################################

##############+Bot Files+###################
File Link: https://api.telegram.org/file/botxxxx[REDACTED]xxxxx:xxxx[REDACTED]xxxxx/documents/xxxx[REDACTED]xxxxx_redacted
-------------------------------------------
File Link: https://api.telegram.org/file/botxxxx[REDACTED]xxxxx:xxxx[REDACTED]xxxxx/documents/xxxx[REDACTED]xxxxx.txt
-------------------------------------------
############################################
```
