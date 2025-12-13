# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![默塞德河, 优胜美地国家公园, 加利福尼亚, 美国](https://cn.bing.com/th?id=OHR.YosemiteWinter_ZH-CN3824387818_1920x1080.webp)
Today: [默塞德河, 优胜美地国家公园, 加利福尼亚, 美国](https://cn.bing.com/th?id=OHR.YosemiteWinter_ZH-CN3824387818_1920x1080.webp) - 冰封的倒影

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
    "date": "2025-12-13",
    "headline": "冰封的倒影",
    "title": "默塞德河, 优胜美地国家公园, 加利福尼亚, 美国",
    "description": "每一幅杰作都需要点睛之笔。而优胜美地的点睛之笔便是默塞德河。作为美国国家级“野生与风景河流”之一，这条水系起源于内华达山脉高处，汇集雪水，蜿蜒145英里，穿过优胜美地山谷，流入加州中央谷地。",
    "image_url": "https://cn.bing.com/th?id=OHR.YosemiteWinter_ZH-CN3824387818_1920x1080.webp",
    "main_text": "默塞德河的主支流是夏季休闲的好去处，这里可以游泳、徒步、钓鱼、漂流、淘金、露营，享受各种户外乐趣。由于海拔较低，冬季也非常适合来一场轻松的日间徒步。"
}
```

UpdataTime：2025-12-13 02:07:35
