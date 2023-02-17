# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![栖息在红袋鼠爪枝干上的艾氏煌蜂鸟](https://cn.bing.com/th?id=OHR.BirdcountAllen_ZH-CN4029022734_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [栖息在红袋鼠爪枝干上的艾氏煌蜂鸟](https://cn.bing.com/th?id=OHR.BirdcountAllen_ZH-CN4029022734_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - “后院鸟类统计”活动开始了！

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
    "date": "2023-02-17",
    "headline": "“后院鸟类统计”活动开始了！",
    "title": "栖息在红袋鼠爪枝干上的艾氏煌蜂鸟",
    "description": "让我们尽点绵薄之力，帮助科学家更多地了解全球鸟类数量吧。“后院鸟类统计”是一项为期四天的年度活动，起源于美国，目前已推广至全世界。该活动鼓励观鸟者留意当地的鸟类，并通过eBird平台上传报告。例如，如果你在墨西哥中南部，你可能会看到一只在这里过冬的艾氏煌蜂鸟。活动的统计结果将被汇总并公布在网上，供科学家和有兴趣的网友查阅。据估计，全球有10000种鸟类。在这个激动人心的周末，带上你的设备，出门观鸟吧！",
    "image_url": "https://cn.bing.com/th?id=OHR.BirdcountAllen_ZH-CN4029022734_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "科学家估计全球约有10000种鸟类。"
}
```

UpdataTime：2023-02-17 02:00:17
