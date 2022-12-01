# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![江泽民逝世](https://cn.bing.com/th?id=OHR.QingmingCandle2020_ZH-CN6775701680_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [江泽民逝世](https://cn.bing.com/th?id=OHR.QingmingCandle2020_ZH-CN6775701680_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 江泽民逝世

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
    "date": "2022-12-01",
    "headline": "江泽民逝世",
    "title": "江泽民逝世",
    "description": "2022年11月30日，江泽民在上海逝世。",
    "image_url": "https://cn.bing.com/th?id=OHR.QingmingCandle2020_ZH-CN6775701680_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "江泽民逝世"
}
```

UpdataTime：2022-12-01 01:57:56
