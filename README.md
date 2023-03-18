# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![甘博阿陨击坑，火星](https://cn.bing.com/th?id=OHR.MarsTars_ZH-CN0496313394_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [甘博阿陨击坑，火星](https://cn.bing.com/th?id=OHR.MarsTars_ZH-CN0496313394_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 此景只应天上有

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
    "date": "2023-03-18",
    "headline": "此景只应天上有",
    "title": "甘博阿陨击坑，火星",
    "description": "在火星上生存相当艰难，天气极寒、干燥，而且条件恶劣。火星上的平均温度约为零下62摄氏度，两极的温度甚至可能低至零下152摄氏度。但这颗行星上有许多峡谷、死火山和冰盖，远观还是很美的。火星勘测轨道飞行器发回的大多数照片都显示火星是一颗红色星球，这是因为火星表面有大量红色的赤铁矿，所以呈现橘红色。",
    "image_url": "https://cn.bing.com/th?id=OHR.MarsTars_ZH-CN0496313394_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "人类曾给火星上的风声录音。"
}
```

UpdataTime：2023-03-18 01:47:14
