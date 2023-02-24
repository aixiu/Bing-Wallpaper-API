# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![里士满公园的鸳鸯，伦敦，英国](https://cn.bing.com/th?id=OHR.RichmondParkDuck_ZH-CN4956127005_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [里士满公园的鸳鸯，伦敦，英国](https://cn.bing.com/th?id=OHR.RichmondParkDuck_ZH-CN4956127005_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 一只华丽招摇的鸳鸯

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
    "date": "2023-02-24",
    "headline": "一只华丽招摇的鸳鸯",
    "title": "里士满公园的鸳鸯，伦敦，英国",
    "description": "今天照片里的是一只鸳鸯，它正在寒冷沉闷的冬日里展示自己漂亮鲜艳的羽毛。到了换羽季节，雄性鸳鸯会脱去色彩斑斓的羽毛，使得它们的外貌更接近色彩暗淡的雌性鸳鸯，不过它们的喙仍然会是明亮的橙黄色或红色。",
    "image_url": "https://cn.bing.com/th?id=OHR.RichmondParkDuck_ZH-CN4956127005_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "里士满公园修建于17世纪，原本是查理一世的鹿园，现在已成为国家级的自然保护区。"
}
```

UpdataTime：2023-02-24 01:54:07
