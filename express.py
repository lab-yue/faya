import requests


def get_express(postID):
    s = requests.session()
    s.keep_alive = False
    # stamp = int(time.time() * 1000)

    headers1 = {
        'Cookie': 'WWWID=WWWE7ECB978614DFC929D09B6F26021ABA5; Hm_lvt_22ea01af58ba2be0fec7c11b25e88e6c=1519385140,1519385152; Hm_lpvt_22ea01af58ba2be0fec7c11b25e88e6c=1519385152',
        'Origin': 'https://www.kuaidi100.com', 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01', 'Referer': 'https://www.kuaidi100.com/',
        'X-Requested-With': 'XMLHttpRequest', 'Connection': 'keep-alive', 'Content-Length': '0'}

    headers2 = {
        'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01', 'Referer': 'https://www.kuaidi100.com/',
        'X-Requested-With': 'XMLHttpRequest', 'Connection': 'keep-alive'}

    cookies = {
        'Hm_lvt_39418dcb8e053c84230016438f4ac86c': '0',
        'Hm_lpvt_39418dcb8e053c84230016438f4ac86c': '-1'
    }

    data1 = requests.get(f'https://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text={postID}', headers=headers1,
                         cookies=cookies).json()
    postData = data1.get('auto', '')
    if postData:
        postType = postData[0]['comCode']
    else:
        return '未知公司'

    link = f'https://www.kuaidi100.com/query?type={postType}&postid={postID}&temp=0.7876708998623851'
    raw = s.get(link, headers=headers2, cookies=cookies).json()
    data2 = raw.get('data', '')

    if not data2:
        return '运单号错了或者暂无数据(´-ω-`)'

    msg = ''

    for port in data2[:3]:
        msg = '时间: ' + port['time'] + '\n信息: ' + port['context'] + '\n' + msg
    msg = f'{postType}运输 最近更新:\n' + msg
    return msg


if __name__ == '__main__':
    print(get_express('63030200378012'))
