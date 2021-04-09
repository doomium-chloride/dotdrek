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

async def message_me_embed(client, embed):
    print("sending embed to me")
    try:
        await client.wait_until_ready()
        me = await client.fetch_user(MY_USER_ID)
        my_dm_channel = await me.create_dm()
        await my_dm_channel.send(embed=embed)
    except Exception as e:
        print("Oh no embed to self failed!")
        print(e)
