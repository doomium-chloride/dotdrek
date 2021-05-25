from commands.base_command import BaseCommand
import random

COOMUNITY_CHEST = (
    "https://cdn.discordapp.com/attachments/823836976893526026/845914224589144064/Drek1494739.png",
    "https://cdn.discordapp.com/attachments/823824715437178890/846675204045275146/a3fd2926375e9bcf2f7951c9fead7ca7.png",
    "https://cdn.discordapp.com/attachments/823836976893526026/831825061551800360/drake_azur_lane_drawn_by_vayneeeee__sample-132aaad7996c900e88d91fb8b4ccb844.png",
    "https://cdn.discordapp.com/attachments/823836976893526026/827307492073013268/illust_86496469_20210402_103030.png",
    "https://cdn.discordapp.com/attachments/745929580279234560/825226829841301504/d322e8be86a42144d966fe53a0ad4191_1.jpg",
    "https://cdn.discordapp.com/attachments/823836976893526026/823841926226640906/83088295_p1_master1200.png",
    "https://cdn.discordapp.com/attachments/823836976893526026/823841267455885312/84188422_p0.png"
)


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

        await message.channel.send(random.choice(COOMUNITY_CHEST))
