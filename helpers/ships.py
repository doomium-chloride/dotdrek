from azurlane.azurapi import AzurAPI
from .parse_time import time_str_to_minutes
from FuzzySearchPy import FuzzySearch
import difflib

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
    if pool.startswith("l"):
        return "light"
    if pool.startswith("h"):
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


def get_ships_with_buildtime(buildtime, tolerance, pool=None):
    api = AzurAPI()
    ships = ships_by_construction_pool(api.getAllShips(), pool)
    comparer = make_buildtime_comparer(buildtime)
    ship_filter = lambda ship: comparer(ship) < tolerance
    filtered_ships = list(filter(ship_filter, ships))
    filtered_ships.sort(key=comparer)
    return filtered_ships


def get_ship_name(ship, lang="en"):
    return ship['names'][lang]


def get_all_ship_names():
    api = AzurAPI()
    ships = api.getAllShips()
    names = []
    for ship in ships:
        ship_names = ship['names'].items()
        for key, name in ship_names:
            names.append(name.lower())
    return names


def get_closest_matching_ship(name: str):
    api = AzurAPI()
    try:
        return api.getShip(filter_name(name))
    except:
        matches = find_ship(name)
        if len(matches) < 1:
            return None
        else:
            return matches[0]


def filter_name(name):
    name = name.lower()

    if name == "fdg":
        return "Friedrich der Große"
    if name == "kgv":
        return "King George V"
    if name == 'kasumi':
        return "10063"

    return name


def approximate_ship_name(name, names):
    matches = difflib.get_close_matches(name.lower(), names, n=1, cutoff=0.1);

    if len(matches) < 1:
        return None
    else:
        return matches[0]


def find_ship(name):
    api = AzurAPI()
    ships = api.getAllShips()
    keys = ["names.code", "names.en", "names.jp", "names.cn", "names.kr"]
    options = {"sort": True, "caseSensitive": False}
    searcher = FuzzySearch(ships, keys, options)
    return searcher.search(name)


def ship_by_skill_name(skill_name):
    api = AzurAPI()
    ships = api.getAllShips()
    keys = ["skills.names.en", "skills.names.jp", "skills.names.cn", "skills.names.kr"]
    options = {"sort": True, "caseSensitive": False}
    searcher = FuzzySearch(ships, keys, options)
    return searcher.search(skill_name)


def find_skills(skill_name):
    api = AzurAPI()
    ships = api.getAllShips()
    skills = []
    for ship in ships:
        for skill in ship["skills"]:
            skills.append(skill)
    options = {"sort": True, "caseSensitive": False}
    keys = ["names.en", "names.jp", "names.cn", "names.kr"]
    searcher = FuzzySearch(skills, keys, options)
    return searcher.search(skill_name)


def get_closest_matching_skill(skill_name, exclude_aoa=True):
    skills = find_skills(skill_name)
    if exclude_aoa:
        skills = [skill for skill in skills if not skill["names"]["en"].startswith("All Out Assault")]
    if len(skills) <= 0:
        return None
    return skills[0]


def dumb_search_ship_by_skill(skill_name):
    api = AzurAPI()
    ships = api.getAllShips()
    results = []
    for ship in ships:
        for skill in ship["skills"]:
            if skill["names"]["en"] == skill_name:
                results.append(ship)
    return results
