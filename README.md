# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![钻石冰沙滩，冰岛](https://cn.bing.com/th?id=OHR.IcelandBeach_ZH-CN1632329693_1920x1080.webp)
Today: [钻石冰沙滩，冰岛](https://cn.bing.com/th?id=OHR.IcelandBeach_ZH-CN1632329693_1920x1080.webp) - 撒了一地的“钻石”

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
    "date": "2024-01-24",
    "headline": "撒了一地的“钻石”",
    "title": "钻石冰沙滩，冰岛",
    "description": "从峡湾和熔岩荒原到冰洞和黑沙滩，就像我们今天在图片中看到的那样，冰岛是一个自然奇观的宝库。钻石冰沙滩是冰岛最受欢迎的自然地标之一。这个独特的沙滩位于杰古沙龙冰河湖附近，其名字源于从冰川上脱落的冰山碎片，当这些冰山碎片被冲到岸上后，在黑色沙子上就像一颗颗闪闪发光的钻石，而这些黑色沙子则是来自被侵蚀的火山岩。清澈的冰块与黑色的沙子形成鲜明对比，尤其是当阳光照射在冰面上时，会产生一种超现实的景象，因此这里是冰岛南海岸的必游之地。",
    "image_url": "https://cn.bing.com/th?id=OHR.IcelandBeach_ZH-CN1632329693_1920x1080.webp",
    "main_text": "当阳光照射在冰层上时，由于光的散射作用，钻石海滩的冰有时会变成蓝色。"
}
```

UpdataTime：2024-01-24 01:34:58
