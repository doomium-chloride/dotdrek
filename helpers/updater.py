from .message import message_me
from azurlane.azurapi import AzurAPI

async def update_azurapi(client):
    api = AzurAPI()
    print("Checking for AzurApi updates...")
    need_update = api.updater.checkForNewUpdate()
    if any(need_update):
        print("Updating")
        await message_me(client, "AzurApi updating")
        api.updater.update()
    else:
        print("No update required for Azur Api")