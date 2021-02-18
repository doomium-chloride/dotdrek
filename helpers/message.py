import discord
from .constants import MY_USER_ID

async def message_me(client, msg):
    print("sending message... " + msg)
    try:
        await client.wait_until_ready()
        me = await client.fetch_user(MY_USER_ID)
        my_dm_channel = await me.create_dm()
        await my_dm_channel.send(msg)
    except Exception as e:
        print("Oh no message to self failed!")
        print(e)

