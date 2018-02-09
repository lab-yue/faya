# coding: utf8

from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from base64 import b64decode, encodebytes, decodebytes
import hashlib
import random
from Fconf import fconf


class Cipher(object):
    def __init__(self):
        self.mode = AES.MODE_CBC

    def get_aes(self):
        base = self.get_md5(self.get_random())
        self.aes_key = base.encode('utf-8')[0:16]
        # print('aes_key :',self.aes_key)

    def get_rsa(self):
        en_key = RSA.importKey(self.pub64)
        self.rsa_key = en_key.encrypt(self.aes_key, '')[0]
        # print('rsa_key :',self.rsa_key)
        self.rsa_key_str = encodebytes(self.rsa_key).decode('utf-8')
        # print('rsa_key_str: ',self.rsa_key_str)

    def encrypt(self, text):
        self.pub_key = bytes(fconf.pub_key.encode('utf-8')).decode('unicode-escape')
        self.pub64 = b64decode(self.pub_key)
        self.opt = {}
        self.get_aes()
        self.get_rsa()
        encrypter = AES.new(self.aes_key, self.mode, self.aes_key)
        btext = bytes(text.encode('utf-8'))
        print(len(btext))
        if len(btext) % 16 != 0:
            text16 = btext + (16 - len(btext) % 16) * b'\0'
        else:
            text16 = btext

        print(len(text16))
        self.ciphertext = encrypter.encrypt(text16)
        self.opt['key'] = self.rsa_key_str
        self.opt['content'] = encodebytes(self.ciphertext).decode('utf-8')

        return self.opt

    @staticmethod
    def decrypt(key, text):
        cryptor = AES.new(key, AES.MODE_CBC, key)
        plain_text = cryptor.decrypt(decodebytes(text.encode('utf-8'))).decode('utf-8')
        return plain_text.strip('\0').strip()

    @staticmethod
    def get_random():
        return str(random.random())[2:]

    @staticmethod
    def key_decrypt(local_pvt, key):
        pvt_key = RSA.importKey(b64decode(local_pvt))
        bmsg = pvt_key.decrypt(decodebytes(key.encode('utf-8')))
        return bmsg

    @staticmethod
    def get_md5(source):
        md5 = hashlib.md5()
        md5.update(source.encode('utf-8'))
        return md5.hexdigest()

if __name__ == '__main__':
    '''
    pvt = ''
    C = Cipher()
    t = C.encrypt("""
来自 en.wiki
The apple tree ( Malus pumila , commonly and erroneously called Malus domestica ) is a deciduous tree
    """)

    print(t)

    aes_key = C.key_decrypt(pvt, t['key'])
    print('aes_key:', aes_key)
    print(C.decrypt(aes_key, t['content']))
'''
    c = Cipher()
    print(c.get_md5('MUSIC_U=255b19fea4bdec0a0011f855c3708e3e97b229707fccab67d74da902317635b4f866558227e6c3335d9bd72ef1abb9ea77749c2dda21047b').upper())