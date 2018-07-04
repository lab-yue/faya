import requests
from lxml import html


def get():
    content = []
    headers = {'authority': 'www.nikkei.com',
               'pragma': 'no-cache',
               'cache-control': 'no-cache',
               'upgrade-insecure-requests': '1',
               'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
               'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'referer': 'https://www.nikkei.com/theme/list/',
               'accept-encoding': 'gzip, deflate, br',
               'accept-language': 'zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7'
               }

    response = requests.get('https://www.nikkei.com/access/', headers=headers).text

    dom = html.fromstring(response)
    titles = dom.xpath('//*[@id="CONTENTS_MAIN"]/div[2]/ul/li/h3/span[2]/span[1]/a/text()')
    links = dom.xpath('//*[@id="CONTENTS_MAIN"]/div[2]/ul/li/h3/span[2]/span[1]/a/@href')

    content.append('=======Rank=======\n')

    [content.append(titles[num] + '\n' + 'https://www.nikkei.com/' + links[num] + '\n') for num in range(len(titles))]
    return '\n'.join(content)


if __name__ == '__main__':
    print(get())
