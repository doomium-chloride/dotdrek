from commands.base_command  import BaseCommand
from helpers                import embeds


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class Bless(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "ask drek to bless others"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params' 
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = ["blessees"]
        super().__init__(description, params)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message, client):
        # 'params' is a list that contains the parameters that the command 
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object

        blessee_list = message.mentions

        blessee_mentions = [blessee.mention for blessee in blessee_list]

        if len(blessee_mentions) <= 0:
            await message.channel.send("there is no one to bless")
            return

        if len(blessee_mentions) <= 2:
            blessee_string = " and ".join(blessee_mentions)
        else:
            last_2 = blessee_mentions[-2:]
            not_last_2 = blessee_mentions[:-2]
            blessee_string = ", ".join(not_last_2)
            blessee_string += " " + " and ".join(last_2)

        msg = "{0} asks drek to bless {1}".format(message.author.mention, blessee_string)

        embed = embeds.drek_shrine()

        await message.channel.send(msg, embed=embed)
