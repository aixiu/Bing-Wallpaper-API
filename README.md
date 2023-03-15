# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![阿圭罗村庄，西班牙](https://cn.bing.com/th?id=OHR.AgueroSpain_ZH-CN9622864502_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [阿圭罗村庄，西班牙](https://cn.bing.com/th?id=OHR.AgueroSpain_ZH-CN9622864502_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 如此美景在何处？

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
    "date": "2023-03-15",
    "headline": "如此美景在何处？",
    "title": "阿圭罗村庄，西班牙",
    "description": "美丽的阿圭罗村庄位于西班牙韦斯卡省，它坐落在独特的粉灰色群山之中。村庄背后是被称为里格洛斯岩的悬崖，非常适合拍照。这个拥有130位居民的小村庄还有一座建于12世纪的教堂。如果你是历史爱好者、攀岩爱好者，或二者兼修，那就请把阿圭罗列入旅行目的地清单吧。",
    "image_url": "https://cn.bing.com/th?id=OHR.AgueroSpain_ZH-CN9622864502_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "这个城镇最有趣的地方便是它身后令人惊艳的岩石。"
}
```

UpdataTime：2023-03-15 01:48:26
