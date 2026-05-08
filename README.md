# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![撒丁岛母驴和幼崽, 法国](https://cn.bing.com/th?id=OHR.SardinianDonkey_ZH-CN0758031524_1920x1080.webp)
Today: [撒丁岛母驴和幼崽, 法国](https://cn.bing.com/th?id=OHR.SardinianDonkey_ZH-CN0758031524_1920x1080.webp) - 不仅仅是一声咿呀学语

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
    "date": "2026-05-08",
    "headline": "不仅仅是一声咿呀学语",
    "title": "撒丁岛母驴和幼崽, 法国",
    "description": "世界驴日旨在庆祝人类最默默无闻却能力出众的伙伴之一——驴。数千年来，驴一直与人类并肩工作，它们以耐力、敏锐的记忆力和在崎岖地形上稳健的步伐而备受推崇。人们常常误以为它们固执，但实际上它们是谨慎的思考者——它们会停下来评估风险，而不是贸然行事。",
    "image_url": "https://cn.bing.com/th?id=OHR.SardinianDonkey_ZH-CN0758031524_1920x1080.webp",
    "main_text": "骡子是公驴和母马杂交产生的后代。"
}
```

UpdataTime：2026-05-08 09:47:48
