#!/usr/bin/python3

import json

class name(object):
    def __init__(self,filename):
        self.dir = 'data/'

        if filename.endswith('.json'):
            self.path = self.dir+filename
        else:
            self.path = self.dir+filename+'.json'

        try:
            with open(self.path ,'r') as data:
                self.data =  json.loads(data.read())
        except:
            self.data = {'0':'0'}

    def get(self):
        if self.data:
            return self.data

    def set(self,data):
        if isinstance(data,dict):
            with open(self.path, 'w') as file:
                json.dump(data,file)

    def get_key(self,key):
        if key in self.data:
            return self.data[key]
    def set_key(self,key,value):
        self.data[key] = value

    def search(self,key,value):
        for each in self.data:
            this = self.data[each]
            if key in this:
                if value == this[key]:
                    return self.data[each]
        return 0

if __name__ == '__main__':
    data = name('wx').search('display','dalao')
    print(data)
