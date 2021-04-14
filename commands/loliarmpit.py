from commands.base_command import BaseCommand
import discord
from helpers.constants import DIE_JAGER_ID

LOLI_LORE = """The benefits of a guild don't compensate the effort I've been putting in frankly. 
With Vier as leader I don't see the guild lasting long so I'm jumping ship. I like Vier, I joined because he asked me if I wanted to but he makes rash and poor decisions like stepping down as leader to begin with, wanting to kick certain people, who he choses to make officers and passes off responsibilities to others too often.
Plus putting up and pretending to get along with a few people is just another stressful thing I don't need nor is worth what a guild offers and it'd be a dick move to make an ultimatum to remove those people so I'll just go myself. This is why I didn't want to be leader of the guild myself, fyi. Leaving or kicking them has been on my mind for awhile now. Peace and good luck."""

# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class LoliArmpit(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "SASUKEEE backstory"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params'
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = []
        super().__init__(description, params, server=DIE_JAGER_ID)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message, client):
        # 'params' is a list that contains the parameters that the command
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object

        if message.guild == None or message.guild.id != self.server:
            return

        await message.channel.send(LOLI_LORE)