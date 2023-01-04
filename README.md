# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![从国际空间站看到的地球](https://cn.bing.com/th?id=OHR.Perihelion_ZH-CN8681537155_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [从国际空间站看到的地球](https://cn.bing.com/th?id=OHR.Perihelion_ZH-CN8681537155_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 如此接近，却又如此遥远

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
    "date": "2023-01-04",
    "headline": "如此接近，却又如此遥远",
    "title": "从国际空间站看到的地球",
    "description": "今天是地球的近日点，由于地球绕太阳公转的轨道是椭圆形的，所以冬至后两周，地球距离太阳最近。你可能有疑问：地球离太阳最近的时候，为什么我们没觉得更热？其实，这是因为近日点的时候地球所接受到的太阳辐射只比平时强了大约7%，这种微小的差异对地球天气的影响并不大。",
    "image_url": "https://cn.bing.com/th?id=OHR.Perihelion_ZH-CN8681537155_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "地球距离太阳最近的时候，北半球为冬天，南半球为夏天。"
}
```

UpdataTime：2023-01-04 01:49:33
