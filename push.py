import os
import sys
import yaml
import re
from datetime import datetime


class Pusher(object):

    def __init__(self):

        with open('faya.yml', 'r') as yml:
            self.config = yaml.load(yml)

        self.old_ver = self.config['ver']
        self.new_ver = '.'.join(str(int(self.old_ver.replace('.', '')) + 1))

    def push(self):

        print(1)

        self.update_md()
        self.update_yml()

        os.system('git add .')

        info = input('commit: ')

        os.system(f'git commit -m "{info}"')

        yes = input('push? enter y to continue:')

        if yes.lower() == 'y':
            os.system('git push origin master')
        else:
            sys.exit()

        update = datetime.now()
        print('Success.  ' + str(update))
        print('faya ver: %s --> %s' % (self.old_ver, self.new_ver))

    def update_yml(self):

        self.config['ver'] = self.new_ver

        with open('faya.yml', 'w') as yml:
            yaml.dump(self.config, yml, default_flow_style=False)

    def update_md(self):

        ver_reg = re.compile('当前版本:.+?♪')

        with open('README.md', 'r') as md:
            readme = md.read()

        ver_info = '当前版本: '+self.new_ver+' ♪'

        new_readme = re.sub(ver_reg, ver_info, readme)

        with open('README.md', 'w') as md:
            md.write(new_readme)

if __name__ == '__main__':
    pusher = Pusher()
    pusher.push()
