# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![一群抹香鲸, 印度洋](https://cn.bing.com/th?id=OHR.EndangeredWhales_ZH-CN4053106967_1920x1080.webp)
Today: [一群抹香鲸, 印度洋](https://cn.bing.com/th?id=OHR.EndangeredWhales_ZH-CN4053106967_1920x1080.webp) - 鲸鱼，你会救我吗？

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
    "date": "2026-05-14",
    "headline": "鲸鱼，你会救我吗？",
    "title": "一群抹香鲸, 印度洋",
    "description": "集智慧、力量与惊人的深潜本领于一身——抹香鲸绝不满足于浅层的生存。在这个“濒危物种日”，让我们一同认识这位胸怀大志、潜得更深的海洋巨兽。",
    "image_url": "https://cn.bing.com/th?id=OHR.EndangeredWhales_ZH-CN4053106967_1920x1080.webp",
    "main_text": "“Cachalot”一词常用于指代抹香鲸，源自一个古法语词汇，意为“大牙齿”。"
}
```

UpdataTime：2026-05-14 18:04:31
