# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![南京夫子庙的春节许愿牌，江苏省，中国](https://cn.bing.com/th?id=OHR.SpringFestival25Y_ZH-CN6133182159_1920x1080.webp)
Today: [南京夫子庙的春节许愿牌，江苏省，中国](https://cn.bing.com/th?id=OHR.SpringFestival25Y_ZH-CN6133182159_1920x1080.webp) - 春节快乐！

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
    "date": "2025-01-29",
    "headline": "春节快乐！",
    "title": "南京夫子庙的春节许愿牌，江苏省，中国",
    "description": "春节，是中国民间最隆重也最富有特色的传统节日之一。春节期间的民俗众多，活动内容也是丰富多彩，且具有重要的历史、艺术和文化价值。其中逛庙会、赏灯会，更是春节最具特色的民俗活动之一。",
    "image_url": "https://cn.bing.com/th?id=OHR.SpringFestival25Y_ZH-CN6133182159_1920x1080.webp",
    "main_text": "夫子庙饮食文化源远流长，传统食品和风味小吃不下200种。经过历代改进融合已经形成了以“秦淮八绝”为代表的秦淮风味小吃。"
}
```

UpdataTime：2025-01-29 08:29:52
