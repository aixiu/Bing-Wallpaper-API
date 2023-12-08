# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![拉罗克港，圣克莱门特，泽西岛](https://cn.bing.com/th?id=OHR.JerseyIsland_ZH-CN6224973235_1920x1080.webp)
Today: [拉罗克港，圣克莱门特，泽西岛](https://cn.bing.com/th?id=OHR.JerseyIsland_ZH-CN6224973235_1920x1080.webp) - 不是那个泽西海岸!

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
    "date": "2023-12-08",
    "headline": "不是那个泽西海岸!",
    "title": "拉罗克港，圣克莱门特，泽西岛",
    "description": "泽西岛位于法国诺曼底海岸附近，是一个有着北欧名字的英属岛屿。拉罗克港位于岛的东南岸，这里有洁白的沙滩和延伸至水中的高架人行道。海岸线上的花岗岩和深成岩起源于4.2亿多年前，呈现出多样化的颜色和纹理。从港口可以看到圆圆的、矮胖的伊乔塔和较高一些的西摩塔，它们分别建于18世纪和19世纪，是海防建筑。这两座建筑距离海岸都有1800多英尺，如果你想步行到这两座建筑的所在地，不仅需要穿一双结实的鞋子，还只能选在一年中潮水退至最低点的时候。",
    "image_url": "https://cn.bing.com/th?id=OHR.JerseyIsland_ZH-CN6224973235_1920x1080.webp",
    "main_text": "泽西岛一开始属于诺曼底公国，而在1066年诺曼底公爵成了英格兰国王后，泽西岛也就成了英国国王的世袭领地。"
}
```

UpdataTime：2023-12-08 01:33:16
