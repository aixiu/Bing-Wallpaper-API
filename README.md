# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![马赛马拉的角马，肯尼亚](https://cn.bing.com/th?id=OHR.ThreeWildebeest_ZH-CN0175563521_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [马赛马拉的角马，肯尼亚](https://cn.bing.com/th?id=OHR.ThreeWildebeest_ZH-CN0175563521_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 动物王国大迁徙

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
    "date": "2023-05-03",
    "headline": "动物王国大迁徙",
    "title": "马赛马拉的角马，肯尼亚",
    "description": "有很多种野生动物栖息在马赛马拉，包括其最具代表性的居民：角马。角马是非洲的原生物种，包含两个亚种，可以从它们的外形区分二者：黑角马和蓝角马。这些社会性动物经常会形成庞大的种群，数量上千。",
    "image_url": "https://cn.bing.com/th?id=OHR.ThreeWildebeest_ZH-CN0175563521_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "角马会随时聆听其他动物发出的警告，这样它们可以降低被猎杀的风险。"
}
```

UpdataTime：2023-05-03 01:40:50
