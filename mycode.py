import os
from slackclient import SlackClient
sc = SlackClient('xoxb-394146951447-432142156005-4cvMCcDtyTzQ7cApVKiLtdlS')

def list_users():
    users_call = sc.api_call("users.list")
    if users_call.get('ok'):
        return users_call['members']
    return None

def send_message(userid):
    sc.api_call(
        "chat.postMessage",
        channel=userid,
        text="Hey there! How are you?",
        username='groupadmin',
        icon_emoji=':robot_face:'
    )

if __name__ == '__main__':   
    users = list_users()
    if users:
        for u in users:
            send_message(u['id'])
        print("Success!")

