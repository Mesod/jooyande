# https://www.hackerearth.com/practice/notes/samarthbhargav/a-design-pattern-for-configuration-management-in-python/
# loaded config 
import yaml
import os

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../../config.yaml")
with open(path, 'r') as ymlfile:
    conf = yaml.load(ymlfile)


class Config(object):
    def __init__(self):
        self._config = conf # set it to conf

    def get_property(self, property_name):
        if property_name not in self._config.keys(): # we don't want KeyError
            return None  # just return None if not found
        return self._config[property_name]

class TelegramConfig(Config):

    @property
    def api_id(self):
        return self.get_property('telegram_api')['id']

    @property
    def api_hash(self):
        return self.get_property('telegram_api')['hash']