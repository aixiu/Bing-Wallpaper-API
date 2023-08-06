# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![镜池，长野，日本](https://cn.bing.com/th?id=OHR.NaganoPond_ZH-CN8794832798_1920x1080.webp)
Today: [镜池，长野，日本](https://cn.bing.com/th?id=OHR.NaganoPond_ZH-CN8794832798_1920x1080.webp) - 一面反映大自然之美的镜子

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
    "date": "2023-08-06",
    "headline": "一面反映大自然之美的镜子",
    "title": "镜池，长野，日本",
    "description": "迷人的镜池坐落在日本长野。水池周围清幽的环境完美倒映在这个人工水库的镜面般的湖水中。被郁郁葱葱的绿色植物和户隐山脉所包围的镜池，四季的风景都各有千秋。在樱花盛开的季节，瓣瓣樱花会随着微风在湖面起伏。秋日，周围橙黄的树木倒映在湖面上，仿佛湖中也有一片人间仙境。",
    "image_url": "https://cn.bing.com/th?id=OHR.NaganoPond_ZH-CN8794832798_1920x1080.webp",
    "main_text": "长野的善光寺始建于7世纪，是一个重要的朝圣地。善光寺供奉着一尊日本最古老的佛像，被称为密佛，从不对外展示，仅每六年向公众展示一次其复制品。"
}
```

UpdataTime：2023-08-06 01:31:14
