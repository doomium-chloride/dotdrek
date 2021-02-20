from events.base_event      import BaseEvent
from helpers                import message, updater


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
        await updater.update_azurapi(client)

