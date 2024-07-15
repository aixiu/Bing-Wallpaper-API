# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![立石公园，神奈川县，日本](https://cn.bing.com/th?id=OHR.TateishiPark_ZH-CN9903501398_1920x1080.webp)
Today: [立石公园，神奈川县，日本](https://cn.bing.com/th?id=OHR.TateishiPark_ZH-CN9903501398_1920x1080.webp) - 宁静惬意的海滨风光

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
    "date": "2024-07-15",
    "headline": "宁静惬意的海滨风光",
    "title": "立石公园，神奈川县，日本",
    "description": "今天的图片带我们来到横须贺市的立石公园，在这里可以欣赏相模湾和富士山的壮丽景色，是庆祝海洋日的理想场所。立石公园是一个风景优美的海滨公园，历史上曾激发过艺术家和摄影师的创作灵感。",
    "image_url": "https://cn.bing.com/th?id=OHR.TateishiPark_ZH-CN9903501398_1920x1080.webp",
    "main_text": "该公园以立石海岸线的美丽景色而闻名，远处的富士山能尽收眼底。"
}
```

UpdataTime：2024-07-15 01:42:27
