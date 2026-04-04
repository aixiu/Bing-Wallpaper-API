# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![春天的雪钟花](https://cn.bing.com/th?id=OHR.SpringSnowdrops_ZH-CN2933051747_1920x1080.webp)
Today: [春天的雪钟花](https://cn.bing.com/th?id=OHR.SpringSnowdrops_ZH-CN2933051747_1920x1080.webp) - 静静绽放的变化

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
    "date": "2026-04-04",
    "headline": "静静绽放的变化",
    "title": "春天的雪钟花",
    "description": "雪滴花是最早开放的花之一，常常在冬天尚未完全离去时，就从寒冷的土壤中探出身来。它低垂的钟形花朵看起来柔弱，却为早春而生。其细胞中含有特殊的抗冻蛋白，能够帮助植物抵御霜冻，使它们能够适应冬末多变而寒冷的天气。",
    "image_url": "https://cn.bing.com/th?id=OHR.SpringSnowdrops_ZH-CN2933051747_1920x1080.webp",
    "main_text": "痴迷于雪花莲的收藏者被称为“雪花莲爱好者”"
}
```

UpdataTime：2026-04-04 16:49:42
