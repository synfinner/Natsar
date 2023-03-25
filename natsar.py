#!/usr/bin/env python3

import sys
import requests

# function to format the profile
def profile_format(users):
    # create a list to store the profile
    profile = []
    # loop through the users
    for user in users:
        # create a list to store the profile
        profile.append('https://t.me/{}'.format(user))
    # return the profiles
    return profile

# function to parse the telegram bot updates
def parse_updates(updates):
    # create a list to store the message
    messages = []
    # create a list to store the usernames
    users = []
    # loop through the updates
    for update in updates:
        # try to get the username from the update. if it fails, do nothing
        try:
            # get the username from the update
            username = update['message']['from']['username']
            # if the username is not in the users list, add it
            if username not in users:
                users.append(username)
        except:
            # do nothing
            pass
    # print that we are getting user profile URLs
    print('Getting user profile URLs...\n')
    # remove duplicates from the users list
    users = list(set(users))
    # send the users variable to the profile_format() function
    userProfiles = profile_format(users)
    # print a new line and the number of user profiles base on the length of the userProfiles list
    print("\n{} user profiles found: ".format(len(userProfiles)))
    # for each user profile in the userProfiles list, print it in a nice format
    for userProfile in userProfiles:
        print(userProfile) 
        
# function to validate the telegram bot token
def validate_tg_bot(tg_bot):
    # get the telegram bot updates with tg_bot as the bot token
    url = 'https://api.telegram.org/bot{}/getUpdates'.format(tg_bot)
    response = requests.get(url).json()
    # check if the response is ok
    if response['ok'] == False:
        # if it's not ok, print the error message and exit the script
        print('Error: {}'.format(response['description']))
        sys.exit(1)
    # if it's ok, print that the Telegram bot token is valid
    print('Telegram bot token is valid.')
    # send the response to parse_updates()
    parse_updates(response['result'])

def main(tg_bot):
    # prompt the user to continue or not 
    print('This script will get data from the telegram bot updates.')
    print('It will then get the profile URLs of the users.')
    # get the user's input
    user_input = input('Do you want to continue? (y/n): ')
    # if the user's input is not y, exit the script
    if user_input != 'y':
        sys.exit(0)
    # print that we are validating the telegram bot token
    print('Validating the telegram bot token...')
    # call a function to validate the telegram bot token
    validate_tg_bot(tg_bot)

    

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: natsar.py <tg_bot>')
        sys.exit(1)

    # call main()
    main(sys.argv[1])