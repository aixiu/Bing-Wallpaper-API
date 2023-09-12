# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![北海日落，诺德多夫，德国](https://cn.bing.com/th?id=OHR.NorthSeaStairs_ZH-CN7044471948_1920x1080.webp)
Today: [北海日落，诺德多夫，德国](https://cn.bing.com/th?id=OHR.NorthSeaStairs_ZH-CN7044471948_1920x1080.webp) - 下一站，地平线。

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
    "date": "2023-09-12",
    "headline": "下一站，地平线。",
    "title": "北海日落，诺德多夫，德国",
    "description": "诺德多夫是位于德国北部海岸阿姆鲁姆岛上的一个小村庄，也是岛上最古老的村庄之一。阿姆鲁姆约有2300名居民，岛上还有许多像诺德多夫这样的渔村。坐落在北海海岸迷人风景中的诺德多夫以其丰富的海洋文化遗产而闻名。透过博物馆和灯塔，我们可以窥见这座岛屿的过去。此外，游客们还可以探索阿姆鲁姆沙丘自然保护区，这里有许多独特的野生动植物：红腹滨鹬、黑雁、知更草和茅膏菜等等。",
    "image_url": "https://cn.bing.com/th?id=OHR.NorthSeaStairs_ZH-CN7044471948_1920x1080.webp",
    "main_text": "1890年，弗里德里希·冯·博德尔施温格在诺德多夫及其北部建立了多家济贫院。1925年，一场大火将村庄烧毁了大半，搭着茅草屋顶的济贫院大多已不复存在，仅存的几座旧时村舍也已挪作他用。"
}
```

UpdataTime：2023-09-12 01:19:05
