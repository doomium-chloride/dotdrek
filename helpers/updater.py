from .message import message_me
from azurlane.azurapi import AzurAPI
import os

azurapi_version = "./azurapi_data/version-info.json"

old_message = ""


async def clear_version(client, update_msg):
    global old_message
    try:
        os.remove(azurapi_version)
        if old_message != update_msg:
            await message_me(client, update_msg)
        old_message = update_msg
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
        await message_me(client, "Version couldn't be cleared when updating...")


async def update_azurapi(client, forced=False):

    api = AzurAPI()

    # forced means no checking
    if forced:
        await clear_version(client, "cleared azurapi version")
        api.updater.update(True)
        print("force updated")
        await message_me(client, "force updated")
        return

    # not forced so check first
    # print("Checking for AzurApi updates...")
    # need_update = api.updater.checkForNewUpdate()
    # if any(need_update) or True:
    update_msg = "AzurApi updating from: {0}".format(api.getVersion())
    print("Updating", update_msg)
    await clear_version(client, update_msg)
    api.updater.update(True)
    # else:
    #     print("No update required for Azur Api")
