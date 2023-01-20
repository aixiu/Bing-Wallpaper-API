# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![王企鹅，福克兰群岛](https://cn.bing.com/th?id=OHR.FalklandKings_ZH-CN6891102487_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [王企鹅，福克兰群岛](https://cn.bing.com/th?id=OHR.FalklandKings_ZH-CN6891102487_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - “兄弟们，跟我走”

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
    "date": "2023-01-20",
    "headline": "“兄弟们，跟我走”",
    "title": "王企鹅，福克兰群岛",
    "description": "今天是企鹅宣传日，我们展示的照片是一群在福克兰群岛散步的王企鹅。王企鹅的体型在“企鹅界”中排名第二，仅次于它们的表亲——帝企鹅。王企鹅身穿“燕尾服”，让它们看起来如同绅士一般温文尔雅。更为重要的是，这是它们的伪装色。王企鹅潜入海洋寻找食物时，黑色的羽毛可以迷惑天空中的捕食者，同时雪白的腹部又可以迷惑海中的猎物。",
    "image_url": "https://cn.bing.com/th?id=OHR.FalklandKings_ZH-CN6891102487_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "王企鹅不筑巢。它们直接把蛋放在脚上，用肚子盖住蛋，直到孵化。"
}
```

UpdataTime：2023-01-20 01:54:24
