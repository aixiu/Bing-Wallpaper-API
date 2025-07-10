# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![日出时的东京，日本](https://cn.bing.com/th?id=OHR.TokyoSunrise_ZH-CN0091906710_1920x1080.webp)
Today: [日出时的东京，日本](https://cn.bing.com/th?id=OHR.TokyoSunrise_ZH-CN0091906710_1920x1080.webp) - 把我们都算上

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
    "date": "2025-07-10",
    "headline": "把我们都算上",
    "title": "日出时的东京，日本",
    "description": "我们生活的地球早已人满为患，并且仍在不断变得更加拥挤。目前全球人口已达82亿，且呈持续增长之势。世界人口日旨在引发人们对人口增长如何影响城市发展、粮食供给与未来前景的思考。该纪念日设立于1989年，聚焦于不受控的人口增长对可持续性带来的影响，其灵感源自1987年全球人口首次突破50亿的“50亿人口日”。随着城市不断扩张，绿地面积减少，农业也在有限的土地和水资源中展开竞争。然而前路并非无解：通过教育投资、改善医疗可及性，以及建设更智慧的城市，人口增长与可持续发展之间可以实现平衡。",
    "image_url": "https://cn.bing.com/th?id=OHR.TokyoSunrise_ZH-CN0091906710_1920x1080.webp",
    "main_text": "在过去三十年间，世界各地的社会在人口数据的收集、分析与使用方面取得了显著进步。如今的人口数据可以按年龄、族裔、性别及其他因素进行细致划分，更加准确地反映出我们社会的多样性。"
}
```

UpdataTime：2025-07-10 16:37:13
