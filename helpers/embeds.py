from .ships import get_ship_construction_string, get_ship_construction_time, get_ship_name
import discord


def get_buildtime_string(ship):
    construction = get_ship_construction_string(ship)
    time = get_ship_construction_time(ship)
    if not bool(construction):
        return time
    return "{0} -- {1}".format(time, construction)

def populate_build_time(embed, ships):
    for ship in ships:
        name_string = "{0} -- {1}".format(
            get_ship_name(ship), ship['rarity'])
        value_string = get_buildtime_string(ship)
        embed.add_field(name=name_string, value=value_string, inline=True)

def show_servers(embed, servers):
    for server in servers:
        server_name = server.name
        server_id = server.id
        embed.add_field(name=server_name, value=server_id, inline=True)

def split_list(array, limit):
    return [array[i:i+limit] for i in range(0, len(array), limit)]

def list_options(embed, options):
    for option in options:
        embed.add_field(name=option, value='** **')

def drek_shrine():
    drek_shrine_pic = "https://cdn.discordapp.com/attachments/823824715437178890/837255400436400148/unknown.png"

    embed = discord.Embed(title="may you get sexy rng")
    embed.set_image(url=drek_shrine_pic)

    return embed


def add_slots(embed, slots):
    def add_slot(index):
        slot = slots[index]
        value = "{0} -> {1}".format(slot['minEfficiency'], slot['maxEfficiency'])
        embed.add_field(name=slot['type'], value=value, inline=True)
    for i in range(0, 3):
        add_slot(i)

def add_stats(embed, stats):

    # not inline to separate

    embed.add_field(name='Armor', value=stats['armor'], inline=False)

    stat_names = (
        'health',
        'reload',
        'luck',
        'firepower',
        'torpedo',
        'evasion',
        'speed',
        'antiair',
        'aviation',
        'oilConsumption',
        'accuracy',
        'antisubmarineWarfare'
    )

    optional_stats = ('oxygen', 'ammunition')  # TODO: Add huntingRange

    def add_stat(field):
        value = stats.get(field)
        if value is not None:
            embed.add_field(name=field.title(), value=value, inline=True)

    for field in stat_names:
        add_stat(field)

    for field in optional_stats:
        add_stat(field)


def ship_stats(ship, kai):
    ship_name = ship['names']['en']

    if kai:
        ship_name += ' kai'

    if kai:
        stats = ship['stats']['level120Retrofit']
    else:
        stats = ship['stats']['level120']

    slots = ship['slots']

    thumbnail = ship['thumbnail']

    summary = "{0} {1} class {2} {3}".format(ship['rarity'],
                                             ship['class'], ship['nationality'], ship['hullType'])

    embed = discord.Embed(title=ship_name, description=summary)

    embed.set_thumbnail(url=thumbnail)

    embed.add_field(name="Build", value=get_buildtime_string(ship), inline=False)

    add_slots(embed, slots)

    add_stats(embed, stats)

    return embed
