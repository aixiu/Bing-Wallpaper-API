# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![望远镜下的月球表面照片](https://cn.bing.com/th?id=OHR.BigMoon_ZH-CN2508603883_1920x1080.webp)
Today: [望远镜下的月球表面照片](https://cn.bing.com/th?id=OHR.BigMoon_ZH-CN2508603883_1920x1080.webp) - 在月光下起舞

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
    "date": "2025-07-19",
    "headline": "在月光下起舞",
    "title": "望远镜下的月球表面照片",
    "description": "每年7月20日是国家月球日，纪念1969年尼尔·阿姆斯特朗首次踏上月球这一具有历史意义的时刻。他的那句宣言：“这是我个人的一小步，却是人类的一大步”，也随之载入史册。紧随其后的是巴兹·奥尔德林，成为第二位登上月球的人。",
    "image_url": "https://cn.bing.com/th?id=OHR.BigMoon_ZH-CN2508603883_1920x1080.webp",
    "main_text": "月球也会发生地震，这类震动被称为“月震”。部分月震可能在月球表面形成裂缝，导致气体逸出。对当年的阿波罗宇航员而言，那无疑是一片既陌生又神秘的着陆景观。"
}
```

UpdataTime：2025-07-19 16:34:31
