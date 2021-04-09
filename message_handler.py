from commands.base_command  import BaseCommand
from FuzzySearchPy          import FuzzySearch

# This, in addition to tweaking __all__ on commands/__init__.py, 
# imports all classes inside the commands package.
from commands import *
import commands

import settings

# Register all available commands
COMMAND_HANDLERS = {c.__name__.lower(): c()
                    for c in BaseCommand.__subclasses__()}

# Command list

COMMAND_LIST = []

for key, value in COMMAND_HANDLERS.items():
    if not value.secret:
        command_dict = {"name": key, "command": value}
        COMMAND_LIST.append(command_dict)

# Register alias
booty = commands.ass.Ass()
booty.description = "**.drek booty**: Drek's booty."
COMMAND_HANDLERS["booty"] = booty
COMMAND_LIST.append({"name": "booty", "command": booty})

###############################################################################


async def handle_command(command, args, message, bot_client):
    # Check whether the command is supported, stop silently if it's not
    # (to prevent unnecesary spam if our bot shares the same command prefix 
    # with some other bot)
    options = { "sort": True, "caseSensitive": False }
    searcher = FuzzySearch(COMMAND_LIST, ["name"], options)

    if command not in COMMAND_HANDLERS:
        approx = searcher.search(command)
        if approx == None or len(approx) <= 0:
            await COMMAND_HANDLERS['commands'].handle([], message, bot_client)
            return
        else:
            command = approx[0]["name"];
            await message.channel.send(message.author.mention + " Did you mean: {0}".format(command))


    print(f"{message.author.name}: {settings.COMMAND_PREFIX}{command} " 
          + " ".join(args))

    # Retrieve the command
    cmd_obj = COMMAND_HANDLERS[command]
    if cmd_obj.params and len(args) < len(cmd_obj.params):
        await message.channel.send(message.author.mention + " Insufficient parameters!")
    else:
        await cmd_obj.handle(args, message, bot_client)
