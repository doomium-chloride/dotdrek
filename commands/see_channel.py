from commands.base_command import BaseCommand
from utils import get_emoji
from helpers import message, constants, regex
import discord


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class SeeChannel(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "See channel"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params'
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = ["channel id"]
        super().__init__(description, params, secret=True)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message_obj: discord.Message, client):
        # 'params' is a list that contains the parameters that the command
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object

        if message_obj.author.id != constants.MY_USER_ID:
            print("{0} tried to use this secret function".format(message_obj.author.display_name))
            return;

        channel_id = int(params[0])

        channel: discord.TextChannel = client.get_channel(channel_id)

        if channel == None:
            return await message.message_me(client, "Channel with id '{0}' not found".format(channel_id))

        embed = discord.Embed(title="Channel info")
        embed.add_field(name="name", value=str(channel.name))
        embed.add_field(name="topic", value=str(channel.topic))
        embed.add_field(name="last message", value=str(channel.last_message))
        try:
            await message.message_me_embed(client, embed)
        except Exception as e:
            await message.message_me(client, "Failed error is {1}".format(e))