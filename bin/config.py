# coding: utf-8
# config

import configparser
config = configparser.ConfigParser()

class Config:
    def __init__(self, route):
        self.route = route

    def read(self, section, option):
        config.read(self.route, encoding='utf-8')
        config_res = config.get(section, option)
        return config_res

    def set(self, section, option, value):
        config.read(self.route, encoding='utf-8')
        config.set(section, option, value)
        config.write(open(self.route, mode='w'))


if __name__ == '__main__':
    config_obj = Config(r"..\conf\lang\lang.ini")
    config_obj.set('default', 'default_lang', 'english')
    res = config_obj.read("default", "default_lang")
    print(res)
