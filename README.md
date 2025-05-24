# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![挪威尤通黑门山国家公园](https://cn.bing.com/th?id=OHR.JotunheimenPark_ZH-CN7417034574_1920x1080.webp)
Today: [挪威尤通黑门山国家公园](https://cn.bing.com/th?id=OHR.JotunheimenPark_ZH-CN7417034574_1920x1080.webp) - 欧洲的野性之美

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
    "date": "2025-05-24",
    "headline": "欧洲的野性之美",
    "title": "挪威尤通黑门山国家公园",
    "description": "今天是“欧洲公园日”，旨在庆祝那些塑造各国自然特性的国家公园和保护区。该纪念日由欧洲公园联盟于1999年创立，以纪念1909年在瑞典建立的九座欧洲最早的国家公园。该节日旨在推动保护自然栖息地、野生动植物及文化遗产的行动，同时鼓励可持续旅游与户外活动。",
    "image_url": "https://cn.bing.com/th?id=OHR.JotunheimenPark_ZH-CN7417034574_1920x1080.webp",
    "main_text": "2020年2月，“冰之秘密”项目的研究人员在挪威南部尤通黑门山脉，因气候变化而逐渐消融的冰川中，发现了一支距今1,500年来自日耳曼铁器时代的维京箭头。"
}
```

UpdataTime：2025-05-24 08:31:12
