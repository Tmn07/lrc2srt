# lrc2srt

该repo下三类脚本

getlrc_\*\*.py 用于获取QQ音乐或网易云音乐的歌词文件(\*.lrc)

main.py 用于将歌词文件初步处理转化成简易字幕文件(*.srt)

MySelection.lua Aegisub自动化脚本，用于全选奇数或偶数行，仅用于个人做伪K轴时配合使用。

## getlrc_\*\*.py

### 网易云音乐

使用方法：`python getlrc_163.py` 

修改其中mid即可

mid的获取，再网易云中选择分享-复制链接

```
https://music.163.com/song?id=455502443&userid=331603845
//其中id的参数就是程序中的mid
```

### QQ音乐

使用方法：`python getlrc_qq.py` 

修改程序中分享短链接或使用歌曲的sid均可

## main.py

使用方法：`python main.py`

将歌词文件test.lrc初步处理转化成简易字幕文件result.srt

是否制作伪K轴或者保留翻译自行修改变量

```python
K = 1 # 伪K轴，即是否进行奇偶定位
positions = ["{\pos(80,900)}", "{\pos(1840,1024)}"] # 奇偶位置，不同分辨率视频需调整

translate = 0 # 是否保留中文翻译
```

**注：**最后一条字幕的时间可能会有问题

## MySelection.lua

放入Aegisub的automation\autoload目录下则会自动载入，或者手动载入

个人制作伪K轴时，对奇数偶数行采用的对齐方式不同，通过插件选中后批量对奇数偶数行套用不同样式

![image-20210213134208471](.\pic\MySelection.png)

## 参考

[网易云音乐常用API浅析](http://get.ftqq.com/7430.get)

QQ音乐接口相关：

https://blog.csdn.net/qq_41979349/article/details/102458551

https://www.cnblogs.com/twilightlemon/p/7076938.html

## 个人制作流程

1. getlrc.py获取歌词文件
2. main.py根据需求生成srt字幕
3. 使用软件对srt进一步调整（如校准时间轴，调整最后一条字幕的时间，调整奇偶样式，过长的过场前字幕调整）
   - 窗口导航栏-平移时间-时间(开始与结束，开始，结束)，可以对时间进行调整（制作伪K轴时，可能需要提前出现或延迟结束，也可在“平移时间”里做到）
   - 奇偶样式采用不同对齐方式，使用MySelection.lua脚本批量选中，修改样式
   - 之后可以考虑套用automatic kalaoke模板啥的？
4. 保存得到ass文件，进行压制
   - 压制代码如： `ffmpeg -i g.mp4 -vf "ass=result.ass" gg.mp4`
   - 个人视频制作方案与ffmpeg命令说明查看：https://git.io/fhSBj