# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![圣马可钟楼，威尼斯，意大利](https://cn.bing.com/th?id=OHR.ItalyClock_ZH-CN0846995743_1920x1080.webp)
Today: [圣马可钟楼，威尼斯，意大利](https://cn.bing.com/th?id=OHR.ItalyClock_ZH-CN0846995743_1920x1080.webp) - 时间的步伐

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
    "date": "2025-03-08",
    "headline": "时间的步伐",
    "title": "圣马可钟楼，威尼斯，意大利",
    "description": "又到了一年中的这个时刻，时钟拨快一小时，虽然少睡了一小时，但换来了更长的傍晚时光。今年的夏令时从今天凌晨2点正式开始，亚利桑那州和夏威夷州除外，这再次提醒我们，时间从不会等待任何人。夏令时的理念很简单：最大化利用自然光，减少能源消耗。这一概念最早在 18 世纪由本杰明·富兰克林提出，尽管他当时 “节省蜡烛”的建议更像是一种讽刺，而非严肃提议。时间快进到 20 世纪初，许多国家在战争期间采用夏令时以节省燃料。美国于 1966 年颁布了《统一时间法案》，正式将夏时令标准化。如今，全球约70个国家实行夏令时，通常从3月持续到11月，让人们享受长达八个月的漫长夜晚。",
    "image_url": "https://cn.bing.com/th?id=OHR.ItalyClock_ZH-CN0846995743_1920x1080.webp",
    "main_text": "2014年6月10日，俄罗斯通过相关法案，决定取消自2011年以来实施的“永久夏令时”，改回冬令时，并不再实行冬夏时制的交替调整。"
}
```

UpdataTime：2025-03-08 16:24:02
