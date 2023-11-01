# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![上巴尔城堡，阿尔萨斯，法国](https://cn.bing.com/th?id=OHR.HautBarr_ZH-CN8274813404_1920x1080.webp)
Today: [上巴尔城堡，阿尔萨斯，法国](https://cn.bing.com/th?id=OHR.HautBarr_ZH-CN8274813404_1920x1080.webp) - 你知道“阿尔萨斯之眼”吗？

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
    "date": "2023-11-01",
    "headline": "你知道“阿尔萨斯之眼”吗？",
    "title": "上巴尔城堡，阿尔萨斯，法国",
    "description": "上巴尔城堡是一座位于阿尔萨斯北部，海拔450米的中世纪堡垒。它建于1170年，几个世纪以来经历了重大改造和修复。该城堡的建造由斯特拉斯堡的主教发起，旨在监视佐恩山谷和阿尔萨斯平原，因此被赋予了富有诗意的绰号“阿尔萨斯之眼”。天气晴朗时，甚至可以看到斯特拉斯堡大教堂的尖顶。",
    "image_url": "https://cn.bing.com/th?id=OHR.HautBarr_ZH-CN8274813404_1920x1080.webp",
    "main_text": "上巴尔城堡于1770年左右被废弃，但金库一直被占用，直到法国大革命。"
}
```

UpdataTime：2023-11-01 01:32:42
