import discord

def get_discord_colour(colour_name: str):
    if 'blue' in colour_name:
        return discord.Color.blue()
    if 'red' in colour_name:
        return discord.Color.red()
    if 'gold' in colour_name:
        return discord.Color.gold()
    if 'pink' in colour_name:
        return discord.Color.magenta()
    return discord.Color.random()