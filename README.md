# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![Hong Kong SAR](https://cn.bing.com/th?id=OHR.WorldPopDay_ZH-CN7074706912_1920x1080.webp)
Today: [Hong Kong SAR](https://cn.bing.com/th?id=OHR.WorldPopDay_ZH-CN7074706912_1920x1080.webp) - 万家灯火

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
    "date": "2023-07-11",
    "headline": "万家灯火",
    "title": "Hong Kong SAR",
    "description": "三十六年前的今天，世界迎来了第 50 亿人口。 现在地球人口已经达到 80 亿，而且还在不断增加，这个问题继续存在：我们会用完空间、食物和其他必要的资源吗？ 在今天，我们可以反思地球能够维持多少生命，以及我们个人和集体的生活如何影响我们的地方、国家和全球环境。",
    "image_url": "https://cn.bing.com/th?id=OHR.WorldPopDay_ZH-CN7074706912_1920x1080.webp",
    "main_text": "世界人口增长率在 1965 年至 1970 年间达到顶峰，当时人口平均每年增长 2.1%。"
}
```

UpdataTime：2023-07-11 01:57:15
