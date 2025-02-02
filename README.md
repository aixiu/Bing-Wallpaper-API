# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![年幼的高山土拨鼠](https://cn.bing.com/th?id=OHR.AustriaMarmot_ZH-CN2303743586_1920x1080.webp)
Today: [年幼的高山土拨鼠](https://cn.bing.com/th?id=OHR.AustriaMarmot_ZH-CN2303743586_1920x1080.webp) - 天气预报还是运气预报？

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
    "date": "2025-02-02",
    "headline": "天气预报还是运气预报？",
    "title": "年幼的高山土拨鼠",
    "description": "又迎来了土拨鼠日。今天，美国和加拿大的人们依赖著名土拨鼠潘克苏托尼·菲尔预测冬季是否会持续。菲尔是世界上最著名的土拨鼠。传说2月2日它若从洞穴中出来看到影子，就会返回洞中继续冬眠，意味着冬天将持续六周；若看不到影子，则预示春天将提前到来。德国移民将这一习俗带到美国。1887年，宾夕法尼亚州潘克苏托尼首次举办土拨鼠日庆祝活动。历史上，欧洲人将这一天视为春天的开始。德国人最初通过观察獾和其他小动物的行为，判断农事重要的季节变化迹象。18至19世纪移居宾夕法尼亚的德国人，选择当地土拨鼠担任“天气预报员”的角色。",
    "image_url": "https://cn.bing.com/th?id=OHR.AustriaMarmot_ZH-CN2303743586_1920x1080.webp",
    "main_text": "阿尔卑斯旱獭以友善的性格闻名。旱獭实行一夫一妻制，生活在家庭群体中，通常由一对亲代繁殖雌雄及其后代组成，每个群体包含15至20只个体。幼崽非常活泼，各个年龄段的旱獭都会通过鼻子相碰互相问候。"
}
```

UpdataTime：2025-02-02 08:27:18
