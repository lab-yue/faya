import yaml
import os


class Config(object):

    __slots__ = ['master_qq_name',
                 'group_name',
                 'my_members_nick',
                 'group_qq',
                 'pvt_key',
                 'pub_key',
                 'line',
                 'master_qq',
                 'my_members',
                 'nick_dict',
                 'ox',
                 'twitter',
                 'ver',
                 'wx',
                 'yd',
                 'server']

    def __init__(self):

        script_dir = os.path.dirname(__file__)
        rel_path = "../faya.yml"
        abs_config_path = os.path.join(script_dir, rel_path)

        with open(abs_config_path, 'r') as yml:
            conf = yaml.load(yml)

        for each in conf:
            if conf[each]:
                self.__setattr__(each, conf[each])

config = Config()

if __name__ == '__main__':
    print(config.my_members)
