# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![苏州古镇风景，江苏省，中国](https://cn.bing.com/th?id=OHR.QingMingY25_ZH-CN9818431198_1920x1080.webp)
Today: [苏州古镇风景，江苏省，中国](https://cn.bing.com/th?id=OHR.QingMingY25_ZH-CN9818431198_1920x1080.webp) - 春和景明

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
    "date": "2025-04-03",
    "headline": "春和景明",
    "title": "苏州古镇风景，江苏省，中国",
    "description": "清明是中国二十四节气之一，源于古代祖先信仰和春祭。至今，扫墓、踏青仍是清明节的主要活动。清明节，春回大地，万物生机，正是人们出门赏春的好时节。",
    "image_url": "https://cn.bing.com/th?id=OHR.QingMingY25_ZH-CN9818431198_1920x1080.webp",
    "main_text": "同里古镇位于苏州，也是江南六大古镇之一。古镇内有许多精致的园林，古色古香，极具江南特色。"
}
```

UpdataTime：2025-04-03 16:32:32
