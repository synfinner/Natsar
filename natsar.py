#!/usr/bin/env python3

import sys
from modules import tele as tg
from time import sleep

# function to get file links from bot
def get_file_links(token):
    # create a telegram bot object
    bot = tg.TelegramBot(token)
    # send a request to the telegram bot api
    response = bot.get_tg_files()
    print("\n##############+Bot Files+###################")
    for paths in response:
        # print the file link
        print("File Link: https://api.telegram.org/file/bot{}/{}".format(token, paths))
        print("-------------------------------------------")
    print("############################################\n")

# function to get bot updates
def get_usernames(token):
    bot = tg.TelegramBot(token)
    response = bot.send_request('getUpdates')
    # ask the user if they would like to attempt to get profile phone and last online status and get the user input
    user_input = input("Would you like to attempt to get profile phone and last online status (requires API!)? (y/n): ")
    # if the user input is y, then set the apiGrab variable to True
    if user_input == 'y':
        apiGrab = True
    else:
        apiGrab = False
    print("##############+Bot Users+###################")
    for i in response:
        # make a call to the extract_profile_data function with the profile link
        profile = bot.extract_profile_data('https://t.me/{}'.format(i[1]))
        print("-------------------------------------------")
        print("User ID: {}".format(i[0]))
        print("Username: {}".format(i[1]))
        print("Profile Link: https://t.me/{}".format(i[1]))
        print("Profile Title: {}".format(profile[1]))
        print("Profile Description: {}".format(profile[0]))
        if apiGrab:
            resolver = tg.TelegramUser(i[1])
            userdata = resolver.resolv_user()
            print("User Phone: {}".format(userdata.phone))
            print("User Language Code: {}".format(userdata.lang_code))
            try:
                print("User Last Online (UTC): {}".format(userdata.status.was_online.strftime('%Y-%m-%d %H:%M:%S')))
            except AttributeError:
                print("User Status: Online")
            # sleep for 2 seconds so we don't overly abuse the api
            sleep(2)
        else:
            pass
    print("############################################\n")

def get_bot_info(token):
    # create a telegram bot object
    bot = tg.TelegramBot(token)
    # send a request to the telegram bot api
    response = bot.send_request('getMe')
    # print the bot first name, last name, and username
    print("##############+Bot info+####################")
    # print the bot ID number
    print("Bot ID: {}".format(response[2]))
    # the bot username
    print("Bot Username: {}".format(response[0]))
    # print the bot first name
    print("Bot Name: {}".format(response[1]))
    print("############################################\n")

def main(token):
    # get the bot info
    get_bot_info(token)
    # call a function to get bot users
    get_usernames(token)
    # call a function to get file links from bot
    get_file_links(token)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: natsar.py <tg_bot>')
        sys.exit(1)
    # call main()
    main(sys.argv[1])
