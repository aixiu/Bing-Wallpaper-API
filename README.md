# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![蕨类植物的卷曲嫩叶](https://cn.bing.com/th?id=OHR.FibonacciFern_ZH-CN3882237848_1920x1080.webp)
Today: [蕨类植物的卷曲嫩叶](https://cn.bing.com/th?id=OHR.FibonacciFern_ZH-CN3882237848_1920x1080.webp) - 自然中的几何之美

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
    "date": "2026-11-22",
    "headline": "自然中的几何之美",
    "title": "蕨类植物的卷曲嫩叶",
    "description": "今天的图片展示了一片蕨类嫩叶的顶端逐渐卷曲的样子，呼应着自然界随处可见的几何图案。在数学中，斐波那契数列也遵循类似的递进规律：每个数都是前两个数之和，即0、1、1、2、3、5、8，依此类推。今天是斐波那契日；选定这一天，是因为日期11/23中的数字与这一数列相呼应，以此向它致敬。图中的蕨类嫩叶终将随着生长而舒展开来，而在植物世界的其他地方，这一数列还会不断出现在向日葵花盘、松果、多肉植物和菠萝的螺旋排列中。",
    "image_url": "https://cn.bing.com/th?id=OHR.FibonacciFern_ZH-CN3882237848_1920x1080.webp",
    "image_url_jpg": "https://cn.bing.com/th?id=OHR.FibonacciFern_ZH-CN3882237848_1920x1200.jpg&rf=LaDigue_1920x1200.jpg",
    "image_url_uhd": "https://cn.bing.com/th?id=OHR.FibonacciFern_ZH-CN3882237848_UHD.jpg",
    "main_text": "斐波那契数列因一道关于兔子繁殖的13世纪数学题而广为人知。"
}
```

UpdateTime：2026-11-23 00:10:44
