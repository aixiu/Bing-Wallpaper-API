# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![波尔多葡萄园的日出，法国](https://cn.bing.com/th?id=OHR.MarathonMedoc_ZH-CN6649798028_1920x1080.webp)
Today: [波尔多葡萄园的日出，法国](https://cn.bing.com/th?id=OHR.MarathonMedoc_ZH-CN6649798028_1920x1080.webp) - 历史、自然和美酒交汇之地

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
    "date": "2023-09-11",
    "headline": "历史、自然和美酒交汇之地",
    "title": "波尔多葡萄园的日出，法国",
    "description": "在波尔多地区，幅员辽阔的梅多克葡萄园盛产优质葡萄酒。九月是葡萄的丰收季，玛歌、波雅克、圣朱利安、圣埃斯特夫等知名产区都保留着古老的酿酒传统。",
    "image_url": "https://cn.bing.com/th?id=OHR.MarathonMedoc_ZH-CN6649798028_1920x1080.webp",
    "main_text": "梅多克值得一游，在这里，你可以了解法国葡萄酒的酿造历史，参观宏伟的著名酒庄，品尝顶级的葡萄美酒。"
}
```

UpdataTime：2023-09-11 01:22:04
