# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![中国传统节日端午节](https://cn.bing.com/th?id=OHR.DragonBoatFestival2023_ZH-CN5255671687_1920x1080.webp)
Today: [中国传统节日端午节](https://cn.bing.com/th?id=OHR.DragonBoatFestival2023_ZH-CN5255671687_1920x1080.webp) - 仲夏端午

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
    "date": "2023-06-22",
    "headline": "仲夏端午",
    "title": "中国传统节日端午节",
    "description": "端午节的起源涵盖了古老星象文化、龙图腾祭祀、人文哲学等方面的内容，蕴含着深邃丰厚的文化内涵，在传承发展中杂糅了多种民俗为一体，各地因地域文化不同而又存在着习俗内容或细节上的差异。",
    "image_url": "https://cn.bing.com/th?id=OHR.DragonBoatFestival2023_ZH-CN5255671687_1920x1080.webp",
    "main_text": "2009年9月，端午节成为中国第一个入选世界非物质文化遗产的节日。"
}
```

UpdataTime：2023-06-22 01:53:51
