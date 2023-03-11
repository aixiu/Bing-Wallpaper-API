# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![马萨诸塞州格洛斯特的沼泽地](https://cn.bing.com/th?id=OHR.LongWharf_ZH-CN8793669955_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [马萨诸塞州格洛斯特的沼泽地](https://cn.bing.com/th?id=OHR.LongWharf_ZH-CN8793669955_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 像一张油画

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
    "date": "2023-03-11",
    "headline": "像一张油画",
    "title": "马萨诸塞州格洛斯特的沼泽地",
    "description": "在新英格兰灿烂阳光的照耀下，这片盐沼地里的耐盐植物和海水形成了色彩鲜明的对比。盐沼是水生食物链中重要的一环，同时也是孕育野生动植物的温床。",
    "image_url": "https://cn.bing.com/th?id=OHR.LongWharf_ZH-CN8793669955_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "由于盐沼常常被潮汐浸没，同时含有大量分解物质，所以其泥炭中的氧气含量极低。"
}
```

UpdataTime：2023-03-11 01:44:58
