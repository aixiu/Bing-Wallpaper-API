# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![马赛马拉的一头狮子，肯尼亚](https://cn.bing.com/th?id=OHR.WorldLionDay_ZH-CN0525835107_1920x1080.webp)
Today: [马赛马拉的一头狮子，肯尼亚](https://cn.bing.com/th?id=OHR.WorldLionDay_ZH-CN0525835107_1920x1080.webp) - 丛林之王？还真不是

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
    "date": "2023-08-10",
    "headline": "丛林之王？还真不是",
    "title": "马赛马拉的一头狮子，肯尼亚",
    "description": "狮子被称作“丛林之王”，但是在今天，也就是世界狮子日，我们得纠正这个说法：狮子其实并不生活在丛林中。狮子是草原和平原的王者，是凶猛的猎手。当它们没有狩猎时，这些威武的生物又会显露出相当有欺骗性的可爱一面来。它们会小憩、打闹、互相梳理毛发，然后下一秒又会突然去追逐羚羊，甚至是河马。就像是1994年的经典电影《狮子王》的片头曲里面唱的，这就是生命的循环。",
    "image_url": "https://cn.bing.com/th?id=OHR.WorldLionDay_ZH-CN0525835107_1920x1080.webp",
    "main_text": "狮子是唯一一种群居的猫科动物，不过也有一些狮子会选择独居。"
}
```

UpdataTime：2023-08-10 01:43:03
