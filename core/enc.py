# coding: utf8

import hashlib
import random
from base64 import b64decode, encodebytes, decodebytes

from Crypto.Cipher import AES
from Crypto.PublicKey import RSA

#from core.Fconf import config


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
        self.pub_key = bytes(config.pub_key.encode('utf-8')).decode('unicode-escape')
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

    v = 'IzqXrmlvNeTr0D1XcQPE09xivBGjVlgsAfeZ9Cd2P/qp7owBiKM+2l1rWx3Y0nbQoF8htiUpFP/WMo1qW2Y49pNo5FJ331N2A/3JAsAdNRAiL+YH5zfb2l23pwvQjBLJaB3Iv3DveMsM4aihw4670g=='
    k = '0beb74e4e93fad8c'

    c = Cipher()

    #a = c.decrypt(key=k,text=v)
    import random
    print(c.get_md5('123'))