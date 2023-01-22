# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![春节的桃花和红灯笼](https://cn.bing.com/th?id=OHR.ChineseSpringFestival2023_ZH-CN7281854882_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [春节的桃花和红灯笼](https://cn.bing.com/th?id=OHR.ChineseSpringFestival2023_ZH-CN7281854882_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 春节快乐，兔年大吉！

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
    "date": "2023-01-22",
    "headline": "春节快乐，兔年大吉！",
    "title": "春节的桃花和红灯笼",
    "description": "兔年快乐！今天是农历新年的开始，我们迎来了兔年。兔子十二生肖中的第四种动物。中国的新年也称为春节，也是家庭团聚的传统日子。春节的起源蕴含着深邃的文化内涵，在传承发展中承载了丰厚的历史文化底蕴。在春节期间，全国各地均有举行各种庆贺新春活动，带有浓郁的各地地方特色。而从年初一开始便进入迎禧接福、拜祭神祖、祈求丰年主题。元日子时交年时刻，鞭炮齐响、烟花照天、辞旧岁、迎新年等各种庆贺新春活动达于高潮。年初一，人们都早早起来，穿上最漂亮的衣服，打扮得整整齐齐出门，恭祝新年大吉大利。",
    "image_url": "https://cn.bing.com/th?id=OHR.ChineseSpringFestival2023_ZH-CN7281854882_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "兔年出生的人被认为是聪明、甜美、快乐、安静和执着的。"
}
```

UpdataTime：2023-01-22 01:54:56
