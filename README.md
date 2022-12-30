# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![白沙漠中的岩石，埃及](https://cn.bing.com/th?id=OHR.ChalkRock_ZH-CN2893565655_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [白沙漠中的岩石，埃及](https://cn.bing.com/th?id=OHR.ChalkRock_ZH-CN2893565655_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 这些雪永远不会融化

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
    "date": "2022-12-30",
    "headline": "这些雪永远不会融化",
    "title": "白沙漠中的岩石，埃及",
    "description": "这是沙漠中的雪吗？其实不是。这里是埃及的白沙漠，当地丰富的白垩岩、石灰岩、石英岩以及长年累月的风化作用造就了这些白色的沙子和形状奇特的岩石，白沙漠也因此得名。游客们蜂拥而至，来欣赏这些大自然的奇观。白沙国家公园距离开罗约5小时车程，这里不仅有白沙和怪石，还有多种濒危保护动物。",
    "image_url": "https://cn.bing.com/th?id=OHR.ChalkRock_ZH-CN2893565655_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "这片白沙看起来像覆盖在沙漠上的雪。这些白色的石英晶体在许多地方都打造出了这种独特的景致。"
}
```

UpdataTime：2022-12-30 01:48:57
