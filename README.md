# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![约书亚树国家公园上空的银河，美国加利福尼亚州](https://th.bing.com/th?id=OHR.JTNPMilkyWay_ZH-CN9128830420_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [约书亚树国家公园上空的银河，美国加利福尼亚州](https://th.bing.com/th?id=OHR.JTNPMilkyWay_ZH-CN9128830420_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 沙漠上空的星海

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
    "date": "2023-04-29",
    "headline": "沙漠上空的星海",
    "title": "约书亚树国家公园上空的银河，美国加利福尼亚州",
    "description": "今天是天文日，快准备好望远镜和星图APP去观星吧！为了让更多人对太空感兴趣，道格·伯杰于1973年创立了天文日，他在街角、商场和公园里架设了望远镜，让人们有机会亲眼看到星星。",
    "image_url": "https://th.bing.com/th?id=OHR.JTNPMilkyWay_ZH-CN9128830420_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "银河中心的云层散发着朗姆酒和覆盆子的味道。"
}
```

UpdataTime：2023-04-29 01:41:11
