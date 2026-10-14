# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![侏罗纪时期的菊石化石](https://cn.bing.com/th?id=OHR.AmmoniteFossils_ZH-CN5825251327_1920x1080.webp)
Today: [侏罗纪时期的菊石化石](https://cn.bing.com/th?id=OHR.AmmoniteFossils_ZH-CN5825251327_1920x1080.webp) - 穿越时间的螺旋

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
    "date": "2026-10-14",
    "headline": "穿越时间的螺旋",
    "title": "侏罗纪时期的菊石化石",
    "description": "我们如何知道早在人类出现之前地球是什么样子？化石提供了许多线索。国家化石日旨在赞颂古生物学，以及那些帮助科学家重建过去环境、追溯生命演化并了解数百万年前消失生物的发现。从恐龙到微小的海洋生物，这些过去的遗存保存着早已不复存在的远古世界的一个个瞬间。",
    "image_url": "https://cn.bing.com/th?id=OHR.AmmoniteFossils_ZH-CN5825251327_1920x1080.webp",
    "image_url_jpg": "https://cn.bing.com/th?id=OHR.AmmoniteFossils_ZH-CN5825251327_1920x1200.jpg&rf=LaDigue_1920x1200.jpg",
    "image_url_uhd": "https://cn.bing.com/th?id=OHR.AmmoniteFossils_ZH-CN5825251327_UHD.jpg",
    "main_text": "化石不一定非得是骨骼。足迹、洞道、巢穴以及古代生命留下的其他痕迹也可以成为化石。"
}
```

UpdateTime：2026-10-14 12:43:17
