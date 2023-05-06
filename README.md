# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![大麦和矢车菊, 诺德豪森, 德国](https://cn.bing.com/th?id=OHR.Kornblume_ZH-CN0344238832_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [大麦和矢车菊, 诺德豪森, 德国](https://cn.bing.com/th?id=OHR.Kornblume_ZH-CN0344238832_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 一片花田

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
    "date": "2023-05-06",
    "headline": "一片花田",
    "title": "大麦和矢车菊, 诺德豪森, 德国",
    "description": "春天久盼终至，今天是种花日，让我们在今天种下一株花吧！种花不仅对我们的身心健康都有好处，也有益于地球。度过了漫长、寒冷又沉郁的冬季之后，开启一年中最美丽的季节之一的方式，非种花莫属！",
    "image_url": "https://cn.bing.com/th?id=OHR.Kornblume_ZH-CN0344238832_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "矢车菊经常长在麦田里，所以它的英文名也叫“cornflower”（麦田花）。"
}
```

UpdataTime：2023-05-06 01:36:38
