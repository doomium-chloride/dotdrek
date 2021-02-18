from commands.base_command  import BaseCommand
from utils                  import get_emoji
from random                 import randint
from helpers.constants      import MY_USER_ID
from helpers.message        import message_me


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class ShowServers(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Lists servers the bot is in"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params' 
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = []
        super().__init__(description, params, True)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message, client):
        # 'params' is a list that contains the parameters that the command 
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object

        if message.author.id != MY_USER_ID:
            return

        guilds_names = [guild.name for guild in client.guilds]
        msg = ', '.join(guilds_names)

        await message_me(client, msg)
