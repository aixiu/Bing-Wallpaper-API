# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![一品红](https://cn.bing.com/th?id=OHR.PoinsettiaDay_ZH-CN5115071992_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [一品红](https://cn.bing.com/th?id=OHR.PoinsettiaDay_ZH-CN5115071992_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 假日色调

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
    "date": "2022-12-12",
    "headline": "假日色调",
    "title": "一品红",
    "description": "一品红从墨西哥引入美国已经有近200年的历史了。在墨西哥，阿兹特克人曾用一品红的叶子制作染料，用它的汁液治疗发烧。1828年，美国驻墨西哥首任大使乔尔·罗伯茨·波因塞特将这种鲜红色的植物引入美国。到了20世纪60年代，人们培育出了大量更耐寒、更饱满的一品红种类。美国的一品红批发贸易蓬勃发展，每年带来高达2.5亿美元的收入。2002年，每年的12月12日定为“一品红日”。一品红是美国和加拿大最畅销的盆栽植物，每年12月都是节日餐桌上的亮点。",
    "image_url": "https://cn.bing.com/th?id=OHR.PoinsettiaDay_ZH-CN5115071992_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "在被命名为一品红之前，这种植物被称为“墨西哥烈焰花”。"
}
```

UpdataTime：2022-12-12 01:55:07
