# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![彩色粉笔](https://cn.bing.com/th?id=OHR.ColourDay_ZH-CN1032554089_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [彩色粉笔](https://cn.bing.com/th?id=OHR.ColourDay_ZH-CN1032554089_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 你最喜欢什么颜色？

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
    "date": "2023-03-21",
    "headline": "你最喜欢什么颜色？",
    "title": "彩色粉笔",
    "description": "有光的地方，就有色彩，五彩缤纷的世界更具活力和个性。颜色如同音符，不同的颜色传达给人的感觉各不相同。蓝色让人感觉冷静镇定，紫色给人奢华之感，红色则代表激情或危险。国际色彩日这天，世界各地的色彩权威机构齐聚一堂，讨论颜色在工业、艺术、科学、设计等领域的研究应用。世界如此丰富多彩，你可以放慢脚步，细细欣赏品味周围的色彩，这些颜色可能会让你的生活充满惊喜。",
    "image_url": "https://cn.bing.com/th?id=OHR.ColourDay_ZH-CN1032554089_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "人眼通过视网膜中的锥细胞来识别各种颜色。"
}
```

UpdataTime：2023-03-21 01:41:25
