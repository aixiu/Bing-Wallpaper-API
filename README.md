# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![冰川国家公园的山羊，美国蒙大拿州](https://cn.bing.com/th?id=OHR.GlacierGoats_ZH-CN0764810245_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [冰川国家公园的山羊，美国蒙大拿州](https://cn.bing.com/th?id=OHR.GlacierGoats_ZH-CN0764810245_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 它们对你也同样好奇

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
    "date": "2022-12-17",
    "headline": "它们对你也同样好奇",
    "title": "冰川国家公园的山羊，美国蒙大拿州",
    "description": "比起美国其它48个州，你更可能在蒙大拿州的冰川国家公园里看到雪羊。雪羊已经习惯人类了，会悠闲地走到游客面前。不过，还是建议你跟它们保持距离，因为雪羊的“铁头功”可不是开玩笑的。",
    "image_url": "https://cn.bing.com/th?id=OHR.GlacierGoats_ZH-CN0764810245_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "雪羊虽然被称为“羊”，但它跟山羊并不同属，反倒是和羚羊、瞪羚和牛的血缘关系更近。"
}
```

UpdataTime：2022-12-17 01:43:48
