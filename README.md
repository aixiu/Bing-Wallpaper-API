# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![北极熊在加拿大沉睡](https://cn.bing.com/th?id=OHR.PolarBearFrost_ZH-CN5918160947_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [北极熊在加拿大沉睡](https://cn.bing.com/th?id=OHR.PolarBearFrost_ZH-CN5918160947_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 冰冷的北极，温暖的拥抱

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
    "date": "2023-02-27",
    "headline": "冰冷的北极，温暖的拥抱",
    "title": "北极熊在加拿大沉睡",
    "description": "2月27日是国际北极熊日，旨在让人们意识到北极熊因气候变化而面临的巨大威胁。北极熊需要北极的浮冰才能捕食，但北极浮冰正随着地球变暖而减少。虽然北极熊是非常出色的游泳选手，它们甚至因此被归类为海洋哺乳动物，但北极的浮冰仍是它们赖以生存的关键因素。让我们在这一天来认真想想，如何通过可持续的生活方式来帮助北极熊。",
    "image_url": "https://cn.bing.com/th?id=OHR.PolarBearFrost_ZH-CN5918160947_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "北极熊没有领地意识，它们面临冲突时总是小心翼翼，常常选择逃跑而不是战斗。"
}
```

UpdataTime：2023-02-27 01:57:10
