# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![大帕拉迪索国家公园，意大利](https://cn.bing.com/th?id=OHR.GranParadiso100th_ZH-CN5744961532_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [大帕拉迪索国家公园，意大利](https://cn.bing.com/th?id=OHR.GranParadiso100th_ZH-CN5744961532_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 意大利最古老的国家公园

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
    "date": "2022-12-14",
    "headline": "意大利最古老的国家公园",
    "title": "大帕拉迪索国家公园，意大利",
    "description": "大帕拉迪索国家公园是意大利的一座国家公园，位于格雷晏阿尔卑斯山脉，以公园里的大帕拉迪索山命名，毗邻法国瓦诺伊塞国家公园。",
    "image_url": "https://cn.bing.com/th?id=OHR.GranParadiso100th_ZH-CN5744961532_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "这个公园所在地原本是为了保护阿尔卑斯野山羊，避免它们被偷猎，因为这里曾经是国王维克托·伊曼纽尔二世的私人狩猎场。但现在，这里保护着许多物种。"
}
```

UpdataTime：2022-12-14 01:55:22
