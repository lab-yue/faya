#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import importlib
function_dict = {}

simple_function_dict = {'aqi'    : 'aqi',
                        'duilian': 'duilian',
                        'exp'    : 'express',
                        '?jp'    : 'jp_dict',
                        '?ox'    : 'ox',
                        'pi_info': 'pi_status',
                        'pixiv'  : 'pixiv_daily',
                        'rss'    : 'rss',
                        'snm'    : 'synonym',
                        'tq'     : 'weather',
                        }


def get(func_name):
    if func_name in function_dict:
        return function_dict[func_name].get


for _ in simple_function_dict:
    f = simple_function_dict[_]
    function_dict[_] = importlib.import_module('lib.simple.' + f)

if __name__ == '__main__':
    print(get('tq')())
