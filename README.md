# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![伊夫堡，马赛，法国](https://cn.bing.com/th?id=OHR.PortMarseille_ZH-CN3194394496_1920x1080.webp)
Today: [伊夫堡，马赛，法国](https://cn.bing.com/th?id=OHR.PortMarseille_ZH-CN3194394496_1920x1080.webp) - 海港景色

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
    "date": "2024-05-08",
    "headline": "海港景色",
    "title": "伊夫堡，马赛，法国",
    "description": "准备好在法国马赛享受阳光和奥林匹克精神吧。马赛是一座充满活力的海滨城市，以其丰富的海洋遗产和文化多样性而闻名，是通往地中海的门户。今天，奥运火炬的到来点燃了这里期待奥运的热潮。作为连接现代奥运会与古希腊文化遗产的一个象征，奥运火炬于4月16日在希腊奥林匹亚点燃，奥运圣火就此开启环绕法国的旅程，直至抵达巴黎奥运会。夏季奥运会将于7月26日开幕，而马赛正在为举办奥运会帆船比赛做准备，这座城市充满活力，将传统与创新融为一体。",
    "image_url": "https://cn.bing.com/th?id=OHR.PortMarseille_ZH-CN3194394496_1920x1080.webp",
    "main_text": "马赛拥有世界上最大的商业港口，每年吞吐量超过1亿吨。"
}
```

UpdataTime：2024-05-08 01:11:09
