# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![泰晤士河，伦敦，英国](https://cn.bing.com/th?id=OHR.ThamesLondon_ZH-CN3629717426_1920x1080.webp)
Today: [泰晤士河，伦敦，英国](https://cn.bing.com/th?id=OHR.ThamesLondon_ZH-CN3629717426_1920x1080.webp) - 小船轻轻划过泰晤士河

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
    "date": "2024-09-01",
    "headline": "小船轻轻划过泰晤士河",
    "title": "泰晤士河，伦敦，英国",
    "description": "欢迎来到英国伦敦的泰晤士河节。每年，它都会将社区、艺术家和自然爱好者聚集在一起，向河流致敬，为期一个月。2024年的重点活动包括一年一度的帆船赛舟会、大河赛和清洁泰晤士河挑战赛。",
    "image_url": "https://cn.bing.com/th?id=OHR.ThamesLondon_ZH-CN3629717426_1920x1080.webp",
    "main_text": "潮道是英国泰晤士河的一部分，受潮汐影响，这段水域位于特丁顿船闸的下游。"
}
```

UpdataTime：2024-09-01 02:00:48
