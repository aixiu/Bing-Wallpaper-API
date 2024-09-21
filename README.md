# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![Oktoberfest in Munich at sunset](https://cn.bing.com/th?id=OHR.MunichBeerfest_ZH-CN0304560562_1920x1080.webp)
Today: [Oktoberfest in Munich at sunset](https://cn.bing.com/th?id=OHR.MunichBeerfest_ZH-CN0304560562_1920x1080.webp) - 为慕尼黑啤酒节干杯！

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
    "date": "2024-09-21",
    "headline": "为慕尼黑啤酒节干杯！",
    "title": "Oktoberfest in Munich at sunset",
    "description": "慕尼黑啤酒节是世界上最大的节日之一，吸引了600多万游客。除了身着传统巴伐利亚服装的服务员端上一大杯泡沫丰富的啤酒之外，每个人都能在这里找到自己喜欢的东西。在这里，您可以享受欢快的音乐、惊险刺激的游乐设施以及令人垂涎欲滴的椒盐卷饼和香肠等当地美食。啤酒节在全球其他地方也有庆祝活动，包括美国的辛辛那提和丹佛等几个城市，每个城市都为节日增添了自己的地方特色。因此，无论您是喜欢啤酒还是喜欢热闹的派对，慕尼黑啤酒节都会让你体验到巴伐利亚的风情。",
    "image_url": "https://cn.bing.com/th?id=OHR.MunichBeerfest_ZH-CN0304560562_1920x1080.webp",
    "main_text": "目前，啤酒节上有14个大帐篷和20个小帐篷。这些帐篷是木制的非永久性建筑，专为啤酒节建造，仅在啤酒节期间使用。"
}
```

UpdataTime：2024-09-21 01:48:22
