# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![蓑羽鹤, 印度](https://cn.bing.com/th?id=OHR.IndiaCranes_ZH-CN5871338482_1920x1080.webp)
Today: [蓑羽鹤, 印度](https://cn.bing.com/th?id=OHR.IndiaCranes_ZH-CN5871338482_1920x1080.webp) - 优雅的动态

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
    "date": "2026-03-30",
    "headline": "优雅的动态",
    "title": "蓑羽鹤, 印度",
    "description": "蓑羽鹤是一种体型虽小却引人注目的候鸟，分布于中亚各地，繁殖地位于哈萨克斯坦、蒙古和中国北部的草原，越冬地则在印度、尼泊尔和非洲部分地区。它拥有优雅的外形——纤细的脖颈、修长的双腿和美丽的羽毛——常被认为是鹤类中最优雅的物种之一。蓑羽鹤以其精妙的求偶舞而闻名，求偶时，雌雄蓑羽鹤会同步地舞动和鸣叫，呈现出一场美妙绝伦的视觉盛宴。",
    "image_url": "https://cn.bing.com/th?id=OHR.IndiaCranes_ZH-CN5871338482_1920x1080.webp",
    "main_text": "在世界自然保护联盟濒危物种红色名录中，蓑羽鹤被评估为无危物种。"
}
```

UpdataTime：2026-03-30 09:24:43
