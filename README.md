# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![乌尔姆市政厅的天文钟, 德国](https://cn.bing.com/th?id=OHR.UlmClock_ZH-CN9282560066_1920x1080.webp)
Today: [乌尔姆市政厅的天文钟, 德国](https://cn.bing.com/th?id=OHR.UlmClock_ZH-CN9282560066_1920x1080.webp) - 节约日光的艺术

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
    "date": "2026-03-08",
    "headline": "节约日光的艺术",
    "title": "乌尔姆市政厅的天文钟, 德国",
    "description": "每年三月，美国大部分地区开始实行夏令时，时钟拨快以最大限度地利用日光。这一想法可以追溯到1784年，当时本杰明·富兰克林曾幽默地建议人们早起以节省蜡烛的使用。美国在第一次世界大战期间，于1918年正式采用夏令时，作为一项节能措施。经过多年执行不一之后，1966年的《统一时间法案》确立了全国范围内季节性时钟调整的标准。虽然如今大多数州都实行夏令时，但夏威夷州和亚利桑那州（纳瓦霍族保留地除外）不实行，理由是日光变化幅度很小，且出于气候方面的考虑。此外，美国的一些属地全年也保持标准时间。",
    "image_url": "https://cn.bing.com/th?id=OHR.UlmClock_ZH-CN9282560066_1920x1080.webp",
    "main_text": "位于德国乌尔姆市市政厅的天文钟是一座历史悠久的时钟，以其精巧的机械结构和详尽的天文显示而闻名。"
}
```

UpdataTime：2026-03-08 08:45:35
