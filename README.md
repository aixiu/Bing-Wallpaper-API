# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![霍亨索伦城堡，德国](https://cn.bing.com/th?id=OHR.HohenzollernBurg_ZH-CN8109082566_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [霍亨索伦城堡，德国](https://cn.bing.com/th?id=OHR.HohenzollernBurg_ZH-CN8109082566_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 正如童话一般

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
    "date": "2023-01-02",
    "headline": "正如童话一般",
    "title": "霍亨索伦城堡，德国",
    "description": "迷人的霍亨索伦城堡经过三次重建后，是真的魅力非凡。这座城堡位于霍亨索伦山顶，修建于11世纪，但大部分建筑在1423年长达10个月的围攻中被摧毁，直到几十年后才得以重建。之后它成为了一个重要的战略据点，然而后来它再次失修。19世纪，普鲁士国王腓特烈·威廉四世（他因在德国各地建造了许多伟大的建筑而闻名）在这里建造了一座新的城堡，几乎完全替换了这座城堡15世纪的建筑结构。如今，霍亨索伦城堡已成为一座露天博物馆，每年接待超过35万名游客，是德国参观人数最多的城堡之一。",
    "image_url": "https://cn.bing.com/th?id=OHR.HohenzollernBurg_ZH-CN8109082566_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "霍亨索伦城堡每年接待超过35万名游客，是德国参观人数最多的城堡之一。"
}
```

UpdataTime：2023-01-02 01:47:15
