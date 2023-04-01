# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![爪哇树蛙](https://cn.bing.com/th?id=OHR.FrogMonth_ZH-CN3874143397_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [爪哇树蛙](https://cn.bing.com/th?id=OHR.FrogMonth_ZH-CN3874143397_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 一只青翠碧绿的蛙

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
    "date": "2023-04-01",
    "headline": "一只青翠碧绿的蛙",
    "title": "爪哇树蛙",
    "description": "青蛙月开始于每年的4月1日。作为食物链的关键一环，青蛙是一种很重要的生物，它们擅长捕食蚊虫、苍蝇、蜘蛛，甚至老鼠，可以帮助控制害虫的数量。",
    "image_url": "https://cn.bing.com/th?id=OHR.FrogMonth_ZH-CN3874143397_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "爪哇树蛙一种很特别的树蛙，它们生活在印度尼西亚爪哇岛。"
}
```

UpdataTime：2023-04-01 01:42:11
