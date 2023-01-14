# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![吃樱桃树枝的毛驴](https://cn.bing.com/th?id=OHR.DonkeyFeast_ZH-CN5880627132_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [吃樱桃树枝的毛驴](https://cn.bing.com/th?id=OHR.DonkeyFeast_ZH-CN5880627132_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 快乐小毛驴

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
    "date": "2023-01-14",
    "headline": "快乐小毛驴",
    "title": "吃樱桃树枝的毛驴",
    "description": "照片里这头正在吃樱桃树叶的毛驴可能不知道：今天曾是它们的节日。不过，我们认为任何一天都是赞美驴子的好日子。驴子已经为人类背负重担超过7000年，所以让我们给它们一些关爱吧。如今，全世界有4000多万头驴仍在负重前行，仅仅中国就有1100万头。",
    "image_url": "https://cn.bing.com/th?id=OHR.DonkeyFeast_ZH-CN5880627132_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "英文的“donkey（驴）”一词首次出现于18世纪晚期，但其起源尚未可知。"
}
```

UpdataTime：2023-01-14 01:45:06
