# FuckFif

修改fif口语的成绩  

## 使用方法
1. 使用IE浏览器，Fiddler（或者是其他抓包软件）
2. 打开fif官网https://www.fifedu.com/iplat/indexm?nextpage=bp/index
3. 找到“教师任务”，并打开
4. 点击话筒🎙图标，当读到最后一段的时候，打开Fiddler，开启截断
5. 如图找到jsonobject，将jsonobject复制到python中，获得新的jsonobject。
6. 将新的jsonobject重新拷贝到Fiddler中，点击"Run to Completion"。
7. 刷新fif的网站，即可看到自己的成绩。