# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![夏日盛开的荷花](https://cn.bing.com/th?id=OHR.SummerSolstice2023_ZH-CN5038619036_1920x1080.webp)
Today: [夏日盛开的荷花](https://cn.bing.com/th?id=OHR.SummerSolstice2023_ZH-CN5038619036_1920x1080.webp) - 夏日仙境

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
    "date": "2023-06-21",
    "headline": "夏日仙境",
    "title": "夏日盛开的荷花",
    "description": "夏至是二十四节气中的一个，也是一年中白昼最长的一天。在这一天，太阳直射北回归线，北半球的温度达到最高，而南半球则是冬至。夏至的日期通常在公历6月21日或22日，不同地区有不同的习俗和活动来庆祝这个节气。在中国，夏至被认为是阴阳转化的重要时刻，也是祭祀天地和祖先的日子。人们会吃面条、鸡蛋、荔枝等食物来祈求健康和长寿，也会烧香、挂艾草、泡药浴等来驱除瘟疫和邪气。",
    "image_url": "https://cn.bing.com/th?id=OHR.SummerSolstice2023_ZH-CN5038619036_1920x1080.webp",
    "main_text": "“荷”被称为“活化石”，是被子植物中起源最早的植物之一。"
}
```

UpdataTime：2023-06-21 01:48:34
