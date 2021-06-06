from commands.base_command  import BaseCommand
from helpers                import ships, colours
import discord

# Your friendly example event
# Keep in mind that the command name will be derived from the class name
# but in lowercase

# So, a command class named Random will generate a 'random' command
class Skills(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Show skills of a certain ship"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params' 
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = ["ship"]
        super().__init__(description, params)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message, client):
        # 'params' is a list that contains the parameters that the command 
        # expects to receive, t is guaranteed to have AT LEAST as many
        # parameters as specified in __init__
        # 'message' is the discord.py Message object for the command to handle
        # 'client' is the bot Client object

        async with message.channel.typing():

            ship_name = ' '.join(params)

            ship = ships.get_closest_matching_ship(ship_name)

            if ship == None:
                return await message.channel.send("No ship named '{0}' found".format(ship_name))
            
            ship_name = ship['names']['en']

            skills = ship['skills']


            if len(skills) <= 0:
                embed = discord.Embed(title="{0} has no skills".format(ship_name), color=constants.SILVER_HEX)
                await message.channel.send(embed=embed)
            else:
                for skill in skills:
                    if ship_name.lower().endswith('s'):
                        title="{0}' skill: {1}"
                    else:
                        title="{0}'s skill: {1}"
                    embed = discord.Embed(title=title.format(ship_name, skill['names']['en']), color=colours.get_discord_colour(skill['color']), description=skill['description'])
                    skill_img = skill['icon'].replace('?','%3F')
                    embed.set_thumbnail(url=skill_img)
                    await message.channel.send(embed=embed)
                
                