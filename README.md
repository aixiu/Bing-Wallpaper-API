# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![布鲁克林大桥，纽约市，美国](https://cn.bing.com/th?id=OHR.BKBridge_ZH-CN3870511222_1920x1080.webp)
Today: [布鲁克林大桥，纽约市，美国](https://cn.bing.com/th?id=OHR.BKBridge_ZH-CN3870511222_1920x1080.webp) - 跨越历史

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
    "date": "2026-08-24",
    "headline": "跨越历史",
    "title": "布鲁克林大桥，纽约市，美国",
    "description": "布鲁克林大桥连接的不只是曼哈顿和布鲁克林——它还连接着历史、工程学以及几个令人惊讶的故事。大桥历经14年建造，于1883年开放，成为世界上第一座钢丝悬索桥，永久改变了纽约人跨越东河的方式。",
    "image_url": "https://cn.bing.com/th?id=OHR.BKBridge_ZH-CN3870511222_1920x1080.webp",
    "main_text": "2024年，布鲁克林大桥日均承载103,051辆机动车、28,845名行人和5,504名骑行者。"
}
```

UpdataTime：2026-08-24 08:58:25
