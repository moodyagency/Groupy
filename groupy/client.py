import os
import requests
import time
import datetime
import groupy
from groupy import Client
from groupy import attachments
from groupy.api import messages


access_token = "oPdzC1eeHQiTf769kv4aW2Z2p85pfWHHpjb1n7iy"
group_id = "92140191"
bot_id = "868ad2fd269ab3cb057a68ed5a"
# The URL for the endpoint that sends messages to a specific group.
group_url = f"https://api.groupme.com/v3/groups/{group_id}/messages"
# The URL for the endpoint that gets the members of a specific group.
members_url = f"https://api.groupme.com/v3/groups/{group_id}/members?token={access_token}"
# The base URL for the GroupMe API.
bot_url = "https://api.groupme.com/v3/bots/post"
# Create a Groupy client
client = Client.from_token(access_token)
# Find the group with the given group_id
group = client.groups.get(group_id)
# Get the members of the group
members = group.members



def send_message(memessage):
    group.post(text=memessage)
    print("My account successfully posted!")
   
send_message("me")


bot = groupy.Bot.bot_with_id(bot_id)
## 🌎💯🔥🔑🚨🚨⏰✅
    
def g_message(gmessage):
    bot.post(text=gmessager)
    print("Bot successfully posted!")
   
g_message("gbot")    
