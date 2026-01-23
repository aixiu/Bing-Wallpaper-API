# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![绵羊在雪地里吃草，冰岛](https://cn.bing.com/th?id=OHR.IcelandSheep_ZH-CN3931993073_1920x1080.webp)
Today: [绵羊在雪地里吃草，冰岛](https://cn.bing.com/th?id=OHR.IcelandSheep_ZH-CN3931993073_1920x1080.webp) - 霜雪中的盛宴

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
    "date": "2026-01-23",
    "headline": "霜雪中的盛宴",
    "title": "绵羊在雪地里吃草，冰岛",
    "description": "一月寒意袭来时，冰岛人会借由“仲冬节”寻回温暖与传统。这个节日以北欧神话中的冬之精灵“托里”为名，起初是一场向诸神献祭、祈求度过漫冬的祭宴。如今，它演变成一场既带着古老气息，又洋溢欢聚之情的文化盛会。",
    "image_url": "https://cn.bing.com/th?id=OHR.IcelandSheep_ZH-CN3931993073_1920x1080.webp",
    "main_text": "19世纪末，一群冰岛学生复兴了“仲冬节”。二战结束后，民族主义推动文化复兴，冰岛人也让这项古老传统重新受到关注，甚至重新登上了各地餐厅的菜单。"
}
```

UpdataTime：2026-01-23 02:26:11
