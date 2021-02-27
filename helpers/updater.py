from .message import message_me
from azurlane.azurapi import AzurAPI

async def update_azurapi(client, forced=False):
    api = AzurAPI()
    print("Checking for AzurApi updates...")
    need_update = api.updater.checkForNewUpdate()
    if any(need_update):
        update_msg = "AzurApi updating from: {0}".format(api.getVersion())
        print("Updating", update_msg)
        if forced:
            await message_me(client, update_msg)
        api.updater.update()
    else:
        print("No update required for Azur Api")
        if forced:
            await message_me(client, "No update required for Azur Api")