from . import state, message

async def log_message(msg, client):
    channel = msg.channel
    channel_id = str(channel.id)
    if channel_id == state.log_channel:
        log_txt = "{0} => {1}".format(msg.author.nick, msg.content)
        await message.message_me(client, log_txt)