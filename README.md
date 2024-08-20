# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![大提顿国家公园日出,怀俄明州,美国](https://cn.bing.com/th?id=OHR.TetonSunrise_ZH-CN1118823848_1920x1080.webp)
Today: [大提顿国家公园日出,怀俄明州,美国](https://cn.bing.com/th?id=OHR.TetonSunrise_ZH-CN1118823848_1920x1080.webp) - 鹿和羚羊嬉戏的地方

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
    "date": "2024-08-20",
    "headline": "鹿和羚羊嬉戏的地方",
    "title": "大提顿国家公园日出,怀俄明州,美国",
    "description": "正如今天图片所展示的那样，怀俄明州和大提顿国家公园拥有令人惊叹的美景，这就是为什么它可以吸引人们不断地回到这里。早些年间，法国猎人将这里取名为“三个乳头”，1929年，小约翰·戴维森·洛克菲勒等生态环保人士创建了大提顿国家公园。公园里有灰熊、狼、野牛、驼鹿和白头海雕等动物，是一个几乎未受破坏的动植物生态系统。",
    "image_url": "https://cn.bing.com/th?id=OHR.TetonSunrise_ZH-CN1118823848_1920x1080.webp",
    "main_text": "https://www.bing.com/images/search?q=大提顿国家公园&form=hpbap1"
}
```

UpdataTime：2024-08-20 01:41:36
