# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![庆祝春节的龙形灯笼，中国西安](https://cn.bing.com/th?id=OHR.ChineseNewYearEveY26_ZH-CN7770318975_1920x1080.webp)
Today: [庆祝春节的龙形灯笼，中国西安](https://cn.bing.com/th?id=OHR.ChineseNewYearEveY26_ZH-CN7770318975_1920x1080.webp) - 祝除夕团圆，新年顺遂！

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
    "date": "2026-02-16",
    "headline": "祝除夕团圆，新年顺遂！",
    "title": "庆祝春节的龙形灯笼，中国西安",
    "description": "除夕夜，街头的龙形灯笼正蜿蜒舒展，金鳞流转间仿佛蓄着时光的温度；而远处隐约响起的蹄声，恰似春风捎来骏马的问候——这是龙与马的相逢，是古老祥瑞与崭新朝气在岁月门楣的相会。",
    "image_url": "https://cn.bing.com/th?id=OHR.ChineseNewYearEveY26_ZH-CN7770318975_1920x1080.webp",
    "main_text": "“龙马精神”是一个富有深厚文化意蕴的中文成语，其核心含义是形容人像龙和马一样，拥有昂扬抖擞、健旺非凡的精神面貌和奋发向上的生命力。"
}
```

UpdataTime：2026-02-16 03:14:29
