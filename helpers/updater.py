from .message import message_me

async def update_azurapi(client):
    api = AzurAPI()
    print("Checking for AzurApi updates...")
    need_update = api.updater.checkForNewUpdate()
    if any(need_update):
        print("Updating")
        api.updater.update()
        await message_me(client, "AzurApi updated")
    else:
        print("No update required for Azur Api")