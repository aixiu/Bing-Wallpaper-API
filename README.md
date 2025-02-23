# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![日出时分的富士山, 河口湖, 日本](https://cn.bing.com/th?id=OHR.MtFujiSunrise_ZH-CN0567499176_1920x1080.webp)
Today: [日出时分的富士山, 河口湖, 日本](https://cn.bing.com/th?id=OHR.MtFujiSunrise_ZH-CN0567499176_1920x1080.webp) - 清晨的美好精致

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
    "date": "2025-02-23",
    "headline": "清晨的美好精致",
    "title": "日出时分的富士山, 河口湖, 日本",
    "description": "在东京西南约 60 英里处，矗立着日本的文化象征之一：富士山。这座日本最高峰海拔近12,000英尺，其近乎完美对称的火山锥，每年约有五个月被积雪覆盖，形成壮丽景观。几个世纪以来，富士山一直被视为神圣之山。在神道信仰中，富士山被奉为本宫浅间大社的圣山，并在其视野范围内建有供奉它的神社。",
    "image_url": "https://cn.bing.com/th?id=OHR.MtFujiSunrise_ZH-CN0567499176_1920x1080.webp",
    "main_text": "富士山是世界上最大的活火山之一，也是富士火山带的一部分。富士火山带是一条火山链，主要从马里亚纳群岛经伊豆群岛和伊豆半岛到本州北部。"
}
```

UpdataTime：2025-02-23 08:28:30
