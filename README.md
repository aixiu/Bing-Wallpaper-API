# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![中国春节传统汉字“福”](https://cn.bing.com/th?id=OHR.SpringFestivalY26_ZH-CN0228318064_1920x1080.webp)
Today: [中国春节传统汉字“福”](https://cn.bing.com/th?id=OHR.SpringFestivalY26_ZH-CN0228318064_1920x1080.webp) - 福气满满，马年大吉

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
    "date": "2026-02-16",
    "headline": "福气满满，马年大吉",
    "title": "中国春节传统汉字“福”",
    "description": "过年好！今天是中国民间最隆重最富有特色的传统节日之一。其实每年从腊八或小年开始，到元宵节，都称之为过年。春节期间，中国全国各地人们都举办着感恩祈福、阖家团聚、除旧布新、迎禧接福、祈求丰年为主要内容的活动。而中国农历新年也在世界各地掀起了“中国风”，春节庆祝活动内容丰富多彩，具有重要的历史、艺术和文化价值。",
    "image_url": "https://cn.bing.com/th?id=OHR.SpringFestivalY26_ZH-CN0228318064_1920x1080.webp",
    "main_text": "十二生肖的起源与动物崇拜有关。最早记载与现代相同的十二生肖的传世文献是东汉王充的《论衡》。"
}
```

UpdataTime：2026-02-16 16:58:03
