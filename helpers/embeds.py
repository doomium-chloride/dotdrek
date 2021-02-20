from .ships import get_ship_construction_string, get_ship_construction_time, get_ship_name


def populate_build_time(embed, ships):
    for ship in ships:
        name_string = "{0} -- {1}".format(
            get_ship_name(ship), ship['rarity'])
        value_string = "{0} -- {1}".format(get_ship_construction_time(
            ship), get_ship_construction_string(ship))
        embed.add_field(name=name_string, value=value_string, inline=False)
