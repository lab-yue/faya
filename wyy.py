#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import requests
import re
from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import db

def love(url, name):
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
         'user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"'
    )

    service_args = ['--load-images=no', '--disk-cache=yes', '--ignore-ssl-errors=true']
    # service_args.append('--load-images=no')  ##关闭图片加载
    # service_args.append('--disk-cache=yes')  ##开启缓存
    # service_args.append('--ignore-ssl-errors=true')

    driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=service_args)

    #driver = webdriver.Chrome() #chrome_options=options

    driver.get("http://music.163.com/")

    driver.delete_all_cookies()

    #input()

    #c = driver.get_cookies()
    #print(c)


    for each in db.name('wyy').get_key('cookies'):
        driver.add_cookie(each)

    # for cookie in c:
    #    cook = {}
    #    for each in ['name', 'value', 'domain', 'path', 'expiry']:
    #        if each in cookie:
    #            cook[each] = cookie[each]
    #    print(cook)
    #    driver.add_cookie(cook)

    # os.chdir('/Users/Cordial/Desktop/')
    # with open ('songurl.txt' ,'r') as l:
    #    songs = l.read().split(',')
    # for song in songs:

    driver.get(url)
    driver.implicitly_wait(3)
    try:
        print('now')
        driver.switch_to.frame('contentFrame')
        WebDriverWait(driver, 5).until(
            ec.presence_of_element_located((By.XPATH, '//*[@id="content-operation"]/a[3]')))
        driver.find_element_by_xpath('//*[@id="content-operation"]/a[3]').click()
        print('click ok')
        #driver.get_screenshot_as_file('/Users/Cordial/Desktop/1.png')
        WebDriverWait(driver, 5).until(ec.presence_of_all_elements_located((By.CLASS_NAME, 'xtag ')))
        pop = driver.find_elements_by_class_name('xtag ')
        pop[2].click()
        WebDriverWait(driver, 5, 0.1).until(ec.presence_of_all_elements_located((By.CLASS_NAME, 'sysmsg')))
        sysmsg = driver.find_element_by_xpath('//div[@class="sysmsg"]/span').text
        time.sleep(2)

        title = driver.title.replace(' - 网易云音乐', '').replace(' - 单曲', '')

        if name == 'master':
            driver.find_element_by_xpath('//*[@id="content-operation"]/a[3]').click()
            print('click ok')
            WebDriverWait(driver, 5, 0.1).until(ec.presence_of_all_elements_located((By.CLASS_NAME, 'xtag ')))
            pop = driver.find_elements_by_class_name('xtag ')
            pop[1].click()
            return f'{title}:\n{sysmsg}'

        driver.close()
        print('finished ' + title)
        return f'{title}:\n{sysmsg}'
    except Exception as e:
        driver.get_screenshot_as_file('1.png')
        info = driver.find_elements_by_xpath('//div[@class="zcnt"]/div/div')
        if len(info):
            return '收藏不了的说...原因:\n'+info[0].text
        else:
            title = driver.title
            return f'收藏{title}失败……,原因:\n{e}'


def give_wyy():

    with open('songinfo.txt', 'r', encoding='utf-8') as bef:
        msgbk = '最近三曲为: '

        last3 = bef.read().split(',')[-3:]

        for song in last3:
            msgbk += '\n\n' + song.split(':')[1]

        return msgbk

def give_wyyurl(s_dex):

    with open('songurl.txt', 'r', encoding='utf-8') as bef:

        last = bef.read().split(',')[-4:]
        print(last)
        return last[s_dex-1]


def save_wyy(msg, nickname):

    url_reg = re.compile(r'(http://music.163.com[^\s]*)')
    wyyurl = re.findall(url_reg, msg)[0].replace('/#','')
    driver = love(wyyurl, nickname)
    #driver.start()
    #driver.join()

    '''

    headers = {
        'Host': 'music.163.com',
        'Referer': 'http://music.163.com/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    tit_re = re.compile('<title>(.+)</title>')
    songinfo = re.findall(tit_re, requests.get(wyyurl , headers = headers).text)
    songinfo = songinfo[0].replace(' - 网易云音乐', '')
        
    '''

    with open('songurl.txt', 'a+', encoding='utf-8') as songurl:
        songurl.write(','+ wyyurl)

    return driver


if __name__ == "__main__":
    #print(give_wyy())
    print(save_wyy('http://music.163.com/#/m/song?id=756137','master'))
    #print(give_wyyurl(1))
