# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![玻利维亚乌尤尼盐湖](https://cn.bing.com/th?id=OHR.SalarUyuni_ZH-CN4163237089_1920x1080.webp)
Today: [玻利维亚乌尤尼盐湖](https://cn.bing.com/th?id=OHR.SalarUyuni_ZH-CN4163237089_1920x1080.webp) - 在盐沼与天空之间，万物静谧

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
    "date": "2026-02-07",
    "headline": "在盐沼与天空之间，万物静谧",
    "title": "玻利维亚乌尤尼盐湖",
    "description": "玻利维亚的乌尤尼盐沼并不会循序渐进地展开视野，它仿佛一道由光线构成的地平线，瞬间闯入眼帘。这里是世界上最大的盐沼，面积约4000平方英里，海拔接近12000英尺。景观会随季节剧烈变化：雨季来临时，地面被薄薄的积水覆盖，化作一面巨大的天然镜子，天空与大地在倒影中融为一片耀眼的光面。",
    "image_url": "https://cn.bing.com/th?id=OHR.SalarUyuni_ZH-CN4163237089_1920x1080.webp",
    "main_text": "这片盐沼几乎看不到野生动物和植被，唯一显眼的生命，是成片生长的巨型仙人掌。它们每年仅生长约1厘 米，最高可达12米。"
}
```

UpdataTime：2026-02-07 08:45:42
