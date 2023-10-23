# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![塞勒斯堡的玉米迷宫，宾夕法尼亚州，美国](https://cn.bing.com/th?id=OHR.PoconosMaze_ZH-CN4696904367_1920x1080.webp)
Today: [塞勒斯堡的玉米迷宫，宾夕法尼亚州，美国](https://cn.bing.com/th?id=OHR.PoconosMaze_ZH-CN4696904367_1920x1080.webp) - “迷”人之境

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
    "date": "2023-10-23",
    "headline": "“迷”人之境",
    "title": "塞勒斯堡的玉米迷宫，宾夕法尼亚州，美国",
    "description": "宾夕法尼亚州波科诺斯地区的迷宫是体验美国乡村风情的绝佳选择，这里的秋季活动给游客提供了令人窒息的挑战。迷宫占地11英亩，每年都会推出新颖独特的迷宫设计，使其成为9月和10月的热门景点。",
    "image_url": "https://cn.bing.com/th?id=OHR.PoconosMaze_ZH-CN4696904367_1920x1080.webp",
    "main_text": "塞勒斯堡是美洲黑熊、灰狐和红狐等野生动物的家园。"
}
```

UpdataTime：2023-10-23 01:28:07
