# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![正在睡觉的北极狐](https://cn.bing.com/th?id=OHR.NewYearFox_ZH-CN9312618796_1920x1080.webp)
Today: [正在睡觉的北极狐](https://cn.bing.com/th?id=OHR.NewYearFox_ZH-CN9312618796_1920x1080.webp) - 伸个懒腰，迈向新年！

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
    "date": "2026-01-01",
    "headline": "伸个懒腰，迈向新年！",
    "title": "正在睡觉的北极狐",
    "description": "是否感觉需要补足整整一年的休息？今日图片上的这只北极狐懂你，它正窝在冰原岩石间，享受惬意时光。无论新年伴随寒风还是暖阳而来，请给自己五分钟，让身体舒展，再迎接接下来的365天。",
    "image_url": "https://cn.bing.com/th?id=OHR.NewYearFox_ZH-CN9312618796_1920x1080.webp",
    "main_text": "格里高利历在儒略历的基础上优化了闰年制度，让历法更精准，避免季节随时间逐渐错位。"
}
```

UpdataTime：2026-01-01 08:39:51
