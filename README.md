# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![布莱斯峡谷国家公园的石林，犹他州，美国](https://cn.bing.com/th?id=OHR.BryceAnniv_ZH-CN5305245786_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [布莱斯峡谷国家公园的石林，犹他州，美国](https://cn.bing.com/th?id=OHR.BryceAnniv_ZH-CN5305245786_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 冬天的布莱斯峡谷石林

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
    "date": "2023-02-25",
    "headline": "冬天的布莱斯峡谷石林",
    "title": "布莱斯峡谷国家公园的石林，犹他州，美国",
    "description": "当太阳在布莱斯峡谷升起时，白雪皑皑的橙红色岩石闪闪发光。这些修长高耸的岩石被称为石林，而布莱斯峡谷国家公园正是因为拥有地球上密度最高的石林而闻名。这些石林的下层是松软的沉积岩，上面则覆盖着一层更为坚硬的石盖。犹他州冬天的冰霜会侵蚀石盖，最终暴露出底下更易被侵蚀的岩石。值得庆幸的是，这些石林现在还屹立不倒，让我们可以在公园成立100周年之时欣赏大自然的鬼斧神工。",
    "image_url": "https://cn.bing.com/th?id=OHR.BryceAnniv_ZH-CN5305245786_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "布莱斯峡谷并非由流过的溪流侵蚀而成，因此严格来说它并不是一个峡谷。"
}
```

UpdataTime：2023-02-25 01:56:12
