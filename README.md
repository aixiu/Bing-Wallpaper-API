# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![吕贝克的霍尔斯滕门，德国](https://cn.bing.com/th?id=OHR.LuebeckCityGate_ZH-CN4618826141_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [吕贝克的霍尔斯滕门，德国](https://cn.bing.com/th?id=OHR.LuebeckCityGate_ZH-CN4618826141_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 纪念硬币上的著名建筑

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
    "date": "2023-03-01",
    "headline": "纪念硬币上的著名建筑",
    "title": "吕贝克的霍尔斯滕门，德国",
    "description": "霍尔斯滕门是一座城门，标志着汉萨同盟城市吕贝克旧中心的西部边界。 砖砌哥特式建筑建于1464年，是吕贝克中世纪城市防御工事的遗迹之一，也是现存的两座城门之一，另一座是城堡门 (Burgtor)。 它以其两个圆形的塔楼和拱形入口而闻名，今天被视为这座城市的象征。",
    "image_url": "https://cn.bing.com/th?id=OHR.LuebeckCityGate_ZH-CN4618826141_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "自1987年以来，它与吕贝克老城中心 (Altstadt) 一起被联合国教科文组织列为世界遗产。"
}
```

UpdataTime：2023-03-01 02:08:07
