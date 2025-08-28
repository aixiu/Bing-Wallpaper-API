# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![马约尔广场鸟瞰图, 马德里, 西班牙](https://cn.bing.com/th?id=OHR.PlazaMayor_ZH-CN4576498488_1920x1080.webp)
Today: [马约尔广场鸟瞰图, 马德里, 西班牙](https://cn.bing.com/th?id=OHR.PlazaMayor_ZH-CN4576498488_1920x1080.webp) - 网格的心脏

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
    "date": "2025-08-28",
    "headline": "网格的心脏",
    "title": "马约尔广场鸟瞰图, 马德里, 西班牙",
    "description": "从高处俯瞰，马德里（西班牙首都）的马约尔广场（Plaza Mayor）上，整齐的拱廊与瓦片屋顶交织成一幅令人着迷的建筑和谐画卷。这片历史悠久的空间曾是热闹的集市广场“阿拉巴尔广场”（Plaza del Arrabal）的所在地，见证了这座城市数百年来的变迁。这一转变始于1561年，当时皇家法院从托莱多迁至马德里，广场随之归入马德里管辖。受秩序与宏伟愿景的启发，菲利普二世重新构想了这片广场——尽管实际施工直至菲利普三世统治时期的1617年才正式展开。",
    "image_url": "https://cn.bing.com/th?id=OHR.PlazaMayor_ZH-CN4576498488_1920x1080.webp",
    "main_text": "经过一系列火灾后，马约尔广场在历史上曾多次重建。要到达那里，你可以选择其中一个入口，每个入口都别具特色。"
}
```

UpdataTime：2025-08-28 16:33:36
