#!/usr/bin/python3

import json


class name(object):
    def __init__(self, filename):
        self.__dir = 'data/'

        if filename.endswith('.json'):
            self.__path = self.__dir+filename
        else:
            self.__path = self.__dir+filename+'.json'

        try:
            with open(self.__path, 'r', encoding='utf-8') as dbs:
                self.__data = json.loads(dbs.read())
        except:
            self.__data = {}

    def get(self):
        if self.__data:
            return self.__data

    def set(self, new_data):
        if isinstance(data, dict):
            with open(self.__path, 'w') as file:
                json.dump(new_data, file, ensure_ascii=False)

    def get_key(self, key):
        if key in self.__data:
            return self.__data[key]

    def set_key(self, key, value):
        self.__data[key] = value

    def search(self, key, value):
        for each in self.__data:
            this = self.__data[each]
            if key in this:
                if value == this[key]:
                    return self.__data[each]
        return 0

if __name__ == '__main__':
    data = name('wx').search('display', 'dalao')
    print(data)
