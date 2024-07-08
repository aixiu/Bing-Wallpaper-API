# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![野生蓝莓](https://cn.bing.com/th?id=OHR.NorwayBlueberries_ZH-CN7643097235_1920x1080.webp)
Today: [野生蓝莓](https://cn.bing.com/th?id=OHR.NorwayBlueberries_ZH-CN7643097235_1920x1080.webp) - 一剂抗氧化剂

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
    "date": "2024-07-08",
    "headline": "一剂抗氧化剂",
    "title": "野生蓝莓",
    "description": "今天，空气中弥漫着一种酸酸甜甜的水果香味，这是美国人心爱的蓝莓，这一天也是美国蓝莓日。野生蓝莓有13000多年的历史，而人工栽培的蓝莓直到20世纪初才出现。当时，农业专家伊丽莎白·科尔曼·怀特和植物学家弗雷德里克·科维尔在新泽西州合作培育出第一个栽培品种，蓝莓才开始被人工种植。",
    "image_url": "https://cn.bing.com/th?id=OHR.NorwayBlueberries_ZH-CN7643097235_1920x1080.webp",
    "main_text": "蓝莓实际上不是蓝色的，而是深紫色。深紫色是花青素的颜色，而蓝莓中恰好含有大量的花青素。"
}
```

UpdataTime：2024-07-08 01:40:46
