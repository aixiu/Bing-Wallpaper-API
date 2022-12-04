# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![乞力马扎罗山附近的大象，安波塞利国家公园，肯尼亚](https://cn.bing.com/th?id=OHR.KilimanjaroElephants_ZH-CN3779609103_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [乞力马扎罗山附近的大象，安波塞利国家公园，肯尼亚](https://cn.bing.com/th?id=OHR.KilimanjaroElephants_ZH-CN3779609103_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 象群在路上

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
    "date": "2022-12-04",
    "headline": "象群在路上",
    "title": "乞力马扎罗山附近的大象，安波塞利国家公园，肯尼亚",
    "description": "今天是世界野生动物保护日，让我们和象群们一起散散步。照片里这些非洲象正缓步穿过肯尼亚安波塞利国家公园的大草原，远处是乞力马扎罗山。由于栖息地丧失和偷猎，非洲象数量锐减。",
    "image_url": "https://cn.bing.com/th?id=OHR.KilimanjaroElephants_ZH-CN3779609103_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "乞力马扎罗山的冰川和冰原在不断缩小，预计将在2025年至2035年之间完全消失。这一直是科学研究的重点对象。"
}
```

UpdataTime：2022-12-04 04:05:55
