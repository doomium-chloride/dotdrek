import settings
import discord

# Base command class
# Do not modify!
class BaseCommand:

    def __init__(self, description, params, secret = False):
        self.name = type(self).__name__.lower()
        self.params = params
        self.secret = secret

        desc = f"**{settings.COMMAND_PREFIX}{self.name}**"

        if self.params:
            desc += " " + " ".join(f"*<{p}>*" for p in params)

        desc += f": {description}."
        self.description = desc

    # Every command must override this method
    async def handle(self, params: list[str], message: discord.Message, client: discord.Client):
        raise NotImplementedError  # To be defined by every command
