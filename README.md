# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![大广场，布鲁塞尔，比利时](https://cn.bing.com/th?id=OHR.GrandPlaceXmas_ZH-CN8299342316_1920x1080.webp)
Today: [大广场，布鲁塞尔，比利时](https://cn.bing.com/th?id=OHR.GrandPlaceXmas_ZH-CN8299342316_1920x1080.webp) - 令人愉悦的忧郁蓝

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
    "date": "2023-12-16",
    "headline": "令人愉悦的忧郁蓝",
    "title": "大广场，布鲁塞尔，比利时",
    "description": "布鲁塞尔位于比利时的中心地带，作为一座充满活力的首都城市，它将悠久的历史与现代大都市的气息融为一体。布鲁塞尔大广场因其建筑而闻名，并被联合国教科文组织列为世界文化遗产，其华丽的市政厅和拥有百年历史的建筑散发着宏伟的气息。",
    "image_url": "https://cn.bing.com/th?id=OHR.GrandPlaceXmas_ZH-CN8299342316_1920x1080.webp",
    "main_text": "布鲁塞尔大广场经常举办各种节日和文化活动，每隔两年的八月，广场中心会铺设一张巨大的花毯。"
}
```

UpdataTime：2023-12-16 01:30:39
