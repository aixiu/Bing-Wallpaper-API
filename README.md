# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![盛开的野蒜，海尼希国家公园，德国](https://cn.bing.com/th?id=OHR.WildGarlic_ZH-CN1869796625_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [盛开的野蒜，海尼希国家公园，德国](https://cn.bing.com/th?id=OHR.WildGarlic_ZH-CN1869796625_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 你见过大蒜开花吗？

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
    "date": "2023-03-24",
    "headline": "你见过大蒜开花吗？",
    "title": "盛开的野蒜，海尼希国家公园，德国",
    "description": "这些清新质朴的白花是野蒜花。在德国图林根州的海尼希国家公园，你可以近距离地欣赏这些野蒜花。海尼希国家公园创建于1997年，旨在保护这里古老的、郁郁葱葱的山毛榉森林。",
    "image_url": "https://cn.bing.com/th?id=OHR.WildGarlic_ZH-CN1869796625_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "大蒜被认为具有丰富的药用价值，是一种非常受欢迎的食疗食材。"
}
```

UpdataTime：2023-03-24 01:43:00
