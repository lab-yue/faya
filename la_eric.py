import requests
import enc
from Fconf import fconf

def get(para):
    pvt = bytes(fconf.pvt_key.encode('utf-8')).decode('unicode-escape')

    #print(pvt)
    info = requests.get(f'{fconf.server}/{para}',headers={'who':'36e2800799c104411ff58543a0b9ac44'}).json()
    cip = enc.Cipher()
    aes_key = cip.key_decrypt(pvt,info['key'])
    return cip.decrypt(aes_key,info['content'])

if __name__ == '__main__':
    print(get('?key=日本'))