# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![斯卡吉特谷地郁金香花田, 华盛顿, 美国](https://cn.bing.com/th?id=OHR.SkagitTulips_ZH-CN4234324174_1920x1080.webp)
Today: [斯卡吉特谷地郁金香花田, 华盛顿, 美国](https://cn.bing.com/th?id=OHR.SkagitTulips_ZH-CN4234324174_1920x1080.webp) - 花瓣巡游

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
    "date": "2026-04-16",
    "headline": "花瓣巡游",
    "title": "斯卡吉特谷地郁金香花田, 华盛顿, 美国",
    "description": "每年春天，华盛顿州的斯卡吉特山谷都会变成一片色彩斑斓的花海，斯卡吉特山谷郁金香节在此欢庆花季的到来。整个四月，游客们可以漫步于郁金香花园和农田，欣赏成排盛开的郁金香，远眺群山美景。",
    "image_url": "https://cn.bing.com/th?id=OHR.SkagitTulips_ZH-CN4234324174_1920x1080.webp",
    "main_text": "郁金香谷农场占地15 英亩，种植着130种花卉，其中包括100多种郁金香。"
}
```

UpdataTime：2026-04-16 03:40:44
