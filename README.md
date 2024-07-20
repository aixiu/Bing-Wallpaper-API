# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![月球](https://cn.bing.com/th?id=OHR.MineralMoon_ZH-CN2555749456_1920x1080.webp)
Today: [月球](https://cn.bing.com/th?id=OHR.MineralMoon_ZH-CN2555749456_1920x1080.webp) - 到月亮上去

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
    "date": "2024-07-20",
    "headline": "到月亮上去",
    "title": "月球",
    "description": "“个人的一小步，人类的一大步！”今天是国际月球日，旨在纪念阿波罗11号首次实现了人类登月的梦想。这一天最初被定为“国家月球日”，并于2021年被联合国确立为一个获得全球认可的节日。几千年来，人类一直凝视着天空，思索着月亮的起源和神秘之处，太空探索的出现使得月球成为许多任务的目标。",
    "image_url": "https://cn.bing.com/th?id=OHR.MineralMoon_ZH-CN2555749456_1920x1080.webp",
    "main_text": "想象一下，如果地球缩小到硬币大小，月球会有多大？答案是：月球大约只有一粒咖啡豆大小。"
}
```

UpdataTime：2024-07-20 01:37:30
