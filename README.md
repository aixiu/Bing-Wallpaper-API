# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![西部箱龟](https://cn.bing.com/th?id=OHR.WesternBoxTurtle_ZH-CN6203163704_1920x1080.webp)
Today: [西部箱龟](https://cn.bing.com/th?id=OHR.WesternBoxTurtle_ZH-CN6203163704_1920x1080.webp) - 保护我们的乌龟

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
    "date": "2023-05-23",
    "headline": "保护我们的乌龟",
    "title": "西部箱龟",
    "description": "西方箱龟以其壳上的明亮斑纹为特征，可能是最广为人知的龟种之一。 它们的寿命约为 25 年，但最长可达 100 年。 某些海龟物种很可能存在于 1 亿多年前。 虽然海龟和陆龟的寿命比恐龙还长，但超过一半的海龟和陆龟物种现在濒临灭绝。今天是世界海龟日，让我们庆祝这些可爱的生物并思考它们在我们的生态系统中发挥的重要作用。",
    "image_url": "https://cn.bing.com/th?id=OHR.WesternBoxTurtle_ZH-CN6203163704_1920x1080.webp",
    "main_text": "箱龟不会游泳，但它们可以漂浮在水中。"
}
```

UpdataTime：2023-05-23 01:43:56
