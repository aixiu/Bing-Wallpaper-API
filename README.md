# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![火星（© NASA/Alamy）](https://cn.bing.com/th?id=OHR.RedPlanetDay_ZH-CN4913018041_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [火星（© NASA/Alamy）](https://cn.bing.com/th?id=OHR.RedPlanetDay_ZH-CN4913018041_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 太阳系的第四颗行星

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
    "date": "2022-11-27",
    "headline": "太阳系的第四颗行星",
    "title": "火星（© NASA/Alamy）",
    "description": "火星距离地球约1.4亿英里，围绕着太阳运行，这颗行星也被称为红色星球，是继水星、金星及地球之后距离太阳第四近的行星。几百年来的研究和探索，使得我们对火星的了解仅次于地球。近年来，随着好奇号和毅力号探测器相继在2012年、2021年成功登陆火星，我们对火星的认识更加深入。每年的11月28号是火星节，让我们在今天庆祝探索火星取得的成就吧。",
    "image_url": "https://cn.bing.com/th?id=OHR.RedPlanetDay_ZH-CN4913018041_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "火星以罗马神话中的战神玛尔斯命名。"
}
```

UpdataTime：2022-11-27 16:55:09
