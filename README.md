# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![上海的樱花，中国](https://cn.bing.com/th?id=OHR.ShanghaiBlossoms_ZH-CN5594677517_1920x1080.webp)
Today: [上海的樱花，中国](https://cn.bing.com/th?id=OHR.ShanghaiBlossoms_ZH-CN5594677517_1920x1080.webp) - 花香满径

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
    "date": "2024-03-28",
    "headline": "花香满径",
    "title": "上海的樱花，中国",
    "description": "春天，大自然展现出勃勃生机，樱花盛开标志着一个季节的开始。在全球范围内，从日本到美国，这一奇观吸引了数百万人的目光。在中国，樱花从3月下旬开到4月下旬，粉色和白色的樱花点缀着一幅幅美景。这些脆弱的花瓣在中国人的传统中有着深远的意义，象征着新生、希望和生命的短暂。中国有很多赏樱地点，包括武汉的东湖樱花公园、上海的顾村公园和鲁迅公园，以及北京的玉渊潭公园。樱花看起来与梅花相似，但区分两者的一个简单方法是看它们的花瓣。樱花的花瓣末端有分叉，而梅花没有。",
    "image_url": "https://cn.bing.com/th?id=OHR.ShanghaiBlossoms_ZH-CN5594677517_1920x1080.webp",
    "main_text": "全球变暖可能影响樱花树的花期。"
}
```

UpdataTime：2024-03-28 01:21:06
