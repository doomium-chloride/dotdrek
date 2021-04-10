import re
import discord

EMOJI_BY_NAME = "{{(.*?)}}"
EMOJI_BY_ID = "/{(.*?)}/"

MAX_DEPTH = 20


def handle_emoji(get_emoji, emoji_list, msg):
    for i in range(MAX_DEPTH):
        match = re.match(EMOJI_BY_ID, msg)
        if match is None:
            break
        str_to_replace = match.group()
        emoji_id = int(match.group(1))
        emoji = get_emoji(emoji_id)
        msg = msg.replace(str_to_replace, str(emoji))
    for i in range(MAX_DEPTH):
        match = re.match(EMOJI_BY_NAME, msg)
        if match is None:
            break
        str_to_replace = match.group()
        emoji_name = match.group(1)
        emoji = discord.utils.get(emoji_list, name=emoji_name)
        if emoji:
            msg = msg.replace(str_to_replace, str(emoji))
        else:
            raise Exception("Get emoji by name failed")

    return msg
