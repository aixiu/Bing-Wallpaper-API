# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![孔雀羽毛](https://cn.bing.com/th?id=OHR.PeacockFeathers_ZH-CN3403145691_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [孔雀羽毛](https://cn.bing.com/th?id=OHR.PeacockFeathers_ZH-CN3403145691_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 华贵的色彩

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
    "date": "2023-03-30",
    "headline": "华贵的色彩",
    "title": "孔雀羽毛",
    "description": "孔雀或许是世界上最色彩斑斓的鸟类。当雄孔雀开屏求偶时，尾羽上的“伪眼”会反射出鲜艳夺目的光泽，以此来吸引雌孔雀。孔雀羽毛迷人的色彩并非来自色素，而是来自羽毛内部的光子晶体结构，也就是“结构色”。结构色十分华丽，能随视角和条件变幻。当交配季节结束，雄孔雀的尾羽就会开始脱落，这正是收集这些漂亮羽毛的好时候。",
    "image_url": "https://cn.bing.com/th?id=OHR.PeacockFeathers_ZH-CN3403145691_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "大多数孔雀在三岁时成熟，当雌孔雀跟雄孔雀交配以后，雄孔雀尾上的羽毛就会开始脱落。"
}
```

UpdataTime：2023-03-30 01:46:25
