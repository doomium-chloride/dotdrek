import asyncio
from commands.base_command import BaseCommand
from helpers import emoji
from typing import List
import discord


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class React(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Temporarily react to the replied message"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params'
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = ["reactions"]
        super().__init__(description, params)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message_obj, client):
        # 'params' is a list that contains the parameters that the command
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object

        message_obj: discord.Message = message_obj

        emoji_names = params[0:]

        reactions_to_clear = []

        try:

            reply = message_obj.reference

            if reply is None:
                slap = await message_obj.channel.send("you need to reply to a message")
                await slap.delete(delay=5)
                return

            channel: discord.TextChannel = client.get_channel(reply.channel_id)

            server: discord.Guild = channel.guild

            msg = await channel.fetch_message(reply.message_id)

            emote_list: List[discord.Emoji] = emoji.get_emojis(client, server, emoji_names)
            for emote in emote_list:
                if not emoji.has_reaction(msg, emote):
                    reactions_to_clear.append((msg, emote))
                    await msg.add_reaction(emote)

            await asyncio.sleep(10)

            await emoji.remove_reactions(reactions_to_clear, client.user)

        except:
            print("Tried to react")
            await message_obj.channel.send("Oh no! failed to react!")
