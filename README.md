# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![从美国宇航局猎户座飞船上看到的月球](https://cn.bing.com/th?id=OHR.MoonDayArtemis_ZH-CN8743374853_1920x1080.webp)
Today: [从美国宇航局猎户座飞船上看到的月球](https://cn.bing.com/th?id=OHR.MoonDayArtemis_ZH-CN8743374853_1920x1080.webp) - 为我们的近邻月球而庆祝

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
    "date": "2023-07-20",
    "headline": "为我们的近邻月球而庆祝",
    "title": "从美国宇航局猎户座飞船上看到的月球",
    "description": "为了纪念1969年7月20日人类首次成功登陆月球，7月20日被定为国际月球日。这个节日不仅让人们回顾我们过去在月球探索上取得的卓越成就，也让人们关注我们如今在月球探索方面的获得的进步。图片上的美国宇航局研制的猎户座飞船正是这种进步的一个实证。这座飞船是为深空探索而设计的，它在2022年执行了一次无人绕月飞行，将在2024年进行一次载人绕月飞行，并计划在2025年载宇航员重返月球。这个节日的意义还在于让大家意识到月球的重要性，并了解人类未来在太空探索和太空殖民方面的潜力。",
    "image_url": "https://cn.bing.com/th?id=OHR.MoonDayArtemis_ZH-CN8743374853_1920x1080.webp",
    "main_text": "人类在地球上只能看到59%的月球表面。"
}
```

UpdataTime：2023-07-20 01:44:21
