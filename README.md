# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![英国诺福克海滩上的灰海豹幼崽](https://cn.bing.com/th?id=OHR.HelloSeal_ZH-CN1064568368_1920x1080.webp)
Today: [英国诺福克海滩上的灰海豹幼崽](https://cn.bing.com/th?id=OHR.HelloSeal_ZH-CN1064568368_1920x1080.webp) - 欢迎来到这个世界！

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
    "date": "2023-11-21",
    "headline": "欢迎来到这个世界！",
    "title": "英国诺福克海滩上的灰海豹幼崽",
    "description": "如果你此时去英国诺福克海滩度假，大概率会看到刚出生的灰海豹幼崽。每年的11月初至1月初，约有3,000只灰海豹幼崽在英国的诺福克海滩上出生，使该地区成为英国最重要的灰海豹繁殖地之一。相比之下，美国海岸的灰海豹幼崽出生时间略晚。海豹妈妈会在海滩上悉心喂养幼崽三周，在这期间，幼崽每天增重约4.5磅！喂养期结束后，小海豹们还不能立刻下水。它们会待在海滩上，直到苍白的皮毛变成斑驳的灰色，才会前往大海，学会自己捕猎。",
    "image_url": "https://cn.bing.com/th?id=OHR.HelloSeal_ZH-CN1064568368_1920x1080.webp",
    "main_text": "海豹幼崽第一年的存活率因地区及其自身条件而异。据估计，有的地区的海豹幼崽存活率在80%到85%之间，有的地区则低于50%。导致海豹幼崽死亡的主要原因是进食困难导致的饥饿。"
}
```

UpdataTime：2023-11-21 01:35:18
