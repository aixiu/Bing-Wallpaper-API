# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![秋天池塘里的两只绿头鸭](https://cn.bing.com/th?id=OHR.MallarDucks_ZH-CN7422818269_1920x1080.webp)
Today: [秋天池塘里的两只绿头鸭](https://cn.bing.com/th?id=OHR.MallarDucks_ZH-CN7422818269_1920x1080.webp) - 我所有的小鸭子们

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
    "date": "2023-11-12",
    "headline": "我所有的小鸭子们",
    "title": "秋天池塘里的两只绿头鸭",
    "description": "绿头鸭，又名野鸭，是世界上分布最广的鸭科动物之一。你知道在20世纪以前，绿头鸭在德国曾被称为三月鸭吗？绿头鸭有着醒目的羽毛，很容易辨认。雄性绿头鸭，被称为公鸭，以其彩色的翅膀和绿色的头部而闻名，而母鸭的颜色则是不起眼的棕色。绿头鸭以植物、昆虫和小鱼为食，并且具有很强的适应性。无论是在城市公园，还是湖泊和河流中，你都能见到它们的身影。而正是这种适应性以及色彩斑斓的羽毛，使得绿头鸭成为一种令人瞩目的鸟类。",
    "image_url": "https://cn.bing.com/th?id=OHR.MallarDucks_ZH-CN7422818269_1920x1080.webp",
    "main_text": "你知道绿头鸭在20世纪之前被称为三月鸭吗？"
}
```

UpdataTime：2023-11-12 01:34:04
