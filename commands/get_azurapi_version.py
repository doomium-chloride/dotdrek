from commands.base_command  import BaseCommand
from helpers import constants, message
from azurlane import AzurAPI

class Version(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Get azur api version"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params' 
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = []
        super().__init__(description, params, True)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message_obj, client):
        # 'params' is a list that contains the parameters that the command 
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object
        if message_obj.author.id != constants.MY_USER_ID:
            return

        async with message_obj.channel.typing():
            api = AzurAPI()
            version = api.getVersion()
            print(version)
            await message.message_me(client, version)