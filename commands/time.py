from commands.base_command import BaseCommand
import numpy as np
from helpers import parse_time, ships, constants, embeds
import discord


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class Time(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Gives a list of what ships you might have built"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params' 
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = ["time"]
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
            string = ' '.join(params)

            buildtime = parse_time.parse_time(string)

            tolerance = buildtime * 0.03

            results = ships.get_ships_with_buildtime(buildtime, tolerance)

            split_results = embeds.split_list(results, 25)

            if len(split_results) == 1:
                embed = discord.Embed(title="Build time = {0}".format(parse_time.minutes_to_hms(buildtime)),
                                      color=constants.SILVER_HEX)
                embeds.populate_build_time(embed, results)

                await message.channel.send(embed=embed)
            elif len(split_results) <= 0:
                await message.channel.send("No ships found for time {0}".format(parse_time.minutes_to_hms(buildtime)))
            else:
                pt = 1
                for part_result in split_results:
                    embed = discord.Embed(title="part{0}: Build time = {1}".format(pt,
                                                                                parse_time.minutes_to_hms(buildtime)),
                                          color=constants.SILVER_HEX)
                    embeds.populate_build_time(embed, part_result)

                    await message.channel.send(embed=embed)
                    pt += 1
