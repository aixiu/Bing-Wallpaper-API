# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![月球与地球由阿耳忒弥斯2号机组人员拍摄](https://cn.bing.com/th?id=OHR.Artemis_ZH-CN3540365575_1920x1080.webp)
Today: [月球与地球由阿耳忒弥斯2号机组人员拍摄](https://cn.bing.com/th?id=OHR.Artemis_ZH-CN3540365575_1920x1080.webp) - 月瞰寰宇

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
    "date": "2026-07-19",
    "headline": "月瞰寰宇",
    "title": "月球与地球由阿耳忒弥斯2号机组人员拍摄",
    "description": "从月球那遍布环形山的表面望去，地球在无垠的黑暗中呈现为一抹微光闪烁的娥眉状——这一罕见的奇观与我们惯常的地面观测视角截然相反。这片由数十亿年撞击作用塑造的荒芜地貌，完整地保存了早期太阳系的演化记录。7月20日是国际月球日，旨在纪念1969年阿波罗11号任务中人类首次踏上月球表面的历史性时刻。该纪念日由联合国于2021年设立，不仅致敬过去的辉煌成就，更聚焦于当下持续不断的月球探测努力。",
    "image_url": "https://cn.bing.com/th?id=OHR.Artemis_ZH-CN3540365575_1920x1080.webp",
    "main_text": "月球的自转速率与其绕地球公转的速率完全同步，由于这种“同步自转”特性，我们在地球上观测时始终只能看到月球的同一面。"
}
```

UpdataTime：2026-07-19 17:09:48
