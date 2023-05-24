# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![科孚岛旧城堡](https://cn.bing.com/th?id=OHR.OldFortress_ZH-CN6469523538_1920x1080.webp)
Today: [科孚岛旧城堡](https://cn.bing.com/th?id=OHR.OldFortress_ZH-CN6469523538_1920x1080.webp) - 历史在这里复活

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
    "date": "2023-05-24",
    "headline": "历史在这里复活",
    "title": "科孚岛旧城堡",
    "description": "希腊科孚岛的旧城堡矗立在半岛的尖端，现在是科孚公共图书馆和档案馆的所在地。这座城堡历史悠久，可以追溯到拜占庭时期。6世纪，入侵者袭击了科孚，促使幸存者建造了一个被城堡包围的新村庄。后来在威尼斯统治期间，城堡又经历了加固改建，以抵御奥斯曼军队的侵扰。数个世纪以来，这座希腊地标见证了当地的巨大变化以及几个帝国的兴衰。",
    "image_url": "https://cn.bing.com/th?id=OHR.OldFortress_ZH-CN6469523538_1920x1080.webp",
    "main_text": "城堡内设有科孚公共图书馆，位于英国人早年建造的军营内。城堡还会举行一些艺术和文化展览。"
}
```

UpdataTime：2023-05-24 01:47:06
