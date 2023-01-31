# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![南非自然保护区的斑马](https://cn.bing.com/th?id=OHR.ZebraTrio_ZH-CN5902552401_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [南非自然保护区的斑马](https://cn.bing.com/th?id=OHR.ZebraTrio_ZH-CN5902552401_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 斑马快活的一天

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
    "date": "2023-01-31",
    "headline": "斑马快活的一天",
    "title": "南非自然保护区的斑马",
    "description": "设立“斑马日”是为了让全世界关注这个特殊的物种，并采取措施避免它们的灭绝。斑马主要分布在非洲南部和东部。它们全身遍布的独特条纹最为引人注目，这些条纹可以让斑马融入周围的环境，“迷惑”捕食者，同时还能防蚊虫叮咬。刚出生的小斑马身上的条纹是红褐色的，但长大后最终还是会变成黑白条纹。",
    "image_url": "https://cn.bing.com/th?id=OHR.ZebraTrio_ZH-CN5902552401_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "巴切尔热带草原斑马是目前唯一可以合法养殖用于食用的斑马。"
}
```

UpdataTime：2023-01-31 01:56:34
