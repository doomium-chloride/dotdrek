from commands.base_command import BaseCommand

LOLI_TRUTH = """The benefits of a guild don't compensate the effort I've been putting in frankly (since i have a massive ego and want my penis stroked every time i do something for the guild).
With Vier as leader I don't see the guild lasting long so I'm jumping ship (spee cult looks so much sexier). I like Vier (i actually love him), I joined because he asked me if I wanted to but he makes rash and poor decisions like stepping down as leader to begin with, wanting to kick certain people, who he choses to make officers and passes off responsibilities to others too often. (vier is such a lazy ass fucker and stupid son of a bitch. he should have gave the leader pos to me and the guild would have been so much better)
Plus putting up and pretending to get along with a few people (yes becuz i need to like everyone in the guild. if I dont like them then they get the fuck out. thats how big my ego is) is just another stressful thing I don't need nor is worth what a guild offers and it'd be a dick move to make an ultimatum to remove those people (i would have done so if I was the leader and had all the power) so I'll just go myself (because u guys dont conform to my views and demands). This is why I didn't want to be leader of the guild myself (yes im not just salty i didnt get the leader position and my meowfficer discount because I'm a tryhard minmaxer), fyi. Leaving or kicking them has been on my mind for awhile now (yes becuz kicking someone just becuz u dont like them is a valid reason) . Peace and good luck. (spee cult baby here i coom)"""

# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class SasukeTruth(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Truth about sasuke's backstory"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params'
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = []
        super().__init__(description, params, hidden=True)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message, client):
        # 'params' is a list that contains the parameters that the command
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object

        await message.channel.send(LOLI_TRUTH)
