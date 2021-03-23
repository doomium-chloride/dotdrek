from commands.base_command import BaseCommand


# This is a convenient command that automatically generates a helpful
# message showing all available commands
class Commands(BaseCommand):

    def __init__(self):
        description = "Displays this help message"
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client):
        from message_handler import COMMAND_HANDLERS
        msg = message.author.mention + "\n"

        # Displays all descriptions, sorted alphabetically by command name
        for cmd in sorted(COMMAND_HANDLERS.items()):
            if(not cmd[1].secret and cmd[1].server == None):
                msg += "\n" + cmd[1].description
            elif message.guild.id == cmd[1].server:
                msg += "\n" + cmd[1].description


        await message.channel.send(msg)
