# -*- coding: UTF-8 -*-
import hashlib
import random
import re
import click


@click.command()
@click.argument('source')
def md5(source):
    _md5 = hashlib.md5()
    _md5.update(source.encode('utf-8'))
    click.echo(_md5.hexdigest())


@click.command()
@click.argument('data')
def unicodeDecode(data):
    s = data.encode('utf-8')
    click.echo(s.decode('unicode-escape'))


@click.command()
@click.argument('data')
def unicodeEncode(data):
    s = data.encode('unicode-escape')
    click.echo(s.decode('utf-8'))


@click.command()
def roll():
    click.echo(str(random.randint(0, 100)))


@click.command()
def greek():
    l = [chr(x) for x in range(945, 970)]
    click.echo(' '.join(l))


@click.command()
@click.argument('data')
def cal(data):
    cal_reg = re.compile('[\.\+\-\*\(\)\d/]+')
    in_cal = re.findall(cal_reg, data)
    if in_cal:
        if in_cal[0] != data:
            click.echo('输入不合法')
        else:
            try:
                click.echo(f'{data} = ' + str(eval(data)))
            except SyntaxError:
                click.echo('输入算式有误')


if __name__ == '__main__':
    pass
