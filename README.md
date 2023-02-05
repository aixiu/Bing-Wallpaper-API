# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![毛茸茸又可爱的山兔](https://cn.bing.com/th?id=OHR.YearRabbit_ZH-CN2751166096_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [毛茸茸又可爱的山兔](https://cn.bing.com/th?id=OHR.YearRabbit_ZH-CN2751166096_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 兔年元宵节快乐！

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
    "date": "2023-02-05",
    "headline": "兔年元宵节快乐！",
    "title": "毛茸茸又可爱的山兔",
    "description": "正月是农历的元月，古人称“夜”为“宵”，正月十五是一年中第一个月圆之夜，所以称正月十五为“元宵节”。元宵节的形成有一个较长的过程，根源于民间开灯祈福古俗。说到元宵节开灯祈福，就会让人们联想到元宵灯的传统习俗闹花灯和猜灯谜。",
    "image_url": "https://cn.bing.com/th?id=OHR.YearRabbit_ZH-CN2751166096_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "在中国古代，元宵节是一个充满浪漫色彩的节日。元宵节为人们创造了一个传情达意的好机会，也是中国古代的“情人节”。"
}
```

UpdataTime：2023-02-05 01:58:45
