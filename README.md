# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![犹他州锡安国家公园的维尔京河，美国](https://cn.bing.com/th?id=OHR.ZNPVR_ZH-CN0123954914_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [犹他州锡安国家公园的维尔京河，美国](https://cn.bing.com/th?id=OHR.ZNPVR_ZH-CN0123954914_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 历经百年的锡安国家公园

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
    "date": "2022-11-18",
    "headline": "历经百年的锡安国家公园",
    "title": "犹他州锡安国家公园的维尔京河，美国",
    "description": "今天照片上展示的是维尔京河，它绵延16英里，切割出了壮丽的锡安峡谷。维尔京河流经锡安国家公园，该区域有许多当地特有的动植物。科罗拉多高原、大盆地和莫哈韦沙漠在这里交汇，形成了独特的交叉生物群落。若没有维尔京河的河水，当地的许多罕见动植物都会无法生存。",
    "image_url": "https://cn.bing.com/th?id=OHR.ZNPVR_ZH-CN0123954914_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "2009年，维尔京河被指定为犹他州第一条自然风景河流。"
}
```

UpdataTime：2022-11-18 16:59:33
