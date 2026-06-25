# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![泰晤士河, 伦敦, 英格兰](https://cn.bing.com/th?id=OHR.ThamesSummer_ZH-CN5292532714_1920x1080.webp)
Today: [泰晤士河, 伦敦, 英格兰](https://cn.bing.com/th?id=OHR.ThamesSummer_ZH-CN5292532714_1920x1080.webp) - 时事

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
    "date": "2026-06-25",
    "headline": "时事",
    "title": "泰晤士河, 伦敦, 英格兰",
    "description": "议会大厦、钟楼和巨型摩天轮有什么共同之处？它们都矗立在泰晤士河畔，仿佛伦敦为了营造戏剧性效果而精心布局了这些标志性建筑。",
    "image_url": "https://cn.bing.com/th?id=OHR.ThamesSummer_ZH-CN5292532714_1920x1080.webp",
    "main_text": "泰晤士河防洪闸于1984年建成，是世界上规模最大的可移动防洪设施之一，用于保护伦敦免受北海风暴潮引发的洪水威胁。"
}
```

UpdataTime：2026-06-25 18:21:36
