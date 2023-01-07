# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![羊毛和马海毛纱线](https://cn.bing.com/th?id=OHR.Mohair_ZH-CN9435762268_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [羊毛和马海毛纱线](https://cn.bing.com/th?id=OHR.Mohair_ZH-CN9435762268_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 纺纱杆到底是什么东西？

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
    "date": "2023-01-07",
    "headline": "纺纱杆到底是什么东西？",
    "title": "羊毛和马海毛纱线",
    "description": "今天的照片展示的是柔软华丽的羊毛和马海毛纱线，因为今天是纺纱杆节（Distaff Day），一个可以追溯到中世纪的节日。但说实话，这个节日或许并不值得庆祝，因为今天是圣诞节后的第13天，过了12天摆脱繁重家务的幸福日子后，女性们要在今天重新开始纺纱工作。",
    "image_url": "https://cn.bing.com/th?id=OHR.Mohair_ZH-CN9435762268_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "乔叟和莎士比亚也用纺纱杆（distaff）这个词指代女性在家庭中所做的工作，类似于中文的“女红”。"
}
```

UpdataTime：2023-01-07 01:48:34
