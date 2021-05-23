import discord
from FuzzySearchPy import FuzzySearch
from typing import List

search_options = {"sort": True, "caseSensitive": False}


def get_emojis(client, server, emote_names):
    server: discord.Guild = server

    emojis = []
    server_emojis = get_emojis_from_server(server)
    other_emojis = get_all_emojis(client, server)
    server_emoji_searcher = FuzzySearch(server_emojis, ["name"], search_options)
    other_emoji_searcher = FuzzySearch(other_emojis, ["name"], search_options)
    for emote_name in emote_names:
        emoji = None
        if server is not None:
            emoji = discord.utils.get(server.emojis, name=emote_name)
        if emoji is None:
            possible_emojis = server_emoji_searcher.search(emote_name)
            if len(possible_emojis) >= 1:
                emoji = possible_emojis[0]["emoji"]
            else:
                possible_emojis = other_emoji_searcher.search(emote_name)
                if len(possible_emojis) >= 1:
                    print(possible_emojis)
                    emoji = possible_emojis[0]["emoji"]
        if emoji:
            emojis.append(emoji)
    return emojis


def get_all_emojis(client, exclude=None):
    emoji_list = []
    servers: List[discord.Guild] = client.guilds
    for server in servers:
        if exclude is None or server.id != exclude.id:
            emoji_list += list(server.emojis)
    return [{"name": e.name, "emoji": e} for e in emoji_list]


def get_emojis_from_server(server):
    if server is None:
        return []
    server: discord.Guild = server
    return [{"name": e.name, "emoji": e} for e in server.emojis]
