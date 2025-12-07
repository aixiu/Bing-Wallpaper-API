# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![雪中的故宫，中国北京](https://cn.bing.com/th?id=OHR.TheGreatSnowY25_ZH-CN2448918230_1920x1080.webp)
Today: [雪中的故宫，中国北京](https://cn.bing.com/th?id=OHR.TheGreatSnowY25_ZH-CN2448918230_1920x1080.webp) - 雪落下的声音

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
    "date": "2025-12-07",
    "headline": "雪落下的声音",
    "title": "雪中的故宫，中国北京",
    "description": "今天是中国传统二十四节气中的大雪节气。大雪的到来预示着气温将逐渐降低，冬季降水量也将增加。大雪期间，中国大部分地区已进入严冬，北方部分地区的气温甚至会降至零度以下。北方大地呈现出“万里冰封”的壮丽景象，而南方则展现出“雪花飘舞，万物银装素裹”的迷人景色。",
    "image_url": "https://cn.bing.com/th?id=OHR.TheGreatSnowY25_ZH-CN2448918230_1920x1080.webp",
    "main_text": "紫禁城是世界上规模最大、保存最完好的古代木构建筑群之一。"
}
```

UpdataTime：2025-12-07 08:33:47
