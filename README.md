# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![一起迎接2023年](https://cn.bing.com/th?id=OHR.TheNationaDay_ZH-CN7631842209_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [一起迎接2023年](https://cn.bing.com/th?id=OHR.TheNationaDay_ZH-CN7631842209_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 和谁一起跨年？

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
    "date": "2022-12-31",
    "headline": "和谁一起跨年？",
    "title": "一起迎接2023年",
    "description": "每年公历1月1日，标志着新一年的到来，人们习惯将这一天称为“元旦”，俗称“公历年”、“阳历年”或“新历年”。在很多国家，有自己的新年，或是因习俗传统，或者是宗教性的，例如：中国春节，伊斯兰新年，泰米尔新年和犹太新年。",
    "image_url": "https://cn.bing.com/th?id=OHR.TheNationaDay_ZH-CN7631842209_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "到豪兰岛迎来新年时，基里巴斯莱恩群岛已是1月2日凌晨2点左右。"
}
```

UpdataTime：2022-12-31 01:45:40
