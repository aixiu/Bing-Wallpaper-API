# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![秋日的白杨树，鱼湖国家森林，犹他州，美国](https://cn.bing.com/th?id=OHR.AspenEquinox_ZH-CN5474695693_1920x1080.webp)
Today: [秋日的白杨树，鱼湖国家森林，犹他州，美国](https://cn.bing.com/th?id=OHR.AspenEquinox_ZH-CN5474695693_1920x1080.webp) - 到冬天的中途

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
    "date": "2025-09-22",
    "headline": "到冬天的中途",
    "title": "秋日的白杨树，鱼湖国家森林，犹他州，美国",
    "description": "随着九月的到来，今天图片中看到的白杨树开始了一年一度的变迁，呈现出鲜艳的黄色，在山丘上荡漾开来。这片森林覆盖了超过2300平方英里的湖泊、小径和山脉，秋天的色彩闪耀着光芒。看着季节与有着比我们遵循的公历更古老的事物同步变化，让人感到一种踏实的感觉。",
    "image_url": "https://cn.bing.com/th?id=OHR.AspenEquinox_ZH-CN5474695693_1920x1080.webp",
    "main_text": "一些白杨克隆树，例如犹他州的潘多树林，是地球上最大、最古老的生物之一，其单一根系支撑着数千个基因相同的茎。"
}
```

UpdataTime：2025-09-22 02:06:48
