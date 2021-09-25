from commands.base_command  import BaseCommand
from helpers.constants      import MY_USER_ID
from helpers.message        import message_me_embed
from helpers                import embeds
import discord


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class ShowServerEmotes(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Lists emotes by server"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params' 
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = []
        super().__init__(description, params, secret=True)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message, client):
        # 'params' is a list that contains the parameters that the command 
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object

        if message.author.id != MY_USER_ID:
            return
        servers = client.guilds

        for server in servers:
            emote_list = [str(e) for e in server.emojis]
            embed = discord.Embed(title="Server: {0}".format(server.name), description="".join(emote_list))
            await message_me_embed(client, embed)
