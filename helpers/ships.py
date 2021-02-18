from azurlane.azurapi import AzurAPI
from .parse_time import time_str_to_minutes

construction_types = {
    "light": "light",
    "heavy": "heavy",
    "aviation": "special",
    "limited": "event",
    "exchange": "exchange"
}

def get_ship_construction_time(ship):
    return ship['construction']['constructionTime']

def get_ship_construction_set(ship):
    construction = ship['construction']['availableIn']
    construction_set = set()
    for key, value in construction_types.items():
        if key in construction:
            if construction[key]:
                construction_set.add(value)
    return construction_set

def get_ship_construction_string(ship):
    construction_set = get_ship_construction_set(ship)
    return ', '.join(construction_set)


def make_buildtime_comparer(buildtime):
    def comparer(ship):
        build = get_ship_construction_time(ship)
        return abs(time_str_to_minutes(build) - buildtime)
    return comparer

def get_ships_with_buildtime(buildtime, tolerance):
    api = AzurAPI()
    ships = api.getAllShips()
    comparer = make_buildtime_comparer(buildtime)
    ship_filter = lambda ship: comparer(ship) < tolerance
    filtered_ships = list(filter(ship_filter, ships))
    filtered_ships.sort(key=comparer)
    return filtered_ships

def get_ship_name(ship, lang = "en"):
    return ship['names'][lang]