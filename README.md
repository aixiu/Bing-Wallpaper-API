# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![与蝴蝶在一起的乌龟](https://cn.bing.com/th?id=OHR.ThreeTurtlesButterflies_ZH-CN7043849571_1920x1080.webp)
Today: [与蝴蝶在一起的乌龟](https://cn.bing.com/th?id=OHR.ThreeTurtlesButterflies_ZH-CN7043849571_1920x1080.webp) - 为龟类喝彩！

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
    "date": "2026-05-23",
    "headline": "为龟类喝彩！",
    "title": "与蝴蝶在一起的乌龟",
    "description": "龟类不仅是引人入胜的生物，更在自然界中扮演着至关重要的角色。海龟有助于维持海草床与珊瑚礁生态系统的健康，而淡水及陆栖龟类则支撑着各自生境的生态平衡。龟壳实际上是其骨架的一部分，由数十块骨头融合而成；此外，部分物种还能够利用地球磁场进行导航，精准地回到它们的出生地。",
    "image_url": "https://cn.bing.com/th?id=OHR.ThreeTurtlesButterflies_ZH-CN7043849571_1920x1080.webp",
    "main_text": "全球共有七种海龟，其中五种正面临灭绝威胁。"
}
```

UpdataTime：2026-05-23 04:03:23
