# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![在北极玩耍的北极熊](https://cn.bing.com/th?id=OHR.PolarBearSwim_ZH-CN1000349057_1920x1080.webp)
Today: [在北极玩耍的北极熊](https://cn.bing.com/th?id=OHR.PolarBearSwim_ZH-CN1000349057_1920x1080.webp) - 过一个冰雪元旦！

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
    "date": "2024-12-31",
    "headline": "过一个冰雪元旦！",
    "title": "在北极玩耍的北极熊",
    "description": "元旦快乐！人类至少从公元前2000年开始庆祝新年，但不同的文化选择了与不同日期，通常与春分或是月相周期相关。公元前153年，罗马人将1月1日定为新年的开始，但在中世纪的欧洲，这一习俗逐渐被冷落。然而，自1582年起随着广泛采用格里高里历（公历），今天成为世界上大部分地区庆祝新年的日子。除了观看烟花、喝香槟和许下新年愿望外，其他全球性的传统还包括了品尝象征幸运的美食和互相赠送礼物。",
    "image_url": "https://cn.bing.com/th?id=OHR.PolarBearSwim_ZH-CN1000349057_1920x1080.webp",
    "main_text": "庆祝新年已经有数千年的历史。最早的新年庆祝活动记录可以追溯到巴比伦时期。"
}
```

UpdataTime：2024-12-31 16:28:33
