from commands.base_command  import BaseCommand
import discord
from helpers.embeds import list_options


renown = {
    "jihadtrain": "https://cdn.discordapp.com/attachments/728445732964794379/813291838719000636/3RZFC-jihadtrain.webm",
    "devbp": "https://cdn.discordapp.com/attachments/574086416192110595/826733996918177832/5PLU1-devbp.png",
    "cvloadout": "https://cdn.discordapp.com/attachments/574086416192110595/826734165922676786/C1QRP-cvloadout.png",
    "chadtydal": "https://cdn.discordapp.com/attachments/574086416192110595/826734491027505162/KA1DR-unknown.png",
    "cvav": "https://cdn.discordapp.com/attachments/574086416192110595/830015582358601738/image0.png"
}


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class Renown(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "renown bot is dead... still incomplete..."
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params' 
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = ["renown command"]
        super().__init__(description, params)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message, client):
        # 'params' is a list that contains the parameters that the command 
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object

        # below is old method
        # file = discord.File('Assets/Images/DrekAss.png')
        # await message.channel.send(file=file)

        command = ' '.join(params);

        reply = renown.get(command, None)

        if reply != None:
            await message.channel.send(reply)
        else:
            options = list(renown.keys())
            embed = discord.Embed(title="renown bot commands")
            list_options(embed, options)
            await message.channel.send(embed=embed)
