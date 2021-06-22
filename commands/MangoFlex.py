from commands.base_command import BaseCommand

mango_flexes = (
    "https://cdn.discordapp.com/attachments/823824715437178890/856800903418871838/Player_Card.png",
    "https://cdn.discordapp.com/attachments/823824715437178890/856800957861068830/Main_Screen.png",
    "https://cdn.discordapp.com/attachments/823824715437178890/856814545296687114/Dock_1.png",
    "https://cdn.discordapp.com/attachments/823824715437178890/856814584768888862/Dock_2.png",
    "https://cdn.discordapp.com/attachments/823824715437178890/856814624342147072/Dock_3.png",
    "https://cdn.discordapp.com/attachments/823824715437178890/856814663114948608/Depot_-_Gear_1.png",
    "https://cdn.discordapp.com/attachments/823824715437178890/856814710938664960/Depot_-_Gear_2.png",
    "https://cdn.discordapp.com/attachments/823824715437178890/856814768458956830/Depot_-_Gear_3.png",
    "https://cdn.discordapp.com/attachments/823824715437178890/856814793830957056/PRDR.png",
    "https://cdn.discordapp.com/attachments/823824715437178890/856814820023599114/Dorm.png",
    "https://cdn.discordapp.com/attachments/823824715437178890/856814851255042059/Cats.png",
    "https://cdn.discordapp.com/attachments/823824715437178890/856814883038691338/Depot_-_Items.png"
)


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class MangoFlex(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Mango, a retired Die Jäger member"
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

        for link in mango_flexes:
            await message.channel.send(link)
