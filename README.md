# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![穆涅略斯自然保护区，西班牙](https://cn.bing.com/th?id=OHR.SessileOaks_ZH-CN6385464274_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [穆涅略斯自然保护区，西班牙](https://cn.bing.com/th?id=OHR.SessileOaks_ZH-CN6385464274_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 树木之美

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
    "date": "2023-01-17",
    "headline": "树木之美",
    "title": "穆涅略斯自然保护区，西班牙",
    "description": "穆涅略斯自然保护区有西班牙保护最好的栎树森林之一。栎树也被称作普通橡树、欧洲橡木或英国橡树。除橡树外，这片面积13560英亩的保护区内还有无梗花栎。",
    "image_url": "https://cn.bing.com/th?id=OHR.SessileOaks_ZH-CN6385464274_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "穆涅略斯自然保护区内有崇山峻岭也有低地山谷，河流就在各种地形之间起伏流淌。"
}
```

UpdataTime：2023-01-17 01:50:14
