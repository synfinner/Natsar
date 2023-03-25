#!/usr/bin/env python3

# import the requests module
import requests

#class to send a request to the telegram bot api based on user supplied endpoint
class TelegramBot:
    # function to initialize the class
    def __init__(self, token):
        # set the token
        self.token = token
    
    def extract_profile_data(self, profile):
        # send a request to the profile link and get the response
        profile = requests.get(profile).text
        # get the profile data
        profile_desc = profile.split('og:description" content="')[1].split('"')[0]
        # get the profile title from og:title
        profile_title = profile.split('og:title" content="')[1].split('"')[0]
        # print tab delimited profile data
        return profile_desc, profile_title
        
    # function to remove duplicates from a list
    def remove_duplicates(self, users):
        # create an empty list
        new_users = []
        # loop through the list
        for i in users:
            # if the user is not in the new list, append it
            if i not in new_users:
                new_users.append(i)
        # return the new list
        return new_users

    # function to send a request to the telegram bot api
    def send_request(self, endpoint):
        # send a request to the telegram bot api
        response = requests.get('https://api.telegram.org/bot{}/{}'.format(self.token, endpoint))
        # if the response is not 200, raise an exception
        if response.status_code != 200:
            raise Exception('Error: {}'.format(response.text))
        if endpoint == 'getMe':
            # Try to return the bot username, first name, username, and id
            try:
                return response.json()['result']['username'], response.json()['result']['first_name'],\
                    response.json()['result']['id']
            except KeyError:
                raise Exception('Error: {}'.format(response.text))
        elif endpoint == 'getUpdates':
            # append the user id and username to a list
            users = []
            for i in response.json()['result']:
                try:
                    users.append((i['message']['from']['id'], i['message']['from']['username']))
                except KeyError:
                    pass
            # call a function to remove duplicates
            users = self.remove_duplicates(users)
            return users