from jooyande.config import config

def run():
    conf = config.TelegramConfig()
    print(conf.api_hash)