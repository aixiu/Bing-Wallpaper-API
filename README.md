# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![斯托尔石山，天空之岛，苏格兰](https://cn.bing.com/th?id=OHR.StorrRocks_ZH-CN4956679462_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [斯托尔石山，天空之岛，苏格兰](https://cn.bing.com/th?id=OHR.StorrRocks_ZH-CN4956679462_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 天空之岛

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
    "date": "2022-12-29",
    "headline": "天空之岛",
    "title": "斯托尔石山，天空之岛，苏格兰",
    "description": "今天照片展示的是斯托尔山的老人峰，这座巨大的石峰耸立在英国最长的连续山体滑坡区之上。岛上有许多怪异而奇妙的岩石，都是由远古一次大滑坡形成的。",
    "image_url": "https://cn.bing.com/th?id=OHR.StorrRocks_ZH-CN4956679462_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "天空之岛是观赏野生动物的好地方，这里的白尾海雕是观鸟者的首选。"
}
```

UpdataTime：2022-12-29 01:48:13
