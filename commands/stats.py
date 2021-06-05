from commands.base_command import BaseCommand
from utils import get_emoji
from random import randint
from helpers import ships, colours, embeds
import discord


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class Stats(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Show Stats of a Ship"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params' 
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = ["ship"]
        super().__init__(description, params)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message, client):
        # 'params' is a list that contains the parameters that the command 
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object

        async with message.channel.typing():
            kai = (params[-1].lower() == 'kai') and len(params) >= 2
            if kai:
                ship_name = ' '.join(params[:-1])
            else:
                ship_name = ' '.join(params)

            ship = ships.get_closest_matching_ship(ship_name)

            kai = kai and bool(ship.get('retrofit'))

            if ship is None:
                return await message.channel.send("No ship named '{0}' found".format(ship_name))

            embed = embeds.ship_stats(ship, kai)

            await message.channel.send(embed=embed)
