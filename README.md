# lrc2srt

详细视频制作方案与说明查看：https://git.io/fhSBj

## TODO
- [ ] 生成卡拉OK字幕
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