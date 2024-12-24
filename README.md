# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![德国圣诞市场](https://cn.bing.com/th?id=OHR.SantaSnowglobe_ZH-CN2671421527_1920x1080.webp)
Today: [德国圣诞市场](https://cn.bing.com/th?id=OHR.SantaSnowglobe_ZH-CN2671421527_1920x1080.webp) - 祝你圣诞快乐！

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
    "date": "2024-12-24",
    "headline": "祝你圣诞快乐！",
    "title": "德国圣诞市场",
    "description": "德国的圣诞集市是一个值得珍视的节日传统，它带领游客进入一个神奇的世界，这里有闪烁的灯光、欢快的音乐和美味可口的季节性美食。这些集市的历史可以追溯至中世纪，它们在德国各地的城镇广场举办，其中最具代表性的是纽伦堡、慕尼黑和德累斯顿等城市。每个集市都会展示独特的地方手工艺品以及节日习俗。在这里，游客可以看到手工制作的装饰品，木制玩具以及舒适的冬日配饰，还有热红酒、姜饼和烤坚果等特色食品。在浓厚的圣诞气氛中，这里是边吃边逛的理想之地。",
    "image_url": "https://cn.bing.com/th?id=OHR.SantaSnowglobe_ZH-CN2671421527_1920x1080.webp",
    "main_text": "全球最著名的圣诞集市之一就位于德国纽伦堡。除此之外，该地还以其历史魅力、节日气氛、传统工艺品和美食而闻名。"
}
```

UpdataTime：2024-12-24 08:30:15
