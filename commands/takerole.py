from commands.base_command  import BaseCommand
import discord
from helpers.constants import DREK_ROLES, DREK_CULT_ID


# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class TakeRole(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Remove role"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params' 
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = ["role names = {0}".format([role for role in DREK_ROLES.keys()])]
        super().__init__(description, params, server=DREK_CULT_ID)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message, client):
        # 'params' is a list that contains the parameters that the command 
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object

        if message.guild == None or message.guild.id != self.server:
            return

        role_name = ' '.join(params)

        member = message.author
        get_role = message.guild.get_role

        role_id = DREK_ROLES.get(role_name)

        if role_id == None:
            return
        
        role = get_role(role_id)

        if role == None:
            return

        await member.remove_roles(role, atomic=True)