这里只是过去日志部分，关于Faya转到这里：[关于Faya](https://minatsuki-yui.github.io/2017/06/11/Faya_Project/)

{% note info %} 

目前功能：  

1. 实时获取bilibili番剧的最新的url 
2. 查询上海天气 
2. 查询城市空气质量  
3. 整点报时  
4. 简单学习能力  
5. 通过消息控制Faya下线  
6. 保存分享的网易云链接，并提示上三首  
7. 禁言wt
8. 查询功能列表  
9. 根据预设回复<del>复读</del>部分信息
10. 有道字典
11. 牛津字典
12. <del>google距离</del>
13. key-value简单记录
14. 计时器
15. 今天事件
16. 随机推荐项目
15. 返回字符串长度
16. faya print bksxds
17. 日语字典
18. 预计时间
19. <del>evernote</del>
20. roll吃啥
21. <del>hexo命令</del>
22. <del>基于osascript的mac通知</del>
23. memo功能
24. <del>电脑锁屏功能</del>
25. mh肉质查询
25. 模糊匹配
26. 传递RPi信息

{% endnote %}



{% note default %} 

更新日志：

17.7.10

1. 接入查询RPi信息的查询
2. 通过爬虫恢复日语字典

17.7.8

1. 将整个项目移动至raspberry的linux上运行
2. 重构、整理代码
2. 删除与mac相关的命令
3. 通过字典映射执行函数

17.7.7

1. 通过pyqt制作了简单的离线桌面版本、
2. 更新了bilibili的7月新番查询

17.7.3

1. 添加了怪物猎人mhxx全肉质查询的功能

17.6.23

1. 增加了收发微信的功能

17.6.13

1. 修复了大师球的bug 
2. 添加了memo功能
3. 添加了电脑锁屏功能
4. 去除了部分复杂的回复

17.6.12

1.添加了大师球功能

17.6.11

1. Faya运行超过一个月了www
2. 添加了创建hexo部分

17.6.7

1. 添加了pixiv生成md的部分，可惜webqq消息不支持接受\<script>  \</script>标签，暂停使用

17.6.3

1. 通过饿了么获取了近200家松江大学城附近餐饮信息，通过随机数roll取

17.5.31

1. 通过applescript接入了日语字典
2. 加入了evernote的添加功能

17.5.29

1. 加入计时器的today和pause功能

17.5.28

1. 加入了查询google距离时间功能

17.5.27

1. 添加了计时器
2. 添加了faya print bksxds

17.5.26

1. 添加 mark.key 查询所有的key
2. 重新加入faya.help

17.5.25

1. 添加mark功能

17.5.23

1. 添加少部分同义语
2. 由于协议更改产生了while 1 循环bksxds的bug。更新项目后作出调整，不再识别自己的消息，20秒内不再重复同样消息。
3. 加入牛津字典模块

17.5.22

1. 大幅度修改网易云音乐的反馈，只返回曲名。分文件储存

17.5.19

2. 添加了字典查询功能

17.5.17

2. 更改了报时时间

17.5.16

2. 更新了qqbot版本


17.5.15 

2. 更新了qqbot版本
3. 修改了部分代码
  

17.5.14  

2. 添加预设消息回复预设
3. 添加查询上海天气功能


17.5.13  

1. 重构回复逻辑整体，通过读取外部json加载回复预设
2. 添加预设消息回复预设
3. 添加查询城市空气质量功能
4. 添加简单学习功能
5. 添加了整点报时功能
6. 饥饿度关系

17.5.12  

1. 涉嫌“发送不良信息”进入保护模式
4. 添加预设消息回复预设
5. 添加禁言功能
6. 添加通过消息控制Faya下线  
6. 修改实时获取bilibili番剧的最新的url功能


17.5.11  

1. 被封号，给予「Faya-01」代号以示纪念。
2. 更换开源项目基础
3. 重构回复代码
2. 添加预设消息回复预设
3. 添加统计饥饿度关系
4. 添加实时获取bilibili番剧的最新的url功能
4. 添加识别消息发送者能力
5. <del>添加复读功能</del>


17.5.10  

Faya上线，初始功能：

1. 保存分享的网易云链接，并提示上三首  
2. 根据预设回复部分信息 
3. 基于某smartqq开源项目