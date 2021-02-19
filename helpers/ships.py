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

def get_build_pool(text):
    pool = text.lower()
    if pool.startswith("l") :
        return "light"
    if pool.startswith("h") :
        return "heavy"
    if pool.startswith("s") or pool.startswith("a"):
        return "aviation"
    if pool.startswith("e"):
        return "limited"
    return None

def ships_by_construction_pool(ships, pool):
    if pool == None:
        return ships
    build_pool = get_build_pool(pool)
    if build_pool == None:
        return ships
    return filter(lambda ship: ship['construction']['availableIn'][build_pool], ships)

def get_ships_with_buildtime(buildtime, tolerance, pool = None):
    api = AzurAPI()
    ships = ships_by_construction_pool(api.getAllShips(), pool)
    comparer = make_buildtime_comparer(buildtime)
    ship_filter = lambda ship: comparer(ship) < tolerance
    filtered_ships = list(filter(ship_filter, ships))
    filtered_ships.sort(key=comparer)
    return filtered_ships

def get_ship_name(ship, lang = "en"):
    return ship['names'][lang]