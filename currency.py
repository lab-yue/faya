#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests


def exchange(data):
    # expect format: (xr).(1 USD:CNY,JPY,AUD)

    parts = data.split(' ', 1)

    if len(parts) != 2:
        return '输入例子: xr 1 USD:CNY'
    else:
        try:
            amount = float(parts[0])
        except ValueError:
            return '数字有误'

        try:
            base, symbols = parts[1].split(':', 1)
        except ValueError:
            return '币种输入有误'

        para = f'base={base}&symbols={symbols}'

        alter = {
                "软妹币": 'CNY',
                "美元": 'USD',
                "日元": 'JPY',
                "欧元": 'EUR',
                "英镑": 'GBP',
                "港币": 'HKD',
                "刀": 'USD',
                "人民币": 'CNY',
                "RMB": "CNY",
                "澳元": 'AUD'
            }

        for each in alter:
            if each in para:
                para = para.replace(each, alter[each])

        rp = requests.get(f'http://api.fixer.io/latest?{para}').json()

        if 'rates' not in rp:
            return 'error: Invalid base'
        else:

            update = rp['date']

            rates = rp['rates']

            info = f'update: {update}\n'

            for currency in rates:
                ratio = rates[currency]
                info += f'\n{amount}   {base}  —＞ {round(ratio*amount, 2)}   {currency}'

    return info

if __name__ == "__main__":
    print(exchange('550.5 日元:软妹币,刀'))
