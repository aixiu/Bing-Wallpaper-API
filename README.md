# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![梯田鸟瞰图，元阳，中国](https://th.bing.com/th?id=OHR.YuanyangChina_ZH-CN7360249295_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [梯田鸟瞰图，元阳，中国](https://th.bing.com/th?id=OHR.YuanyangChina_ZH-CN7360249295_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 彩虹般的风景

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
    "date": "2023-03-07",
    "headline": "彩虹般的风景",
    "title": "梯田鸟瞰图，元阳，中国",
    "description": "元阳梯田风景壮丽，已被联合国教科文组织列为世界文化遗产。这些壮观的梯田位于中国云南省，总面积约17万亩，有1300多年的历史。成片的梯田沿着哀牢山缓缓延伸，色彩丰富、景观壮丽，是摄影爱好者的“天堂”。元阳县远离城市的喧嚣，游客们可以放心享受这里的宁静。在这里，依然可以感受到原住民哈尼族延续了数百年的文化，绚丽多彩的服饰、传统的房屋，以及在田间劳作的水牛，它们共同构成了一幅极其动人的彩绘版画。",
    "image_url": "https://th.bing.com/th?id=OHR.YuanyangChina_ZH-CN7360249295_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "元阳梯田位于红河哈尼梯田的核心区域，已有1300多年的历史。2013年，元阳梯田被联合国教科文组织列为世界文化遗产。"
}
```

UpdataTime：2023-03-07 02:04:52
