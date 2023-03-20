# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![紫番红花](https://cn.bing.com/th?id=OHR.PurpleCrocus_ZH-CN0891528297_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [紫番红花](https://cn.bing.com/th?id=OHR.PurpleCrocus_ZH-CN0891528297_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 春天的色彩

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
    "date": "2023-03-20",
    "headline": "春天的色彩",
    "title": "紫番红花",
    "description": "每年3月20日或3月21日，太阳直射赤道，昼夜等长。在北半球，这一天被称为春分，意味着冬天结束，温暖明媚的春天已经来临，你可能会不经意间在路边发现一朵悄悄盛开的番红花。如同今天的照片，鲜艳美丽的紫番红花正在尽情绽放，它们是每年春天最早绽放的花卉之一。春分是一个北半球的节日。在中国，春分是传统节气之一。在伊朗，春分被称为诺鲁孜节，代表着新的一年开始。不过，在南半球，这一天则意味着秋天开始了，所以给你在阿根廷朋友们寄些毛衣吧。",
    "image_url": "https://cn.bing.com/th?id=OHR.PurpleCrocus_ZH-CN0891528297_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "番红花色彩丰富，有紫色、薰衣草色、蓝色、橙色、黄色、白色等。"
}
```

UpdataTime：2023-03-20 01:51:26
