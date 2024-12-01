# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![南极洲的冰山](https://cn.bing.com/th?id=OHR.IcebergsAntarctica_ZH-CN2942178295_1920x1080.webp)
Today: [南极洲的冰山](https://cn.bing.com/th?id=OHR.IcebergsAntarctica_ZH-CN2942178295_1920x1080.webp) - 保护最后一片大荒野

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
    "date": "2024-12-01",
    "headline": "保护最后一片大荒野",
    "title": "南极洲的冰山",
    "description": "今天是南极日，让我们将目光聚焦在世界上最引人注目的国际协定之一的《南极条约》上。该条约于1959年由12个国家签署，将整个南极大陆指定为非军事区，特别注重促进科学研究与合作。这一天彰显了全球合作精神，提醒我们肩负起保护地球上最后一片大荒野的集体责任。",
    "image_url": "https://cn.bing.com/th?id=OHR.IcebergsAntarctica_ZH-CN2942178295_1920x1080.webp",
    "main_text": "南极洲是地球上最寒冷、风力最大、最干燥的大陆。"
}
```

UpdataTime：2024-12-01 02:23:18
