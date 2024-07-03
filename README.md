# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![猫鼬家族](https://cn.bing.com/th?id=OHR.MeerkatManor_ZH-CN2486051161_1920x1080.webp)
Today: [猫鼬家族](https://cn.bing.com/th?id=OHR.MeerkatManor_ZH-CN2486051161_1920x1080.webp) - 等等，谁在那儿？

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
    "date": "2024-07-03",
    "headline": "等等，谁在那儿？",
    "title": "猫鼬家族",
    "description": "大家一起说，“哈库纳·马塔塔”！今天是“世界猫鼬日”，一个庆祝这些以直立姿势而闻名的可爱动物的节日。但不要被它们的名字所迷惑，猫鼬并不是猫。它们是獴科的小型食肉动物，原产于非洲西南部的沙漠和草原。猫鼬是高度社会化的动物，生活在被称为“暴徒”的紧密群体中，最多可由30只个体组成。这些群体通力合作，一起觅食、相互梳理毛发、照看孩子，并轮流担任哨兵，监视捕食者。猫鼬在洞穴中过夜，并躲避中午的炎热——它们喜欢午休。",
    "image_url": "https://cn.bing.com/th?id=OHR.MeerkatManor_ZH-CN2486051161_1920x1080.webp",
    "main_text": "猫鼬因同类暴力致死的比例高达19%，是哺乳动物中占比最高的。"
}
```

UpdataTime：2024-07-03 01:37:29
