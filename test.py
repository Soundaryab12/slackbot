import os
from slackclient import SlackClient
sc = SlackClient('xoxb-394146951447-432142156005-4cvMCcDtyTzQ7cApVKiLtdlS')

def list_channels():
    channels_call = sc.api_call("channels.list")
    if channels_call.get('ok'):
        return channels_call['channels']
    return None

if __name__ == '__main__':
    channels = list_channels()
    if channels:
        print("Channels: ")
        for c in channels:
            print(c['name'] + " (" + c['id'] + ")")
    else:
        print("Unable to authenticate.") 
