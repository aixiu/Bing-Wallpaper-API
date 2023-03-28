# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![意大利三峰山上空的银河](https://cn.bing.com/th?id=OHR.MWDolomites_ZH-CN2886991396_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [意大利三峰山上空的银河](https://cn.bing.com/th?id=OHR.MWDolomites_ZH-CN2886991396_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 这些蔚为壮观的山峰在何处？

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
    "date": "2023-03-28",
    "headline": "这些蔚为壮观的山峰在何处？",
    "title": "意大利三峰山上空的银河",
    "description": "这三座位于意大利多洛米蒂山脉的山峰被称为三峰山。这片群山是阿尔卑斯山最著名的景点之一，世界各地的游客都来这里徒步旅行。你可以从各个角度欣赏壮丽的山峰，到了夏天，你还能看到漫山的野花。如果你想在月光下徒步或露营，一定要提前计划，为5小时的行程准备充足的水和零食。2009年，三峰山和整个多洛米蒂山脉一起被联合国教科文组织列为世界遗产。",
    "image_url": "https://cn.bing.com/th?id=OHR.MWDolomites_ZH-CN2886991396_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "阿尔卑斯山脉繁花似锦，像风铃草、火绒草和龙胆草等植物都在这里茁壮生长。"
}
```

UpdataTime：2023-03-28 01:46:07
