# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![盛开的樱花树上的红头长尾山雀](https://cn.bing.com/th?id=OHR.BeginningofSpring25Y_ZH-CN7356156800_1920x1080.webp)
Today: [盛开的樱花树上的红头长尾山雀](https://cn.bing.com/th?id=OHR.BeginningofSpring25Y_ZH-CN7356156800_1920x1080.webp) - 春光明媚的日子

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
    "date": "2025-02-03",
    "headline": "春光明媚的日子",
    "title": "盛开的樱花树上的红头长尾山雀",
    "description": "立春到啦，新的四季轮回已经开启。虽然我们已经开始步入了春天，但中国幅员辽阔，南北跨度大，很多地区都是只是刚刚进入春天的前奏阶段。",
    "image_url": "https://cn.bing.com/th?id=OHR.BeginningofSpring25Y_ZH-CN7356156800_1920x1080.webp",
    "main_text": "黑喉丛山雀具有很强的社会性，它们会成群迁徙，最多可有40只鸟。"
}
```

UpdataTime：2025-02-03 01:49:17
