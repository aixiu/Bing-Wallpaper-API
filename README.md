# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![向日葵](https://cn.bing.com/th?id=OHR.HelianthusAnnuus_ZH-CN1675762555_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [向日葵](https://cn.bing.com/th?id=OHR.HelianthusAnnuus_ZH-CN1675762555_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 自然、艺术和数学

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
    "date": "2022-11-22",
    "headline": "自然、艺术和数学",
    "title": "向日葵",
    "description": "向日葵原产于美洲，是一种引人注目的开花植物。一年中，无论什么时候，它都向着天空生长，愉快地歌颂着夏日。事实上，它的花头由许多极小的花朵组成，而这些花朵最终会成熟、变成种子。但是你知道吗？向日葵上也蕴含着大自然的数学奇迹。",
    "image_url": "https://cn.bing.com/th?id=OHR.HelianthusAnnuus_ZH-CN1675762555_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "在斐波纳契数列中，两个连续数字的比值十分接近黄金分割率。"
}
```

UpdataTime：2022-11-22 23:52:03
