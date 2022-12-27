# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![格林达维克的蓝湖，冰岛](https://cn.bing.com/th?id=OHR.BlueLagoon_ZH-CN3874240119_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [格林达维克的蓝湖，冰岛](https://cn.bing.com/th?id=OHR.BlueLagoon_ZH-CN3874240119_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 治愈身心的“废水”

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
    "date": "2022-12-27",
    "headline": "治愈身心的“废水”",
    "title": "格林达维克的蓝湖，冰岛",
    "description": "实不相瞒，今天这张美丽的照片展示的是一个废水池，其源头是附近一家地热发电厂。虽然这个源头听起来并不诱人，但蓝湖是冰岛最受欢迎的景点之一。关键是不要被废水中的“废”字影响。这里的水很干净，温度常年保持在37.7摄氏度左右，富含（使水呈现蓝色的）二氧化硅以及工厂处理废水过程中产生的硫。人们认为蓝湖里的这些矿物质和藻类对皮肤和身体健康大有益处。",
    "image_url": "https://cn.bing.com/th?id=OHR.BlueLagoon_ZH-CN3874240119_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "冰岛蓝湖上方的天空同湖水一样迷人。北极天空中的北极光会让你目不转睛。"
}
```

UpdataTime：2022-12-27 01:45:48
