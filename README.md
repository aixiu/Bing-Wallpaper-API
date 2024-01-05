# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![巴伐利亚阿尔卑斯山脉，德国](https://cn.bing.com/th?id=OHR.AlpsReflecting_ZH-CN4036320440_1920x1080.webp)
Today: [巴伐利亚阿尔卑斯山脉，德国](https://cn.bing.com/th?id=OHR.AlpsReflecting_ZH-CN4036320440_1920x1080.webp) - 是现实还是童话？

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
    "date": "2024-01-05",
    "headline": "是现实还是童话？",
    "title": "巴伐利亚阿尔卑斯山脉，德国",
    "description": "冬日的晴空笼罩着阿尔卑斯山白雪皑皑的山景，雄伟的山峰倒映在冰湖光滑的镜面上。四周白雪覆盖的树木见证了这一刻的宁静与祥和，只有脚踏积雪发出轻柔的嘎吱声可以偶尔打破这种宁静。阳光洒向湖光山色，令人心旷神怡。",
    "image_url": "https://cn.bing.com/th?id=OHR.AlpsReflecting_ZH-CN4036320440_1920x1080.webp",
    "main_text": "楚格峰是巴伐利亚阿尔卑斯山乃至整个德国的最高峰。它位于韦特施泰因山脉的西部，海拔2962米，具有高阿尔卑斯山的特征，并有两个小冰川。"
}
```

UpdataTime：2024-01-05 01:32:19
