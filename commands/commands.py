from commands.base_command import BaseCommand


# This is a convenient command that automatically generates a helpful
# message showing all available commands
class Commands(BaseCommand):

    def __init__(self):
        description = "Displays this help message"
        params = None
        super().__init__(description, params)

    async def handle(self, params, message, client, temp=False):
        from message_handler import COMMAND_HANDLERS
        msg = message.author.mention + "\n"

        # Displays all descriptions, sorted alphabetically by command name
        for cmd in sorted(COMMAND_HANDLERS.items()):
            command = cmd[1]
            visible = not command.secret and not command.hidden
            if visible and command.server is None:
                msg += "\n" + command.description
            elif message.guild is not None and message.guild.id == command.server and visible:
                msg += "\n" + command.description

        sent_msg = await message.channel.send(msg)

        if temp:
            await sent_msg.delete(delay=5)
