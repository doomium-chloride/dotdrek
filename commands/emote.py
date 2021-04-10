from commands.base_command  import BaseCommand
from FuzzySearchPy          import FuzzySearch
import discord


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class Emote(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Use nitro emotes"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params'
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = ["emote names"]
        super().__init__(description, params)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message_obj, client):
        # 'params' is a list that contains the parameters that the command
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object

        emote_names = params[0:]

        server: discord.Guild = message_obj.guild

        channel: discord.TextChannel = message_obj.channel

        emojis = []
        server_emojis = [e.name for e in server.emojis]
        search_options = { "sort": True, "caseSensitive": False }
        emoji_searcher = FuzzySearch(server_emojis, [], search_options)
        for emote_name in emote_names:
            emoji = discord.utils.get(server.emojis, name=emote_name)
            if emoji is None:
                possible_emojis = emoji_searcher.search(emote_name)
                if len(possible_emojis) >= 1:
                    emoji = discord.utils.get(server.emojis, name=possible_emojis[0])
            if emoji:
                emojis.append(emoji)

        emoji_strs = [str(emoji) for emoji in emojis]
        try:
            await channel.send(' '.join(emoji_strs))
        except Exception:
            await channel.send("Emote sending encountered a problem")