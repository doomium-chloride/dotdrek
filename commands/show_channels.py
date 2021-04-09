from commands.base_command  import BaseCommand
from utils                  import get_emoji
from random                 import randint
from helpers                import constants, message, embeds
import discord


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class ShowChannels(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Lists channels of a server"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params' 
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = ["server"]
        super().__init__(description, params, secret=True)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message_obj, client):
        # 'params' is a list that contains the parameters that the command 
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object

        if message_obj.author.id != constants.MY_USER_ID:
            print("{0} tried to use this secret function".format(message_obj.author.display_name))
            return;

        server_id = params[0]

        server: discord.Guild = None

        guilds = client.guilds
        for guild in guilds:
            if str(guild.id) == server_id:
                server = guild
                break
        if server == None:
            return await message.message_me(client, "Server with id '{0}' not found".format(server_id))

        split_list = embeds.split_list(server.channels, 25)
        for channel_list in split_list:
            embed = discord.Embed(title="Channels in {0}".format(server.name))
            embeds.show_servers(embed, channel_list)
            await message.message_me_embed(client, embed)

