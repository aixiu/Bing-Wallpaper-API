# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![从国际空间站看到的巴哈马周围的蓝绿色水域](https://cn.bing.com/th?id=OHR.BlueBahamas_ZH-CN2083290847_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [从国际空间站看到的巴哈马周围的蓝绿色水域](https://cn.bing.com/th?id=OHR.BlueBahamas_ZH-CN2083290847_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 像极了艺术画作的真实照片

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
    "date": "2023-01-28",
    "headline": "像极了艺术画作的真实照片",
    "title": "从国际空间站看到的巴哈马周围的蓝绿色水域",
    "description": "对于国际空间站的宇航员来说，巴哈马群岛是一个很适合拍照的目标。从空间站俯瞰下去，水面之下的巨大山丘便形成了这些漂亮的纹路。今天照片里的这些海底山丘深度可达13000英尺。",
    "image_url": "https://cn.bing.com/th?id=OHR.BlueBahamas_ZH-CN2083290847_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "巴哈马群岛占据了庐卡雅群岛的大部分，由近700个环状珊瑚岛和主要由珊瑚或沙子构成的岛礁组成。"
}
```

UpdataTime：2023-01-28 01:52:50
