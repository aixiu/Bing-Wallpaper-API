# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![从国际空间站拍摄的地球](https://cn.bing.com/th?id=OHR.EuropeFromISS_ZH-CN0722816540_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [从国际空间站拍摄的地球](https://cn.bing.com/th?id=OHR.EuropeFromISS_ZH-CN0722816540_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 此景只应天上有

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
    "date": "2023-04-12",
    "headline": "此景只应天上有",
    "title": "从国际空间站拍摄的地球",
    "description": "1961年4月12日，宇航员尤里·加加林成为人类历史上前往太空的第一人，举世震惊。他乘坐“东方太空3KA”号，在两小时之内完成了绕地球一周的飞行。此后不到一个月的时间，水星计划的宇航员艾伦·谢泼德成功飞往太空，成为第一个进入太空的美国人。今天这张照片向我们展示了从国际空间站拍摄的地球，从太空回望地球的风景，依然魅力十足，星光璀璨俨然一副艺术品。每年的4月12日，是纪念加加林的“尤里之夜”，也被称为“世界太空派对”，这一天是全球天文学爱好者的狂欢。",
    "image_url": "https://cn.bing.com/th?id=OHR.EuropeFromISS_ZH-CN0722816540_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "铁元素构成了地球的核心"
}
```

UpdataTime：2023-04-12 01:40:37
