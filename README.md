# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![科尔多瓦的古罗马桥，西班牙](https://cn.bing.com/th?id=OHR.RomanBridge_ZH-CN4699931052_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [科尔多瓦的古罗马桥，西班牙](https://cn.bing.com/th?id=OHR.RomanBridge_ZH-CN4699931052_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 这座古桥在哪呢？

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
    "date": "2023-04-04",
    "headline": "这座古桥在哪呢？",
    "title": "科尔多瓦的古罗马桥，西班牙",
    "description": "科尔多瓦的古罗马桥跨越瓜达尔基维尔河，是这座城市的一处历史地标。这座桥始建于公元前1世纪罗马帝国的扩张时期，在历史上曾被多次重建，目前这座桥的主体是在8世纪由阿拉伯人重建。虽然它已经承载了数个世纪的交通往来，但现在这座桥仅供行人通行。如果你觉得它很眼熟，可能是因为你曾在《权力的游戏》第五季中见过它，在剧中它是虚构的瓦兰提斯城的一部分。",
    "image_url": "https://cn.bing.com/th?id=OHR.RomanBridge_ZH-CN4699931052_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "这座桥在历史上数次被翻新，现在只有它的第14和15个桥洞是罗马时期的。"
}
```

UpdataTime：2023-04-04 01:43:39
