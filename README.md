# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![博罗韦茨，保加利亚](https://cn.bing.com/th?id=OHR.Borovets_ZH-CN5914681811_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [博罗韦茨，保加利亚](https://cn.bing.com/th?id=OHR.Borovets_ZH-CN5914681811_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 冬季仙境

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
    "date": "2022-12-15",
    "headline": "冬季仙境",
    "title": "博罗韦茨，保加利亚",
    "description": "博罗韦茨建于1896年，是保加利亚最古老的冬季度假胜地。相较于阿尔卑斯山其他消费高昂的滑雪胜地，博罗韦茨是欧洲滑雪爱好者们更便宜的选择，不用花大钱就能享受滑雪的乐趣，非常适合滑雪新手。",
    "image_url": "https://cn.bing.com/th?id=OHR.Borovets_ZH-CN5914681811_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "博罗韦茨曾两次主办高山滑雪世界杯（1981年和1984年），这里的冬季两项赛道是世界上最好的赛道之一。"
}
```

UpdataTime：2022-12-15 01:57:13
