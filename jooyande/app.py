from jooyande.config import config
from telethon import TelegramClient, events, sync
from tinydb import TinyDB, Query

def run():
    print('bootstraping...')
    db = TinyDB('db.json')

    print('loading config files...')
    conf = config.TelegramConfig()
    channels = config.ChannelsConfig().channels_list
    
    print('connecting to Telegram...')
    with TelegramClient('app_session', conf.api_id, conf.api_hash) as client:
        print('listening started from channels: ', channels)
        
        @client.on(events.NewMessage)
        async def my_event_handler(event):
            sender = await event.get_sender()
            username = sender.username

            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("MESSAGE: ", event.message)
            if username in channels:
                print('new message in channel: ', username)

                # chat = await event.get_chat()
                chat_id = event.chat_id
                sender_id = event.sender_id
                message = event.message
                text = event.raw_text

                db.insert({
                    'text': text,
                    'username': username,
                    'message': message.stringify(),
                    'chat_id': chat_id,
                    'sender_id': sender_id 
                })

                # await event.forward_to('testMonitoringMesod')

        client.run_until_disconnected()
