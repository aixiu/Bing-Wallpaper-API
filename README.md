# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![蝴蝶正在黄花上授粉](https://cn.bing.com/th?id=OHR.BFPollin_ZH-CN7654067396_1920x1080.webp)
Today: [蝴蝶正在黄花上授粉](https://cn.bing.com/th?id=OHR.BFPollin_ZH-CN7654067396_1920x1080.webp) - 花粉与翅膀相遇

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
    "date": "2026-06-24",
    "headline": "花粉与翅膀相遇",
    "title": "蝴蝶正在黄花上授粉",
    "description": "放大观察维持大地生机的微小交易：一只蝴蝶停在黄色的花朵上，吮吸着花蜜。它吸食花蜜的同时，花粉沾满了它的身体，搭上了前往下一朵花的“顺风车”——这是开花植物悄无声息的繁殖方式之一。传粉者并非只有蜜蜂。蝴蝶、鸟类、蝙蝠、甲虫以及许多其他昆虫都在帮助传播花粉，从而支持野生植物以及我们食用的许多水果和蔬菜的生长。",
    "image_url": "https://cn.bing.com/th?id=OHR.BFPollin_ZH-CN7654067396_1920x1080.webp",
    "main_text": "我们所吃的食物中，大约有三分之一要归功于授粉昆虫。"
}
```

UpdataTime：2026-06-24 11:12:46
