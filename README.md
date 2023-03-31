# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![斯太尔河, 奥地利](https://cn.bing.com/th?id=OHR.SteyrRiver_ZH-CN3175702026_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [斯太尔河, 奥地利](https://cn.bing.com/th?id=OHR.SteyrRiver_ZH-CN3175702026_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 大自然的蓝色奇观

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
    "date": "2023-03-31",
    "headline": "大自然的蓝色奇观",
    "title": "斯太尔河, 奥地利",
    "description": "今天这张照片并未经过调色，奥地利斯太尔河的水真的就是这般湛蓝。斯太尔河流经托特斯山脉，当地植被稀少，那为什么斯太尔河还能如此清澈湛蓝？答案就在环绕斯太尔河谷的群山之中。雨水和融化的雪水流入斯太尔河后，其中较重的沉积物沉到水底，而较细的沉积物则会悬浮在水中。被沉积物散射或反射的阳光就赋予了河水这样鲜艳的蓝色。",
    "image_url": "https://cn.bing.com/th?id=OHR.SteyrRiver_ZH-CN3175702026_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "斯太尔河位于下奥地利阿尔卑斯山脉地区，流经斯太尔市附近的格伦堡镇。"
}
```

UpdataTime：2023-03-31 01:44:46
