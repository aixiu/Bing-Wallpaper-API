# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![奔跑在诺曼底草地上的小狍，法国](https://cn.bing.com/th?id=OHR.Fawn_ZH-CN2172152960_1920x1080.webp)
Today: [奔跑在诺曼底草地上的小狍，法国](https://cn.bing.com/th?id=OHR.Fawn_ZH-CN2172152960_1920x1080.webp) - 这只小可爱在哪里?

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
    "date": "2023-06-19",
    "headline": "这只小可爱在哪里?",
    "title": "奔跑在诺曼底草地上的小狍，法国",
    "description": "獐子（Capreolus capreolus），也被称为狍子、西方狍子或欧洲狍子，是鹿的一种。该物种的雄性有时被称为 \"獐\"。它主要以草、叶、浆果和嫩芽为食。它特别喜欢非常年轻的、水分含量高的嫩草，即前一天下过雨的草。",
    "image_url": "https://cn.bing.com/th?id=OHR.Fawn_ZH-CN2172152960_1920x1080.webp",
    "main_text": "体格健壮的雄袍子鹿角长达20-25厘米，有两个或三个角，很少有四个角。"
}
```

UpdataTime：2023-06-19 01:53:09
