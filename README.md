# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![中国的梅花](https://cn.bing.com/th?id=OHR.PlumBlossom_ZH-CN5888621119_1920x1080.webp)
Today: [中国的梅花](https://cn.bing.com/th?id=OHR.PlumBlossom_ZH-CN5888621119_1920x1080.webp) - 花开中国

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
    "date": "2025-03-06",
    "headline": "花开中国",
    "title": "中国的梅花",
    "description": "在杭州西湖，这些转瞬即逝的花朵吸引了无数游客，他们纷纷前来欣赏这短暂而绚丽的美景。在中国文化中，梅花象征着纯洁和春天的到来，而在日本，它则代表新的开始。梅花即使在严寒的冬季也能傲然绽放，这种特性使其成为坚毅与希望的象征。目前已知的梅花品种超过 300 种，适应各种园林环境，呈现出丰富多样的形态和颜色。除了视觉上的吸引力，梅花还被用于传统美食，如花茶和酸甜可口的梅子蜜饯。看到这里，为何不亲自去感受这份独特的魅力呢？",
    "image_url": "https://cn.bing.com/th?id=OHR.PlumBlossom_ZH-CN5888621119_1920x1080.webp",
    "main_text": "在中国传统文化中，梅以它的高洁、坚强、谦虚的品格，给人以立志奋发的激励。"
}
```

UpdataTime：2025-03-06 16:32:14
