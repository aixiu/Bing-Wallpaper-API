# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![“火流”马尾瀑布，约塞米蒂国家公园，美国加利福尼亚州](https://cn.bing.com/th?id=OHR.FireFallYosemite_ZH-CN3351604820_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [“火流”马尾瀑布，约塞米蒂国家公园，美国加利福尼亚州](https://cn.bing.com/th?id=OHR.FireFallYosemite_ZH-CN3351604820_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 这个悬崖怎么着火了？

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
    "date": "2023-02-16",
    "headline": "这个悬崖怎么着火了？",
    "title": "“火流”马尾瀑布，约塞米蒂国家公园，美国加利福尼亚州",
    "description": "在约塞米蒂国家公园的埃尔卡皮坦山东侧，当所有自然条件齐备，马尾瀑布就像火一样“燃烧”起来。这种现象只有在2月的几周时间里可以看到，前提是天气晴朗，雪水或雨水形成瀑布，并且光照条件恰到好处。“火瀑布”只会持续大约10分钟，届时，观景区会人潮涌动。希望今年的游客能有幸看到这一神奇的自然景观。",
    "image_url": "https://cn.bing.com/th?id=OHR.FireFallYosemite_ZH-CN3351604820_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "火瀑布的形成需要几个要素：下了足量的雪，天气够暖和，雪融化后形成瀑布，天空晴朗无云，阳光照耀的角度正合适，然后瀑布才会“燃烧”。"
}
```

UpdataTime：2023-02-16 01:55:55
