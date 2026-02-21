# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![一只红狐狸站在雪地里，大提顿国家公园，怀俄明州，美国](https://cn.bing.com/th?id=OHR.TetonFox_ZH-CN9461948674_1920x1080.webp)
Today: [一只红狐狸站在雪地里，大提顿国家公园，怀俄明州，美国](https://cn.bing.com/th?id=OHR.TetonFox_ZH-CN9461948674_1920x1080.webp) - 冬日的低语

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
    "date": "2026-02-21",
    "headline": "冬日的低语",
    "title": "一只红狐狸站在雪地里，大提顿国家公园，怀俄明州，美国",
    "description": "大雪纷飞中，一只赤狐站在大提顿国家公园的雪地里。这一刻不仅美得纯粹，也让人窥见赤狐在严寒中自如生存的力量。锐利的目光、浓密而火红的毛皮，让它立刻显得与众不同，即便在怀俄明州严酷的冬季，也能安然生存。积雪会吞没声音，但赤狐异常灵敏的听觉，仍能捕捉到雪层之下猎物的细微动静。你几乎可以想象它在飞雪中短暂停步，耳朵微转，身形凝固，专注等待那一丝几不可闻的声响。",
    "image_url": "https://cn.bing.com/th?id=OHR.TetonFox_ZH-CN9461948674_1920x1080.webp",
    "main_text": "赤狐起源于欧亚大陆，早可追溯至至少40万年前的中更新世，并在约13万年前扩散至北美地区。"
}
```

UpdataTime：2026-02-21 02:44:09
