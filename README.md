# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![黄山的冬天，中国](https://cn.bing.com/th?id=OHR.MountainDayChina_ZH-CN6894169616_1920x1080.webp)
Today: [黄山的冬天，中国](https://cn.bing.com/th?id=OHR.MountainDayChina_ZH-CN6894169616_1920x1080.webp) - 想看看黄山的全貌吗？

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
    "date": "2023-12-11",
    "headline": "想看看黄山的全貌吗？",
    "title": "黄山的冬天，中国",
    "description": "12月11日是国际山岳日，这个特殊的节日是联合国大会在2003年设立的。今年节日的主题是“恢复山区生态系统”，与“联合国生态系统恢复十年”计划相呼应。",
    "image_url": "https://cn.bing.com/th?id=OHR.MountainDayChina_ZH-CN6894169616_1920x1080.webp",
    "main_text": "黄山山脉有72座山峰，包括36座大峰和36座小峰。"
}
```

UpdataTime：2023-12-11 01:33:39
