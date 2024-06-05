# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![马达加斯加的马苏阿拉国家公园](https://cn.bing.com/th?id=OHR.MadagascarRiver_ZH-CN3842472014_1920x1080.webp)
Today: [马达加斯加的马苏阿拉国家公园](https://cn.bing.com/th?id=OHR.MadagascarRiver_ZH-CN3842472014_1920x1080.webp) - 世界环境日快乐！

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
    "date": "2024-06-05",
    "headline": "世界环境日快乐！",
    "title": "马达加斯加的马苏阿拉国家公园",
    "description": "世界环境日快乐！1973年，首届世界环境日活动以“只有一个地球”为主题，由联合国组织举办，旨在鼓励人们保护环境。如今，全世界有143个国家庆祝这个节日。今年的主题将聚于焦土地恢复、荒漠化和抗旱能力。",
    "image_url": "https://cn.bing.com/th?id=OHR.MadagascarRiver_ZH-CN3842472014_1920x1080.webp",
    "main_text": "2024年世界环境日将在沙特阿拉伯举行，主题活动将聚焦于土地恢复、荒漠化和抗旱能力。"
}
```

UpdataTime：2024-06-05 01:35:19
