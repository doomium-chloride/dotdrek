from commands.base_command  import BaseCommand
import discord


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class Pray(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "pray to the drek"
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

        drek_shrine = "https://cdn.discordapp.com/attachments/823824715437178890/837255400436400148/unknown.png"

        msg = "drek blesses {0}".format(message.author.mention, drek_shrine)

        embed = discord.Embed(title="may you get sexy rng")
        embed.set_image(url=drek_shrine)

        await message.channel.send(msg, embed=embed)