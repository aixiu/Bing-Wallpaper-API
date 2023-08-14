# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![叶片上的小壁虎](https://cn.bing.com/th?id=OHR.GeckoLeaf_ZH-CN9908456174_1920x1080.webp)
Today: [叶片上的小壁虎](https://cn.bing.com/th?id=OHR.GeckoLeaf_ZH-CN9908456174_1920x1080.webp) - 躲猫猫，我看见你了!

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
    "date": "2023-08-14",
    "headline": "躲猫猫，我看见你了!",
    "title": "叶片上的小壁虎",
    "description": "当你试图吸引人们关注世界蜥蜴日这项活动时，你不会想要用吉拉毒蜥、巨蜥，或者更常见的、但仍不讨喜的鬣蜥作为开场白。不，你想要的是一只可爱的小壁虎，就像我们在这张照片中看到的那样。壁虎有1500多种，大小不一，与其他蜥蜴不同的是，它们可以通过发声吸引配偶、威吓敌人和进行各种社交互动。",
    "image_url": "https://cn.bing.com/th?id=OHR.GeckoLeaf_ZH-CN9908456174_1920x1080.webp",
    "main_text": "斐济冠状鬣蜥是一种蜥蜴，在20世纪80年代的电影《蓝色泻湖》拍摄期间被发现。"
}
```

UpdataTime：2023-08-14 01:19:53
