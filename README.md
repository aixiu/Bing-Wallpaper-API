# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![城市灯光在下方划过, 拍摄于国际空间站](https://cn.bing.com/th?id=OHR.SpaceTrails_ZH-CN8377463217_1920x1080.webp)
Today: [城市灯光在下方划过, 拍摄于国际空间站](https://cn.bing.com/th?id=OHR.SpaceTrails_ZH-CN8377463217_1920x1080.webp) - 离开地球的第一步

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
    "date": "2026-04-11",
    "headline": "离开地球的第一步",
    "title": "城市灯光在下方划过, 拍摄于国际空间站",
    "description": "今天，世界纪念国际载人航天日，这是联合国设立的纪念日，旨在纪念人类首次进入太空的旅程以及人类太空时代的开始。这个日期回忆起1961年4月12日，尤里·加加林绕地球飞行，证明人类可以离开地球并安全返回。",
    "image_url": "https://cn.bing.com/th?id=OHR.SpaceTrails_ZH-CN8377463217_1920x1080.webp",
    "main_text": "联合国在2011年设立了国际人类航天日，距首次有人类航天飞行已有50年。"
}
```

UpdataTime：2026-04-11 16:51:06
