# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![红海星, 地中海](https://cn.bing.com/th?id=OHR.RedSeaStars_ZH-CN6243743747_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [红海星, 地中海](https://cn.bing.com/th?id=OHR.RedSeaStars_ZH-CN6243743747_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 日光下的星星

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
    "date": "2023-04-14",
    "headline": "日光下的星星",
    "title": "红海星, 地中海",
    "description": "海星，又称星鱼，是最迷人的海洋生物之一。首先，虽然其名称叫“星鱼”，但实际上根本不是鱼，它们属于海洋无脊椎动物中的棘皮动物。海星的身体是五角星状的，多条“臂”从身体中央延伸出来，呈辐射对称状。",
    "image_url": "https://cn.bing.com/th?id=OHR.RedSeaStars_ZH-CN6243743747_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "红海星被认为是一个关键物种，因为它们没有天敌。"
}
```

UpdataTime：2023-04-14 01:38:40
