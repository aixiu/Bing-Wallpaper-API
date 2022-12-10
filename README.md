# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![玻利维亚的乌尤尼盐沼](https://cn.bing.com/th?id=OHR.SaltDesert_ZH-CN4728398785_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [玻利维亚的乌尤尼盐沼](https://cn.bing.com/th?id=OHR.SaltDesert_ZH-CN4728398785_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 一小撮盐可不够

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
    "date": "2022-12-10",
    "headline": "一小撮盐可不够",
    "title": "玻利维亚的乌尤尼盐沼",
    "description": "在安第斯山脉的顶峰附近，海拔两英里以上的地方出现了自然界的异象——这是一片面积比许多国家都大的盐滩。这是玻利维亚的乌尤尼盐沼，它是世界上最大的盐沼，占地约4000平方英里。乌尤尼盐沼是一个古老湖泊的遗迹，这个湖泊在很久以前蒸发，留下了厚厚的矿物地壳。这里不仅是食用盐的来源，也是火烈鸟重要的繁殖地。但是，对于一个电池紧缺的世界来说，其最宝贵的财富可能藏在地壳下面——那里藏着大量富含锂的盐水。",
    "image_url": "https://cn.bing.com/th?id=OHR.SaltDesert_ZH-CN4728398785_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "乌尤尼盐沼曾是《星球大战：最后的绝地武士》等电影的取景地。"
}
```

UpdataTime：2022-12-10 01:48:34
