# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![除夕夜的中国新年灯笼](https://cn.bing.com/th?id=OHR.ChineseNewYearEve2023_ZH-CN7188893388_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [除夕夜的中国新年灯笼](https://cn.bing.com/th?id=OHR.ChineseNewYearEve2023_ZH-CN7188893388_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 爆竹声中一岁除

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
    "date": "2023-01-21",
    "headline": "爆竹声中一岁除",
    "title": "除夕夜的中国新年灯笼",
    "description": "“除夕”是岁除之夜的意思，又称大年夜、除夕夜、除夜等，时值年尾的最后一个晚上。除夕自古就有守岁、团圆饭、贴年红、挂灯笼等习俗，经久不息。比如我们所熟知的贴年红年红，是春联、门神、窗花、年画、福字等过年时所贴的红色喜庆元素统称。过年贴年红（挥春），是中国民间由来已久的风俗，寄托了人们对幸福生活的向往，对美好未来的祝愿。除夕守岁也是年俗的重要活动之一，守岁之俗由来已久。守岁的民俗主要表现为所有房子都点燃岁火，合家欢聚，并守着“岁火”不让熄灭，等着辞旧迎新的时刻，迎接新年到来。",
    "image_url": "https://cn.bing.com/th?id=OHR.ChineseNewYearEve2023_ZH-CN7188893388_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "许多家庭的过年传统中除夕夜到大年初一屋里的灯都不关，要彻夜不灭，寓意来年前途光明。"
}
```

UpdataTime：2023-01-21 01:49:29
