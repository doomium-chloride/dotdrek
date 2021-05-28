from commands.base_command import BaseCommand
from helpers import web_request
import random

CHEST_LINK = "https://raw.githubusercontent.com/doomium-chloride/dotdrek/master/Assets/json/drek_pics.json"


class Chest(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Offerings of drek from the community chest"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params' 
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = []
        super().__init__(description, params)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message, client):
        # 'params' is a list that contains the parameters that the command 
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object

        coomunity_chest = web_request.fetch_json(CHEST_LINK)

        await message.channel.send(random.choice(coomunity_chest))
