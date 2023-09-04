# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![布尔日的沼泽，法国](https://cn.bing.com/th?id=OHR.BourgesMarsh_ZH-CN0505354655_1920x1080.webp)
Today: [布尔日的沼泽，法国](https://cn.bing.com/th?id=OHR.BourgesMarsh_ZH-CN0505354655_1920x1080.webp) - 城市中心的绿色天堂

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
    "date": "2023-09-04",
    "headline": "城市中心的绿色天堂",
    "title": "布尔日的沼泽，法国",
    "description": "布尔日沼泽位于布尔日城市的中心，占地135公顷，为人们提供了一个放松和探索的空间。在中世纪时期，这片沼泽地曾是抵御入侵的城市保护带。",
    "image_url": "https://cn.bing.com/th?id=OHR.BourgesMarsh_ZH-CN0505354655_1920x1080.webp",
    "main_text": "沼泽为很多种无脊椎动物、两栖动物、水鸟和水生哺乳动物提供了栖息地。"
}
```

UpdataTime：2023-09-04 01:21:20
