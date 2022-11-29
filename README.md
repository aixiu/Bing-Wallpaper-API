# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![罗维尼老城，克罗地亚](https://cn.bing.com/th?id=OHR.RovinjCroatia_ZH-CN5459110500_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [罗维尼老城，克罗地亚](https://cn.bing.com/th?id=OHR.RovinjCroatia_ZH-CN5459110500_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 亚得里亚海边的明珠

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
    "date": "2022-11-29",
    "headline": "亚得里亚海边的明珠",
    "title": "罗维尼老城，克罗地亚",
    "description": "美丽而又历史悠久的罗维尼矗立在亚得里亚海边。圣尤菲米亚教堂200英尺高的钟楼俯瞰着罗维尼老城中心。这座教堂建于18世纪初，也充当着灯塔，照亮镇上渔船回家的路。",
    "image_url": "https://cn.bing.com/th?id=OHR.RovinjCroatia_ZH-CN5459110500_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "伊斯特拉语是一种曾在伊斯特拉地区广泛使用的语言，现在当地仍有一些居民在使用。如今，这座小镇的官方语言是克罗地亚语和意大利语。"
}
```

UpdataTime：2022-11-29 16:56:13
