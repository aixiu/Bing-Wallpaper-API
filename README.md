# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![克罗索尔山谷，斯诺多尼亚国家公园，英国威尔士](https://cn.bing.com/th?id=OHR.BabblingBrook_ZH-CN9371346787_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [克罗索尔山谷，斯诺多尼亚国家公园，英国威尔士](https://cn.bing.com/th?id=OHR.BabblingBrook_ZH-CN9371346787_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 宁静的山谷

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
    "date": "2023-02-23",
    "headline": "宁静的山谷",
    "title": "克罗索尔山谷，斯诺多尼亚国家公园，英国威尔士",
    "description": "今天照片中展示的宁静山谷坐落在北威尔士格的斯诺登尼亚国家公园。克罗伊索（Croesor）峡谷曾经是热闹非凡的采石场，专门生产用于建造屋顶及地板的石板。如今这里没有了采石的喧嚣，只有长满苔藓的石墙、潺潺的溪流、羊群啃过的田野和台阶，还有穿过这里前往莫尔温尼恩（Moelwynion）山脉的徒步者。",
    "image_url": "https://cn.bing.com/th?id=OHR.BabblingBrook_ZH-CN9371346787_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "威尔士被誉为神话传说之地。传说两条古龙曾在威尔士的迪纳斯埃姆里斯山展开一场大战。"
}
```

UpdataTime：2023-02-23 01:53:04
