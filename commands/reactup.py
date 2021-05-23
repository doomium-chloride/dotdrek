import asyncio
from commands.base_command import BaseCommand
from helpers import constants, emoji
from typing import List
import discord


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class ReactUp(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Temporarily react to messages above"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params'
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = ["number of messages to react", "reactions"]
        super().__init__(description, params)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message_obj, client):
        # 'params' is a list that contains the parameters that the command
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object

        channel: discord.TextChannel = message_obj.channel

        if message_obj.author.id != constants.MY_USER_ID:
            print("{0} tried to use a secret function".format(message_obj.author.display_name))
            return
        try:
            number_of_messages = max(int(params[0]), 0)
            if number_of_messages > 100:
                number_of_messages = 100
        except:
            return await channel.send("error parsing int")
        emoji_names = params[1:]

        server: discord.Guild = channel.guild

        messages: List[discord.Message] = await channel.history(limit=number_of_messages).flatten()

        reactions_to_clear = []

        for msg in messages:
            emote_list: List[discord.Emoji] = emoji.get_emojis(client, server, emoji_names)
            for emote in emote_list:
                if not has_reaction(msg, emote):
                    reactions_to_clear.append((msg, emote))
                    await msg.add_reaction(emote)

        await asyncio.sleep(10)

        await remove_reactions(reactions_to_clear, client.user)


async def remove_reactions(reactions_to_clear, user):
    for react in reactions_to_clear:
        msg: discord.Message = react[0]
        reaction: discord.Emoji = react[1]
        try:
            await msg.remove_reaction(reaction, user)
        except:
            # do nothing message was probably deleted
            pass


def has_reaction(message, reaction):
    message: discord.Message
    reaction: discord.Emoji
    for react in message.reactions:
        if react.emoji == reaction:
            return True
    return False
