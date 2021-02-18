from commands.base_command  import BaseCommand
from helpers.rate_up import build_chance
import numpy as np


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class Stats(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Shows rate up chance"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params' 
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = ["build rate", "builds"]
        super().__init__(description, params)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message, client):
        # 'params' is a list that contains the parameters that the command 
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object

        try:
            build_rate = params[0]
            if build_rate[-1] == '%':
                build_rate = float(build_rate[:-1]) / 100
            else:
                build_rate = float(build_rate)
            builds = int(params[1])
        except ValueError:
            await client.send_message(message.channel,
                                      "Build rate must be a decimal or percentage and builds must be a positive number")
            return

        if build_rate > 1:
            build_rate = build_rate / 100
        
        if build_rate > 1:
            await client.send_message(message.channel,
                                      "Build rate must be a chance 0 - 1, can be percentage or decimal")
            return

        if build_rate < 0:
            await client.send_message(message.channel,
                                      "Build rate must be positive")
            return
        
        if builds < 0:
            await client.send_message(message.channel,
                                      "The number of builds must be positive")
            return

        build_chance_decimal = build_chance(build_rate, builds)

        build_chance_percentage = np.round(build_chance_decimal * 100, 4)

        msg = "Chance to build a ship at {0}% build rate is {1}%".format(np.round(build_rate * 100, 4), build_chance_percentage)

        await message.channel.send(msg)
