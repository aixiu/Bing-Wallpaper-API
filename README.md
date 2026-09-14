# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![红绿金刚鹦鹉](https://cn.bing.com/th?id=OHR.RedMacawsFlight_ZH-CN5045822113_1920x1080.webp)
Today: [红绿金刚鹦鹉](https://cn.bing.com/th?id=OHR.RedMacawsFlight_ZH-CN5045822113_1920x1080.webp) - 最炫者生存

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
    "date": "2026-09-14",
    "headline": "最炫者生存",
    "title": "红绿金刚鹦鹉",
    "description": "进化偶尔也会偏爱繁复华丽。看看这些红绿金刚鹦鹉：它们拥有猩红色羽毛、鲜绿色翅膀和蓝色飞羽。它们生活在南美洲热带地区，日常活动以不易从地面察觉的方式将果实、种子与土壤联系在一起。",
    "image_url": "https://cn.bing.com/th?id=OHR.RedMacawsFlight_ZH-CN5045822113_1920x1080.webp",
    "main_text": "大型金刚鹦鹉可产生数百磅每平方英寸的咬合压力，远高于普通人类，因而能轻松咬开坚硬的坚果和种子。"
}
```

UpdataTime：2026-09-14 20:16:22
