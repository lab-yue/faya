当前版本: 3.9.0 ♪

环境:

`python3.6`  
`qqbot`  
`itchat` 
`selenium`    
`chrome/phantomJS driver`  
`lxml` 

以下单独运行：

| .py file  | usage   | command  |note | 
| ------------- |:-------------| :-----|:-----|
| qq      | qqbot主文件 | python3 qq.py  ||
| wx      | 微信端主文件 | python3 wx.py  | 转发内容到qq中 |
| line      | line段主文件 | python3 line.py  |需要翻墙 在line上运行 目前使用ngrok代理|
| faya_GUI      | 以简单GUI运行 | python3 faya_GUI.py  ||
| t.sh/t_stream.py      | 获取自己的关注的推特 | sh t.sh/python3 t_stream.py  |需要翻墙 .sh自动重启|




以下可以作为插件

()表示可选择
粗体表示参数

| .py file  | usage   | command  |note | 
| ------------- |:-------------| :-----|:-----|
| aqi    | aqi info      |  aqi (sh/lz/nj)|默认上海 |
| bilibili | 自动获取番剧更新时间并推送     |   follow https://bangumi.bilibili.com/anime/6432  | 面向 bangumi 栏目|
| currency    | 获取汇率      |  xr 1 USD:CNY,JPY,AUD| |
| duilian    | http://ai.binwang.me/couplet/的自动对联      |  对联 今天天气真好|由于网站还在开发并不稳定 |
| express      | 获取快递信息 默认最新3条| 快递 896052528662 |
| mh      | 获取mhxx对应monster肉质 | ?mh イビルジョー  ||
| ox      | 牛津字典api | ?ox apple |需要先注册获取使用key|
| pi_status      | RaspberryPi运行状况 | pi_info | |
| weather      | 获取今日上海天气 | tq | |
| wyy      | 自动收藏歌曲到网易云歌单 | http://music.163.com/#/m/song?id=455502617 |先正则匹配url，再使用selenium操作 速度较慢 需要提前获取登录用cookies |
| yd      | 查询有道字典 | ? apple | 需要先注册获取使用key|
| yd      | 查询有道字典读音 | en/us apple is sweet | 需要先注册获取使用key|
| wiki      | 获取wiki第一段 自动选择语言 | wiki Tokyo 7th シスター | |

以往更新：
[before.md](https://github.com/minatsuki-yui/faya/blob/master/before.md)