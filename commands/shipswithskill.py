from commands.base_command import BaseCommand
from helpers import ships, colours, embeds
import discord


# So, a command class named Random will generate a 'random' command
class ShipsWithSkill(BaseCommand):

    def __init__(self):
        # A quick description for the help message
        description = "Get all ships with a skill, All Out Assault excluded"
        # A list of parameters that the command will take as input
        # Parameters will be separated by spaces and fed to the 'params'
        # argument in the handle() method
        # If no params are expected, leave this list empty or set it to None
        params = ["skill name"]
        super().__init__(description, params)

    # Override the handle() method
    # It will be called every time the command is received
    async def handle(self, params, message, client):
        skill_name = ' '.join(params)

        async with message.channel.typing():
            skill = ships.get_closest_matching_skill(skill_name)

            if skill is None:
                return await message.channel.send("No skill named '{0}' found".format(skill_name))

            skill_name = skill["names"]["en"]

            description = skill["description"]

            ships_with_skill = ships.dumb_search_ship_by_skill(skill_name)

            split_results = embeds.split_list(ships_with_skill, 25)

            if len(split_results) == 1:
                embed = discord.Embed(title=skill_name,
                                      color=colours.get_discord_colour(skill['color']), description=description)
                skill_img = skill['icon'].replace('?', '%3F')
                embed.set_thumbnail(url=skill_img)

                populate_ships(embed, ships_with_skill)

                await message.channel.send(embed=embed)
            elif len(split_results) <= 0:
                await message.channel.send("No ships found with skill {0}".format(skill_name))
            else:
                pt = 1
                parts = len(split_results)
                for part_result in split_results:
                    title = "{0} {1}/{2}".format(skill_name, pt, parts)
                    embed = discord.Embed(title=title, color=colours.get_discord_colour(skill['color']),
                                          description=description)
                    skill_img = skill['icon'].replace('?', '%3F')
                    embed.set_thumbnail(url=skill_img)

                    populate_ships(embed, part_result)

                    await message.channel.send(embed=embed)
                    pt += 1


def populate_ships(embed, results):
    for ship in results:
        name = ship["names"]["en"]
        summary = "{0} {1} class {2} {3}".format(ship['rarity'],
                                                 ship['class'], ship['nationality'], ship['hullType'])
        embed.add_field(name=name, value=summary)
