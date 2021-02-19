from commands.base_command  import BaseCommand
import numpy as np
from helpers import parse_time, ships
import discord

# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class Buildtime(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Gives a list of what ships you might have built from a specific build pool"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params' 
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = ["build pool", "time"]
        super().__init__(description, params)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message, client):
        # 'params' is a list that contains the parameters that the command 
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object

        pool = params[0]

        string = ' '.join(params[1:])

        buildtime = parse_time.parse_time(string)

        tolerance = 5

        results = ships.get_ships_with_buildtime(buildtime, tolerance, pool)

        pool_string = ships.get_build_pool(pool)

        if(pool_string == None):
            pool_string = "unknown"
        else:
            try:
                pool_string = ships.construction_types[pool_string]
            except KeyError as e:
                print("Unexpected value in buildtime's pool_string. string={0} error={1}".format(pool_string, e))
                pool_string = "unknown"

        embed = discord.Embed(title="Build time = {0} from {1}".format(parse_time.minutes_to_hms(buildtime), pool_string))
        for ship in results:
            name_string = "{0} -- {1}".format(ships.get_ship_name(ship), ship['rarity'])
            value_string = "{0} -- {1}".format(ships.get_ship_construction_time(ship), ships.get_ship_construction_string(ship))
            embed.add_field(name=name_string, value=value_string, inline=False)

        await message.channel.send(embed=embed)
