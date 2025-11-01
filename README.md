# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![岚山缤纷的枫叶与竹林, 京都, 日本](https://cn.bing.com/th?id=OHR.KyotoMaple_ZH-CN4730358356_1920x1080.webp)
Today: [岚山缤纷的枫叶与竹林, 京都, 日本](https://cn.bing.com/th?id=OHR.KyotoMaple_ZH-CN4730358356_1920x1080.webp) - 竹林吐纳清气，枫叶绚烂如火

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
    "date": "2025-11-01",
    "headline": "竹林吐纳清气，枫叶绚烂如火",
    "title": "岚山缤纷的枫叶与竹林, 京都, 日本",
    "description": "今日，我们前往京都岚山地区，这里以迷人的四季风光闻名于世。此处，鲜艳的日本红枫与静谧的竹林交织出色彩与宁静的和谐画卷。这些以纤细深裂叶片著称的枫树，每逢秋日便幻化成炽烈的红、橙、金三色，吸引着全球游客纷至沓来。它们不仅因绝美姿态备受推崇，更承载着象征优雅、平和与生命无常的文化意蕴。",
    "image_url": "https://cn.bing.com/th?id=OHR.KyotoMaple_ZH-CN4730358356_1920x1080.webp",
    "main_text": "岚山在四月初和十一月下半月最有吸引力（也最繁忙），此时樱花和秋色通常达到顶峰。"
}
```

UpdataTime：2025-11-01 16:29:51
