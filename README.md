# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![塞纳河，巴黎，法国](https://cn.bing.com/th?id=OHR.PontdArcole_ZH-CN5348049357_1920x1080.webp)
Today: [塞纳河，巴黎，法国](https://cn.bing.com/th?id=OHR.PontdArcole_ZH-CN5348049357_1920x1080.webp) - 一座承载历史的桥

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
    "date": "2023-05-21",
    "headline": "一座承载历史的桥",
    "title": "塞纳河，巴黎，法国",
    "description": "塞纳河流经法国巴黎，对这座古城的历史有着非比寻常的意义。公元前3世纪，一个名为帕里西人的凯尔特部落决定定居在塞纳河两岸之间的一座岛屿，即如今的西岱岛。在接下来的数个世纪里，塞纳河在巴黎发展成为全球商业和文化中心的过程中发挥了重要作用。",
    "image_url": "https://cn.bing.com/th?id=OHR.PontdArcole_ZH-CN5348049357_1920x1080.webp",
    "main_text": "这条河是许多著名印象派画作的主题，包括莫奈的《拉格勒努耶尔浴池》和雷诺阿的《阿斯涅尔的塞纳河》。"
}
```

UpdataTime：2023-05-21 01:49:13
