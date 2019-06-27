from jooyande.config import config
from telethon import TelegramClient, events, sync

def run():
    conf = config.TelegramConfig()
    client = TelegramClient('session_name', conf.api_id, conf.api_hash)
    client.start()
    print(client.get_me().stringify())

    client.send_message('username', 'Hello! Talking to you from Telethon')
    client.send_file('username', '/home/myself/Pictures/holidays.jpg')

    client.download_profile_photo('me')
    messages = client.get_messages('username')
    messages[0].download_media()

    @client.on(events.NewMessage(pattern='(?i)hi|hello'))
    async def handler(event):
        await event.respond('Hey!')