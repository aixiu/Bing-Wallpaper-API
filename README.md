# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![云层中的纽约市天际线](https://cn.bing.com/th?id=OHR.NYCClouds_ZH-CN2585785154_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [云层中的纽约市天际线](https://cn.bing.com/th?id=OHR.NYCClouds_ZH-CN2585785154_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 云雾缭绕的纽约市

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
    "date": "2023-03-27",
    "headline": "云雾缭绕的纽约市",
    "title": "云层中的纽约市天际线",
    "description": "即使笼罩着朦胧雾气，纽约市的天际线也能一眼就被认出。美国最高的建筑中有八座都位于纽约曼哈顿区。帝国大厦也许是纽约最著名的大楼，曾连续36年都是世界上最高的建筑。而现在，世贸中心的一号楼因其高耸的塔尖成为了美国目前最高的建筑。纽约市的许多摩天大楼都是装饰艺术风格，如《周六夜现场》的录制地洛克菲勒广场30号大厦，以及装饰着镀铬合金老鹰及点缀的克莱斯勒大厦。来到纽约，你会忍不住不停抬头去仰望这些百年来的摩登奇迹。",
    "image_url": "https://cn.bing.com/th?id=OHR.NYCClouds_ZH-CN2585785154_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "纽约市是美国人口最稠密的城市，有7000多座高度超35米的高楼大厦，其中至少有101座高度超过198米。"
}
```

UpdataTime：2023-03-27 01:42:13
