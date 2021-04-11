from .ships import get_ship_construction_string, get_ship_construction_time, get_ship_name


def populate_build_time(embed, ships):
    for ship in ships:
        name_string = "{0} -- {1}".format(
            get_ship_name(ship), ship['rarity'])
        value_string = "{0} -- {1}".format(get_ship_construction_time(
            ship), get_ship_construction_string(ship))
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