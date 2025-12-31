# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![除夕夜，奥伯鲍姆桥，柏林，德国](https://cn.bing.com/th?id=OHR.GermanyNewYear_ZH-CN9155122755_1920x1080.webp)
Today: [除夕夜，奥伯鲍姆桥，柏林，德国](https://cn.bing.com/th?id=OHR.GermanyNewYear_ZH-CN9155122755_1920x1080.webp) - 柏林，新年之桥

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
    "date": "2025-12-31",
    "headline": "柏林，新年之桥",
    "title": "除夕夜，奥伯鲍姆桥，柏林，德国",
    "description": "三、二、一……等等，先按下暂停键。新年还没到，但柏林的奥伯鲍姆桥仿佛已经提前按下了“庆祝”按钮。今晚，这座桥不再只是河上的通道，而是一条通往新年的跑道：引擎低鸣，烟花预热，人群齐声练习着那句“新年快乐！”",
    "image_url": "https://cn.bing.com/th?id=OHR.GermanyNewYear_ZH-CN9155122755_1920x1080.webp",
    "main_text": "新年的脚步由时区决定。最先跨入新年的，是国际日期变更线以西的太平洋岛屿：基里巴斯的莱恩群岛、萨摩亚，以及汤加。"
}
```

UpdataTime：2025-12-31 08:40:31
