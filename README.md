# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![印度洋马约特岛，一只呈防御姿态的章鱼](https://cn.bing.com/th?id=OHR.MayotteOctopus_ZH-CN2837659998_1920x1080.webp)
Today: [印度洋马约特岛，一只呈防御姿态的章鱼](https://cn.bing.com/th?id=OHR.MayotteOctopus_ZH-CN2837659998_1920x1080.webp) - 现在你“海”能看见我……

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
    "date": "2026-10-08",
    "headline": "现在你“海”能看见我……",
    "title": "印度洋马约特岛，一只呈防御姿态的章鱼",
    "description": "显然有什么东西越界了。在印度洋马约特岛近海，这只章鱼摆出了一副防御姿态，仿佛在说：无论是什么正在靠近，都该重新考虑一下自己的生命选择。",
    "image_url": "https://cn.bing.com/th?id=OHR.MayotteOctopus_ZH-CN2837659998_1920x1080.webp",
    "image_url_jpg": "https://cn.bing.com/th?id=OHR.MayotteOctopus_ZH-CN2837659998_1920x1200.jpg&rf=LaDigue_1920x1200.jpg",
    "image_url_uhd": "https://cn.bing.com/th?id=OHR.MayotteOctopus_ZH-CN2837659998_UHD.jpg",
    "main_text": "章鱼的化学触觉受体由古老的神经递质受体演化而来，并能检测难溶性分子。"
}
```

UpdateTime：2026-10-08 23:31:21
