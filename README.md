# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![黄山的日落，安徽省，中国](https://cn.bing.com/th?id=OHR.LiDong2023_ZH-CN5089092069_1920x1080.webp)
Today: [黄山的日落，安徽省，中国](https://cn.bing.com/th?id=OHR.LiDong2023_ZH-CN5089092069_1920x1080.webp) - 冬日里的壮丽美景

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
    "date": "2023-11-08",
    "headline": "冬日里的壮丽美景",
    "title": "黄山的日落，安徽省，中国",
    "description": "立冬是中国二十四节气中的第十九个节气。 这也是冬天的开始。在南方，初冬时节一般都不是很冷。随着时间的推移，冬至后冷空气频繁南下，气温逐渐下降。入冬后，北方大部分地区将出现雨雪降温天气。华北部分地区此时常下初雪。",
    "image_url": "https://cn.bing.com/th?id=OHR.LiDong2023_ZH-CN5089092069_1920x1080.webp",
    "main_text": "自唐代至清末，有关黄山的诗词有2万多首，并有一个画派因此而得名。"
}
```

UpdataTime：2023-11-08 01:28:53
