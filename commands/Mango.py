from commands.base_command import BaseCommand

mango_farewell = """August 26, 2020 - June 21, 2021 
My last flex <:mutsukipog:793343586732212234> 
I prob wouldn’t be playing this game for this long if it wasn’t for this guild
Thank you guys for having me apart of this guild, I really enjoyed being able to play and talk to all of you especially during the quarantine <a:unilove:793598511257223198>"""

mango_reason = """The main reason is going to be working full time in 2 weeks while prepping for applications, with summer break now for me I thought that I should really reprioritize what I do… I have thought of quitting before since AL started to feel like a chore… like I know I can log in warrior this game, but I guess I just want to break out of the habit of having to login to a game everyday <:Sadge:804605195170349057>
If anyone wants my account for free dm me, I put quite a lot of money into this game so I want to make sure this acc goes to someone I can trust"""


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class Mango(BaseCommand):

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

        await message.channel.send(mango_farewell)
        await message.channel.send(mango_reason)
