# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![爱沙尼亚佩普斯湖上的小冰丘](https://cn.bing.com/th?id=OHR.HummockIce_ZH-CN9917832145_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [爱沙尼亚佩普斯湖上的小冰丘](https://cn.bing.com/th?id=OHR.HummockIce_ZH-CN9917832145_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 当冰块变成了艺术

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
    "date": "2023-01-10",
    "headline": "当冰块变成了艺术",
    "title": "爱沙尼亚佩普斯湖上的小冰丘",
    "description": "佩普斯湖是欧洲第五大湖泊，形成于数亿年前的古生代。这里的沙丘非常有名，当各方面条件恰好时，这些沙丘会在风吹时“唱歌”。在冬天，结冰的湖面上可能形成照片中的堆积冰。这些堆积冰是由浮冰受到缓慢不均匀的挤压而形成的。",
    "image_url": "https://cn.bing.com/th?id=OHR.HummockIce_ZH-CN9917832145_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "1242年，德意志条顿骑士团和亚历山大·涅夫斯基领导的诺夫哥罗德人之间的冰上之战就发生在这里。"
}
```

UpdataTime：2023-01-10 01:55:33
