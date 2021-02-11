# lrc2srt

详细视频制作方案与说明查看：https://git.io/fhSBj

使用注意，制作出srt文件后，用字幕软件打开平移时间轴，最后一条字幕的时间需要手动调整。

以Aegisub为例，窗口-平移时间-时间(开始与结束，开始，结束)，对时间进行调整。

K轴设置positions设置目前写死在main.py里的positions变量里，不同分辨率视频可能要求的位置不同。

然后生成的srt文件在aegisub中套用样式即可。

压制代码如： `ffmpeg -i g.mp4 -vf "ass=result.ass" gg.mp4`

## TODO
- [x] 生成卡拉OK字幕
- [x] 增加qq音乐的歌词文件获取

该repo下三个脚本

## getlrc.py

用于获取歌词文件，保存当前目录test.lrc中

修改其中mid就可以

mid的获取，再网易云中选择分享-复制链接

```
https://music.163.com/song?id=455502443&userid=331603845
//其中id的参数就是程序中的mid
```

使用方法：`python getlrc.py` （需要requests库

api说明：

```
http://get.ftqq.com/7430.get
```

## getlrc_qq.py

适用于qq音乐的歌词获取。用歌曲sid或者分享短链接均可

api说明：

```
https://blog.csdn.net/qq_41979349/article/details/102458551
https://www.cnblogs.com/twilightlemon/p/7076938.html
```

## main.py

用于将当前目录test.lrc文件，转化成result.srt字幕文件格式

使用方法：`python main.py`