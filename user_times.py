#!/usr/bin/env python3

import sys
import requests
import datetime
import pytz

if len(sys.argv) < 2:
    print("Please provide a Telegram bot token as a command line argument.")
    sys.exit(1)

# Get the bot token from the command line arguments
bot_token = sys.argv[1]

# Retrieve updates from the server
url = f'https://api.telegram.org/bot{bot_token}/getUpdates'
response = requests.get(url)
updates = response.json()['result']

# Create a dictionary to store user interaction times
interaction_times = {}

# Extract each username observed in updates and log interaction times
for update in updates:
    message = update.get('message')
    if message:
        user = message['from']
        username = user.get('username')
        if username:
            # Log interaction time in EDT
            interaction_time_utc = datetime.datetime.utcfromtimestamp(message['date']).replace(tzinfo=pytz.UTC)
            interaction_time_edt = interaction_time_utc.astimezone(pytz.timezone('US/Eastern')).strftime('%Y-%m-%d %H:%M:%S')
            if username not in interaction_times:
                interaction_times[username] = [interaction_time_edt]
            else:
                interaction_times[username].append(interaction_time_edt)

# Print interaction times for each user
for username, times in interaction_times.items():
    print(f"{username} interacted with the bot at the following times (EDT):")
    for time in times:
        print(f"- {time}")
