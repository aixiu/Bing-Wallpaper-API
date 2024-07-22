# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![树上的中国小熊猫, 成都, 四川省, 中国](https://cn.bing.com/th?id=OHR.TheGreatHeat2024_ZH-CN6033129823_1920x1080.webp)
Today: [树上的中国小熊猫, 成都, 四川省, 中国](https://cn.bing.com/th?id=OHR.TheGreatHeat2024_ZH-CN6033129823_1920x1080.webp) - 和我一起避暑吧！

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
    "date": "2024-07-22",
    "headline": "和我一起避暑吧！",
    "title": "树上的中国小熊猫, 成都, 四川省, 中国",
    "description": "今天是大暑节气，既是夏季的最后一个节气，也是一年中阳光最猛烈、最炎热的日子。图中那只在树枝上看向我们的小可爱是大名鼎鼎的中华小熊猫。夏日炎炎，我们也需要放松一下，挑个绿荫密布的地方避暑吧！",
    "image_url": "https://cn.bing.com/th?id=OHR.TheGreatHeat2024_ZH-CN6033129823_1920x1080.webp",
    "main_text": "2020年，中国科学院动物研究所研究员魏辅文研究发现两个小熊猫亚种约于22万年前就分家了，其后鲜有基因交流，故将小熊猫川西亚种提升为种阶并命名为中华小熊猫。"
}
```

UpdataTime：2024-07-22 01:43:09
