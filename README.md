# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![从洞穴中探出头的土拨鼠](https://cn.bing.com/th?id=OHR.AlpineMarmot_ZH-CN3818584615_1920x1080.webp)
Today: [从洞穴中探出头的土拨鼠](https://cn.bing.com/th?id=OHR.AlpineMarmot_ZH-CN3818584615_1920x1080.webp) - 菲尔会看到它的影子吗?

## 接口

接口地址：

```html
https://aixiu.github.io/Bing-Wallpaper-API/
```

请求方式：

```html
https://aixiu.github.io/Bing-Wallpaper-API/<year>/<month>/<day>.json
```

参数说明

| 参数 | 类型 | 说明 |
| - | - | - |
| year | str | 4位年份, 例如：2022 |
| month | str | 2位月份, 例如：02、12 |
| day | str | 2位日期, 例如：02、25 |

例如

[https://aixiu.github.io/Bing-Wallpaper-API/2022/11/01.json](https://aixiu.github.io/Bing-Wallpaper-API/2022/11/01.json)

返回数据

```json
{
    "date": "2024-02-02",
    "headline": "菲尔会看到它的影子吗?",
    "title": "从洞穴中探出头的土拨鼠",
    "description": "想知道今年冬天会持续多久吗？迷信的人可以从土拨鼠日的预报中得到启示，也就是根据土拨鼠是否能看到自己的影子来判断。2月2日，宾夕法尼亚州的普苏塔尼是“核心圈子俱乐部”的舞台，该俱乐部由一群当地政要组成，他们按照传统将一只名叫“普苏塔尼菲尔”的土拨鼠从一个人造树桩中抱出来。然后，俱乐部主席会与这只矮胖的土拨鼠进行交谈，了解菲尔的占卜结果。结果是什么？看到影子表明冬季还会持续六周；如果没看到，那么春天就会提早来临。预测完成后，戴礼帽的人就会向观众宣读，而观众则会为菲尔欢呼。菲尔的亲戚，也就是今天图片里的阿尔卑斯旱獭，它也有自己的过冬传统，那就是储备食物，为漫长的冬眠做准备。但愿菲尔不会看到自己的影子，这样我们就可以走出寒冬的阴影了。",
    "image_url": "https://cn.bing.com/th?id=OHR.AlpineMarmot_ZH-CN3818584615_1920x1080.webp",
    "main_text": "土拨鼠日最早是由德国移民于1887年在美国设立的，其灵感来自欧洲的烛光节。"
}
```

UpdataTime：2024-02-02 01:21:11
