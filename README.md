# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![北卡罗来纳州的南瓜农场, 美国](https://cn.bing.com/th?id=OHR.PumpkinFarm_ZH-CN1232784365_1920x1080.webp)
Today: [北卡罗来纳州的南瓜农场, 美国](https://cn.bing.com/th?id=OHR.PumpkinFarm_ZH-CN1232784365_1920x1080.webp) - 南瓜日，今日登场！

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
    "date": "2025-10-26",
    "headline": "南瓜日，今日登场！",
    "title": "北卡罗来纳州的南瓜农场, 美国",
    "description": "没有什么比一片等待采摘的南瓜田更能代表秋天了。这些圆滚滚的南瓜出现在南瓜派、门廊装饰、拿铁和游行中。美国一些地方更是把对南瓜的喜爱推向极致——伊利诺伊州莫顿镇自称为“世界南瓜之都”，因为其产量高且与罐装南瓜产业联系紧密。新罕布什尔州则紧随其后，将南瓜定为州水果。",
    "image_url": "https://cn.bing.com/th?id=OHR.PumpkinFarm_ZH-CN1232784365_1920x1080.webp",
    "main_text": "2020 年，美国人均南瓜消费量为 6.44 磅。"
}
```

UpdataTime：2025-10-26 02:08:16
