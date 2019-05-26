import json
from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http


def ws_connect(message):
    message.reply_channel.send({"accept": True})
    group = message['path'].replace('/', '')
    Group(group).add(message.reply_channel)


def ws_disconnect(message):
    group = message['path'].replace('/', '')
    Group(group).discard(message.reply_channel)


def ws_message(message):
    group = message['path'].replace('/', '')
    Group(group).send({
        "text": ">> {}".format(message.content['text']),
    })
