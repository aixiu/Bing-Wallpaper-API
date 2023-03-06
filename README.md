# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![站在自己领域的冰岛马，冰岛](https://cn.bing.com/th?id=OHR.IcelandHorses_ZH-CN7213041152_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [站在自己领域的冰岛马，冰岛](https://cn.bing.com/th?id=OHR.IcelandHorses_ZH-CN7213041152_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 这些独特的生物是什么?

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
    "date": "2023-03-06",
    "headline": "这些独特的生物是什么?",
    "title": "站在自己领域的冰岛马，冰岛",
    "description": "冰岛马是在冰岛发现的一种小型马，也是地球上血统最纯的马种。这些独特的生物吸引了许多来自世界各地的马术爱好者。为了避免疾病在马匹之间传播，冰岛禁止进口马匹，并且冰岛马一旦出口就不能再回到冰岛。冰岛马的颜色非常丰富，有灰色、黑色、栗色等。它们通常在四岁后才能被骑乘，主要用于展示、竞赛和休闲活动。",
    "image_url": "https://cn.bing.com/th?id=OHR.IcelandHorses_ZH-CN7213041152_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "这是几匹来自北方的马。"
}
```

UpdataTime：2023-03-06 02:00:05
