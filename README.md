# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![巴伐利亚森林酒窖，德国](https://cn.bing.com/th?id=OHR.FranconianWineCellar_ZH-CN8234719750_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [巴伐利亚森林酒窖，德国](https://cn.bing.com/th?id=OHR.FranconianWineCellar_ZH-CN8234719750_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 隐藏在树林中

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
    "date": "2023-04-24",
    "headline": "隐藏在树林中",
    "title": "巴伐利亚森林酒窖，德国",
    "description": "德国可能因啤酒在世界享誉盛名，但这个丰饶的国家也以其强大的酿酒业而闻名。随着葡萄酒产量的增加，酒的储存需求也随之而来。酒窖通常需要低温黑暗的环境，所以图中这个位于巴伐利亚森林的酒窖位置十分完美。",
    "image_url": "https://cn.bing.com/th?id=OHR.FranconianWineCellar_ZH-CN8234719750_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "巴伐利亚森林是一片树木繁茂的低山区，位于德国巴伐利亚，长约100公里。"
}
```

UpdataTime：2023-04-24 01:44:04
