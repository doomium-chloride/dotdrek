from commands.base_command  import BaseCommand
from helpers                import constants, message
import discord


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class Delete(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "See stuff"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params'
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = ["channel id", "msg id"]
        super().__init__(description, params, secret=True)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message_obj, client):
        # 'params' is a list that contains the parameters that the command
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object

        if message_obj.author.id != constants.MY_USER_ID:
            print("{0} tried to use a secret function".format(message_obj.author.display_name))
            return

        try:
            channel_id = int(params[0])
            message_id = int(params[1])
        except:
            return await message.message_me(client, "Error parsing int")

        channel: discord.TextChannel = client.get_channel(channel_id)

        if channel == None:
            return await message.message_me(client, "Channel with id '{0}' not found".format(channel_id))

        try:
            msg_id = int(message_id)
            target_message = await channel.fetch_message(msg_id)
            await target_message.delete()
        except:
            await message.message_me(client, "Failed to delete to message")