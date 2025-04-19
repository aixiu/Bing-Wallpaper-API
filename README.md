# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![春天里的野生小兔子](https://cn.bing.com/th?id=OHR.BunnyLove_ZH-CN1145897965_1920x1080.webp)
Today: [春天里的野生小兔子](https://cn.bing.com/th?id=OHR.BunnyLove_ZH-CN1145897965_1920x1080.webp) - 复活节兔子要来了

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
    "date": "2025-04-19",
    "headline": "复活节兔子要来了",
    "title": "春天里的野生小兔子",
    "description": "复活节快乐！今天是全世界数十亿基督徒的重要节日，这是一个重生、庆祝与传承传统并存的时刻。复活节，也被称为“逾越节”或“复活主日”，纪念《新约》中所描述的耶稣基督的复活事件。这也是一个充满节日传统的时刻，从日出礼拜到寻找复活节彩蛋活动，当然还有深受大家喜爱的复活节兔子！",
    "image_url": "https://cn.bing.com/th?id=OHR.BunnyLove_ZH-CN1145897965_1920x1080.webp",
    "main_text": "复活节的另一个象征是兔子，因为它繁殖能力强，人们将其视为新生命的创造者。此外，百合花是复活节期间主要使用的花卉。"
}
```

UpdataTime：2025-04-19 16:31:22
