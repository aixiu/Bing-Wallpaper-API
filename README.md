# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![阿姆布鲁大桥，阿姆斯特丹，荷兰](https://cn.bing.com/th?id=OHR.ArmbrugBridge_ZH-CN4600005169_1920x1080.webp)
Today: [阿姆布鲁大桥，阿姆斯特丹，荷兰](https://cn.bing.com/th?id=OHR.ArmbrugBridge_ZH-CN4600005169_1920x1080.webp) - 一次挥动桥臂，连接两岸

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
    "date": "2026-04-03",
    "headline": "一次挥动桥臂，连接两岸",
    "title": "阿姆布鲁大桥，阿姆斯特丹，荷兰",
    "description": "在阿姆斯特丹，有些桥梁只是用来跨越运河，而阿姆布鲁赫桥（Armbrug）则多了一份趣味——当人们经过时，它仿佛在向行人挥手致意。这座桥横跨在旧侧沃堡运河之上。它的名字意为“手臂桥”，但实际上并不是指桥的形状，而是源自附近的一条小巷——Oudezijds Armsteeg（旧侧臂巷）。虽然名字与“手臂”有关，但更像是一种有趣的联想，让人不禁想象它正向经过的骑行者和行人友好地打招呼。",
    "image_url": "https://cn.bing.com/th?id=OHR.ArmbrugBridge_ZH-CN4600005169_1920x1080.webp",
    "main_text": "“Armbrug”这一名称源自该桥的运作机制。这座桥配有长长的升降臂，通过升降桥面来让船只得以穿过运河。"
}
```

UpdataTime：2026-04-03 09:06:35
