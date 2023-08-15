# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![四月九日广场，陶尔米纳，西西里岛，意大利](https://cn.bing.com/th?id=OHR.TaorminaSquare_ZH-CN0273325652_1920x1080.webp)
Today: [四月九日广场，陶尔米纳，西西里岛，意大利](https://cn.bing.com/th?id=OHR.TaorminaSquare_ZH-CN0273325652_1920x1080.webp) - 发光的矩形广场

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
    "date": "2023-08-15",
    "headline": "发光的矩形广场",
    "title": "四月九日广场，陶尔米纳，西西里岛，意大利",
    "description": "陶尔米纳，一颗镶嵌在西西里岛上的美丽明珠，毗邻古希腊殖民地纳克索斯，被爱奥尼亚海和风景如画的伊索拉贝拉岛所环绕。自19世纪以来，这个美丽的小镇一直是旅游胜地。",
    "image_url": "https://cn.bing.com/th?id=OHR.TaorminaSquare_ZH-CN0273325652_1920x1080.webp",
    "main_text": "陶尔米纳会在夏季组织许多展览和活动，古剧场经常举办戏剧演出或古典音乐会，电影银丝带奖颁奖典礼等文化盛会也会在此举行。"
}
```

UpdataTime：2023-08-15 01:19:09
