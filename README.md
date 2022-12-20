# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![维也纳美景宫的圣诞市场，奥地利](https://cn.bing.com/th?id=OHR.PalaceBelvedere_ZH-CN1818163173_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [维也纳美景宫的圣诞市场，奥地利](https://cn.bing.com/th?id=OHR.PalaceBelvedere_ZH-CN1818163173_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 圣诞节的倒影

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
    "date": "2022-12-20",
    "headline": "圣诞节的倒影",
    "title": "维也纳美景宫的圣诞市场，奥地利",
    "description": "圣诞集市有三个吸引游客的点：在欧洲风景如画的城镇村庄里举行，可以买到有趣的礼物（通常是手工制作的），还可以品尝到热红酒和当地美食。圣诞集市是欧洲最古老的降临节活动之一。",
    "image_url": "https://cn.bing.com/th?id=OHR.PalaceBelvedere_ZH-CN1818163173_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "美景宫是一座位于奥地利维也纳的历史建筑群，由两座巴洛克风格的宫殿（上美景宫和下美景宫）、橘园和宫殿马厩组成。"
}
```

UpdataTime：2022-12-20 01:48:36
