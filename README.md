# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![从意大利圣天使城堡俯瞰罗马](https://cn.bing.com/th?id=OHR.RomeView_ZH-CN5882212305_1920x1080.webp)
Today: [从意大利圣天使城堡俯瞰罗马](https://cn.bing.com/th?id=OHR.RomeView_ZH-CN5882212305_1920x1080.webp) - 超凡脱俗的风景

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
    "date": "2023-07-01",
    "headline": "超凡脱俗的风景",
    "title": "从意大利圣天使城堡俯瞰罗马",
    "description": "今天的照片是从圣天使堡（又称哈德良陵墓）拍下的罗马美景。圣天使堡是由罗马帝国皇帝哈德良所修建，用作自己和后代的陵墓。除他之外，还有许多皇帝被葬在这里，公元217年的卡拉卡拉是最后一位。",
    "image_url": "https://cn.bing.com/th?id=OHR.RomeView_ZH-CN5882212305_1920x1080.webp",
    "main_text": "罗马圣天使堡的盛名，在很大程度上要归功于改编自丹·布朗的长篇小说《天使与魔鬼》的电影。"
}
```

UpdataTime：2023-07-01 02:14:34
