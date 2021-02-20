from commands.base_command  import BaseCommand
from utils                  import get_emoji
from helpers                 import message, constants
import discord


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class Chat(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Sends a message to a channel in a server"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params' 
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = ["server", "channel", "message"]
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

        server_name = params[0]
        channel_name = params[1]
        msg = ' '.join(params[2:])

        server: discord.Guild = None

        guilds = client.guilds
        for guild in guilds:
            if guild.name.lower() == server_name.lower():
                server = guild
                break
        if server == None:
            return await message.message_me("Server named '{0}' not found".format(server_name))
        
        channel: discord.TextChannel = None

        for guild_channel in server.channels:
            if guild_channel.name == channel_name:
                channel = guild_channel
        
        if channel == None:
            return await message.message_me("Channel named '{0}' not found in server: {1}".format(channel_name, server_name))
        
        try:
            await channel.send(msg)
        except AttributeError as e:
            await message.message_me(client, "Failed to send message '{0}' error is {1}".format(msg, e))