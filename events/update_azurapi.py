from events.base_event      import BaseEvent
from azurlane.azurapi       import AzurAPI
from helpers                import message


# Your friendly example event
# You can name this class as you like, but make sure to set BaseEvent
# as the parent class
class UpdateAzurApi(BaseEvent):

    def __init__(self):
        interval_minutes = 60  # Set the interval for this event
        super().__init__(interval_minutes)

    # Override the run() method
    # It will be called once every {interval_minutes} minutes
    async def run(self, client):
        api = AzurAPI()
        print("Checking for AzurApi updates...")
        need_update = api.updater.checkForNewUpdate()
        if any(need_update):
            print("Updating")
            api.updater.update()
            message.message_me(client, "AzurApi updated")
        else:
            print("No update required for Azur Api")

