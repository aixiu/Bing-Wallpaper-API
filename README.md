# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![座头鲸](https://cn.bing.com/th?id=OHR.PlayfulHumpback_ZH-CN2241016258_1920x1080.webp)
Today: [座头鲸](https://cn.bing.com/th?id=OHR.PlayfulHumpback_ZH-CN2241016258_1920x1080.webp) - 座头鲸唱歌的地方

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
    "date": "2023-06-08",
    "headline": "座头鲸唱歌的地方",
    "title": "座头鲸",
    "description": "海洋覆盖了地球表面70%以上的面积，因此海洋在调节地球气候和生态系统方面发挥着至关重要的作用。这些浩瀚的海洋支撑着巨大的海洋生物生态系统，美丽的座头鲸也在其中。座头鲸因其“唱歌”而闻名，研究认为这可能是一种孤独的表现。好消息是，随着商业捕鲸活动的结束，鲸鱼的数量有所上升，鲸鱼们也就不太需要再唱孤独之歌了。",
    "image_url": "https://cn.bing.com/th?id=OHR.PlayfulHumpback_ZH-CN2241016258_1920x1080.webp",
    "main_text": "雄性座头鲸被称为公鲸，而雌性则被称为母鲸。"
}
```

UpdataTime：2023-06-08 02:01:37
