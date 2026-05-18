# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![伦敦自然历史博物馆, 英格兰](https://cn.bing.com/th?id=OHR.MuseumLondon_ZH-CN5602977820_1920x1080.webp)
Today: [伦敦自然历史博物馆, 英格兰](https://cn.bing.com/th?id=OHR.MuseumLondon_ZH-CN5602977820_1920x1080.webp) - 大厅里的希望

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
    "date": "2026-05-18",
    "headline": "大厅里的希望",
    "title": "伦敦自然历史博物馆, 英格兰",
    "description": "当你步入博物馆，时光仿佛瞬间流转。一枚化石，诉说着数百万年前生命的印迹；一颗宝石，映照着肉眼难见的沧海桑田。正是这种深切的联结感，构成了“国际博物馆日”——这一由国际博物馆协会于1977年创立的节日——所旨在颂扬的核心精神。",
    "image_url": "https://cn.bing.com/th?id=OHR.MuseumLondon_ZH-CN5602977820_1920x1080.webp",
    "main_text": "国际博物馆日（IMD）是由国际博物馆协会（ICOM）协调举办的国际性节日，于每年5月18日或前后举行。"
}
```

UpdataTime：2026-05-18 04:36:08
