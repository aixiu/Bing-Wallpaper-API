# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![迈阿密海滩海洋大道，美国佛罗里达州](https://cn.bing.com/th?id=OHR.MiamiDT_ZH-CN3528760113_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [迈阿密海滩海洋大道，美国佛罗里达州](https://cn.bing.com/th?id=OHR.MiamiDT_ZH-CN3528760113_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 在艺术天堂追逐夏天

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
    "date": "2022-12-03",
    "headline": "在艺术天堂追逐夏天",
    "title": "迈阿密海滩海洋大道，美国佛罗里达州",
    "description": "海洋大道是迈阿密最受欢迎的景点之一，是位于南海滩的一条观光长廊。在这里，有关迈阿密的一切想象都变成了现实——海滩上的性感女郎，白色沙滩，热带鸡尾酒，热情的拉丁音乐和独特的艺术建筑。",
    "image_url": "https://cn.bing.com/th?id=OHR.MiamiDT_ZH-CN3528760113_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "迈阿密海滩海洋大道是美国电影界的一个传奇地点。《疤面煞星》和《迈阿密风云》等著名电影曾在这里取景拍摄。"
}
```

UpdataTime：2022-12-03 02:22:25
