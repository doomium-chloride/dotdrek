from commands.base_command  import BaseCommand
from helpers                import emoji, embeds
import discord


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class ShowEmotes(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "List available emotes"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params'
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = []
        super().__init__(description, params)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message_obj, client):
        # 'params' is a list that contains the parameters that the command
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object

        channel: discord.TextChannel = message_obj.channel

        emojis = [{"name": e.name, "emoji": e} for e in client.emojis]

        split_list = embeds.split_list(emojis, 25)

        for part in split_list:
            part_embed = discord.Embed(title="test")
            for obj in part:
                part_embed.add_field(name=obj["name"], value=obj["emoji"])
            try:
                await channel.send(embed=part_embed)
            except Exception:
                await channel.send("Error sending emote list")
