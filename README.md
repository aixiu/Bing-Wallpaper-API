# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![英格兰湖区的Black Fell](https://cn.bing.com/th?id=OHR.BlackFell_ZH-CN9224189688_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [英格兰湖区的Black Fell](https://cn.bing.com/th?id=OHR.BlackFell_ZH-CN9224189688_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - “群山拥有抚慰和治愈的力量”

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
    "date": "2023-01-06",
    "headline": "“群山拥有抚慰和治愈的力量”",
    "title": "英格兰湖区的Black Fell",
    "description": "今天照片中展示的美丽风景是位于英格兰湖区的黑山（Black Fell），“fell”一词源于古挪威语中的“山”，主要是指地势高且贫瘠的地区，而英格兰湖区的土地通常是未经开垦、用于放牧的。黑山（Black Fell）海拔约1000英尺，被评为英格兰湖区的最佳观景区。站在山顶上，无论望向哪个方向，你都能欣赏到美景。",
    "image_url": "https://cn.bing.com/th?id=OHR.BlackFell_ZH-CN9224189688_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "黑山（Black Fell）以南有一片区域被称为塔恩豪斯（Tarn Hows），由詹姆斯·马歇尔于19世纪60年代开发设计。这是湖区最受欢迎的景点之一。"
}
```

UpdataTime：2023-01-06 01:54:34
