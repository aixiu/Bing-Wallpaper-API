# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![南极洲冰山上的阿德利企鹅](https://cn.bing.com/th?id=OHR.PenguinDirections_ZH-CN8498684753_1920x1080.webp)
Today: [南极洲冰山上的阿德利企鹅](https://cn.bing.com/th?id=OHR.PenguinDirections_ZH-CN8498684753_1920x1080.webp) - 很高兴在这里见到你们！

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
    "date": "2024-04-25",
    "headline": "很高兴在这里见到你们！",
    "title": "南极洲冰山上的阿德利企鹅",
    "description": "可以滑行，又何需飞行？世界企鹅日快乐！这些不会飞的鸟主要栖息在南极洲，从帝企鹅到今天的明星阿德利企鹅，种类繁多。1840年，法国冒险家儒勒·杜蒙·德维尔发现了阿德利企鹅，并决定以他心爱的妻子的名字“阿德利”来命名这种企鹅。阿德利企鹅虽然体型娇小，但游泳动作敏捷，可以潜入575英尺深的海底寻找长得像虾一样的磷虾或鱼类。它们是社会性动物，会聚集在小群中觅食、狩猎和保护自己。调皮捣蛋的阿德利企鹅还会偷窃附近巢穴中的鹅卵石来加固自己的巢穴，以保护自己的蛋和雏鸟免受南极洲恶劣环境和捕食者的伤害。",
    "image_url": "https://cn.bing.com/th?id=OHR.PenguinDirections_ZH-CN8498684753_1920x1080.webp",
    "main_text": "在远古时代，甚至出现过身高近2米、体重80千克的巨型企鹅！"
}
```

UpdataTime：2024-04-25 01:31:36
