# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![瓜纳阿卡维韦斯半岛国家公园的红树林，古巴](https://cn.bing.com/th?id=OHR.RedMangrove_ZH-CN4083989028_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [瓜纳阿卡维韦斯半岛国家公园的红树林，古巴](https://cn.bing.com/th?id=OHR.RedMangrove_ZH-CN4083989028_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 向伟大的红树林致敬！

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
    "date": "2023-01-27",
    "headline": "向伟大的红树林致敬！",
    "title": "瓜纳阿卡维韦斯半岛国家公园的红树林，古巴",
    "description": "今天照片里的是古巴的瓜纳阿卡维韦斯半岛国家公园的红树林幼苗。红树林特别适合在淡盐水或盐水中生长，它们不仅能够保护海岸线，而且还是热带沿海生态系统的重要组成部分。这些顽强的树木可以承受巨浪和狂风，还能抵御海上风暴和海水侵蚀的破坏性影响。",
    "image_url": "https://cn.bing.com/th?id=OHR.RedMangrove_ZH-CN4083989028_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "红树林面临着一些自然威胁，例如霜冻和飓风。但红树林的减少大部分是人为造成的。"
}
```

UpdataTime：2023-01-27 01:53:08
