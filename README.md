# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![帕克城, 美国犹他州](https://cn.bing.com/th?id=OHR.SFFParkCity_ZH-CN6707019061_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [帕克城, 美国犹他州](https://cn.bing.com/th?id=OHR.SFFParkCity_ZH-CN6707019061_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 圣丹斯上空的云彩

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
    "date": "2023-01-19",
    "headline": "圣丹斯上空的云彩",
    "title": "帕克城, 美国犹他州",
    "description": "尽管城外的景色如此美丽，但今天来到帕克城的人，大多是为了在城里举行的圣丹斯电影节，这是美国独立电影人最大的庆典。昆汀·塔伦蒂诺、史蒂文·索德伯格等好莱坞导演的职业生涯都是从这里开始的。每年都有一批年轻电影人怀揣梦想来到这里，希望能卖出自己的作品。",
    "image_url": "https://cn.bing.com/th?id=OHR.SFFParkCity_ZH-CN6707019061_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "帕克城被陡峭的瓦萨奇山脉环绕，毗邻鹿谷度假村和巨大的帕克城山地度假村，这两个度假村都以滑雪场而闻名。"
}
```

UpdataTime：2023-01-19 01:55:30
