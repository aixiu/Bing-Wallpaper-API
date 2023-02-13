# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![阿卡切斯瞭望台，月亮谷，智利](https://cn.bing.com/th?id=OHR.MoonValley_ZH-CN1906470869_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [阿卡切斯瞭望台，月亮谷，智利](https://cn.bing.com/th?id=OHR.MoonValley_ZH-CN1906470869_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 带我飞向月球

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
    "date": "2023-02-13",
    "headline": "带我飞向月球",
    "title": "阿卡切斯瞭望台，月亮谷，智利",
    "description": "月亮谷位于智利北部的阿塔卡马沙漠，有着令人惊叹的美景。1982年，月亮谷被列为自然保护区，这是因为它拥有极吸引人的、未受破坏的原生环境和奇特的月球地形。关于月亮谷还有一个有趣的知识，那就是这片沙漠已经很多年未下过一滴雨了。",
    "image_url": "https://cn.bing.com/th?id=OHR.MoonValley_ZH-CN1906470869_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "月亮谷的地形干燥恶劣，于是科学家们在那里测试了一辆火星探测器的原型。"
}
```

UpdataTime：2023-02-13 01:56:30
