# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![雪地里的大熊猫宝宝，中国](https://cn.bing.com/th?id=OHR.PandaSnow_ZH-CN5981854301_1920x1080.webp)
Today: [雪地里的大熊猫宝宝，中国](https://cn.bing.com/th?id=OHR.PandaSnow_ZH-CN5981854301_1920x1080.webp) - 回归黑白世界

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
    "date": "2025-03-16",
    "headline": "回归黑白世界",
    "title": "雪地里的大熊猫宝宝，中国",
    "description": "让我们一起庆祝大自然最毛茸茸的珍宝之一：大熊猫。这些标志性的黑白色熊原产于中国，不仅仅因可爱而闻名。它们在竹林生态系统中发挥着关键作用，通过传播种子和促进植被生长，造福无数动植物。",
    "image_url": "https://cn.bing.com/th?id=OHR.PandaSnow_ZH-CN5981854301_1920x1080.webp",
    "main_text": "熊猫每天要花14个小时咀嚼竹子，一天最多可吃83磅！它们独特的“第六指”实则是手掌前端增大的手腕部骨骼，帮助它们更轻松地抓握竹子。"
}
```

UpdataTime：2025-03-16 08:29:00
