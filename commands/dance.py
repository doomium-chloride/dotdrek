from commands.base_command  import BaseCommand
import discord


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class Dance(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "drek dance"
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

        # below is old method
        # file = discord.File('Assets/Images/DrekAss.png')
        # await message.channel.send(file=file)

        await message.channel.send("https://media.discordapp.net/attachments/468719321087082516/817815678031102014/image0.gif")