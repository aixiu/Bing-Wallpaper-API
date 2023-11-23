# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![泰德国家公园的日落，特内里费岛，加那利群岛, 西班牙](https://cn.bing.com/th?id=OHR.TeideNational_ZH-CN1367200520_1920x1080.webp)
Today: [泰德国家公园的日落，特内里费岛，加那利群岛, 西班牙](https://cn.bing.com/th?id=OHR.TeideNational_ZH-CN1367200520_1920x1080.webp) - 从深海到天空

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
    "date": "2023-11-23",
    "headline": "从深海到天空",
    "title": "泰德国家公园的日落，特内里费岛，加那利群岛, 西班牙",
    "description": "雄伟的泰德峰海拔3718米，耸立在加那利群岛上。这座火山从海底隆起的高度达到了惊人的7500米，因此它既是西班牙最高的山峰，也是世界上海拔第三高的火山。",
    "image_url": "https://cn.bing.com/th?id=OHR.TeideNational_ZH-CN1367200520_1920x1080.webp",
    "main_text": "泰德火山拥有世界上最大的锥形阴影。"
}
```

UpdataTime：2023-11-23 01:31:45
