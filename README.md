# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![艾琳多南堡，苏格兰高地](https://cn.bing.com/th?id=OHR.EileanDonanDawn_ZH-CN0383017858_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [艾琳多南堡，苏格兰高地](https://cn.bing.com/th?id=OHR.EileanDonanDawn_ZH-CN0383017858_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 湖滨城堡

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
    "date": "2023-02-08",
    "headline": "湖滨城堡",
    "title": "艾琳多南堡，苏格兰高地",
    "description": "艾琳多南堡坐落在苏格兰三个湖泊的交汇处，其宁静的表面下，是数个世纪的风云动荡。维京人、封建贵族和起义军来来去去，在这个苏格兰西部高地的湖滨城堡里留下了他们的足迹。",
    "image_url": "https://cn.bing.com/th?id=OHR.EileanDonanDawn_ZH-CN0383017858_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "艾琳多南堡（Eilean Donan）的英文名意思是“多南的岛屿”。这个名字来源于埃格的多南（ Donnán of Eigg），一个凯尔特圣徒，于公元617年被杀害。"
}
```

UpdataTime：2023-02-08 01:56:28
