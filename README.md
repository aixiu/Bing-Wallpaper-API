# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![岛屿灰狐，海峡群岛国家公园，美国加利福尼亚州](https://cn.bing.com/th?id=OHR.EarthDayFox_ZH-CN7926350207_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [岛屿灰狐，海峡群岛国家公园，美国加利福尼亚州](https://cn.bing.com/th?id=OHR.EarthDayFox_ZH-CN7926350207_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 国家公园中狡猾的常住居民

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
    "date": "2023-04-22",
    "headline": "国家公园中狡猾的常住居民",
    "title": "岛屿灰狐，海峡群岛国家公园，美国加利福尼亚州",
    "description": "今天是地球日，这正是庆祝地球生物丰富多样性和广阔生命之美的绝佳机会。有些动物的活动范围几乎覆盖全球，而另一些动物的栖息地却很狭窄。今日图片的岛屿灰狐是南加州海峡群岛特有的本土物种。在南加州海峡群岛的八个岛屿中，有六个都能找到它们的身影，其中每个岛屿都有一个独特的灰狐亚种。截至2021年，世界上的岛屿灰狐只有不到10000只。但归功于保护组织的圈养繁殖和种群恢复计划，岛屿灰狐的数量正在增加。当我们迎来国家公园周时，请记住这些公园在保护地球和野生动物方面有着至关重要的作用。",
    "image_url": "https://cn.bing.com/th?id=OHR.EarthDayFox_ZH-CN7926350207_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "岛屿灰狐在当地海峡岛民的精神生活中发挥了重要作用。它们很可能已被半驯化为宠物，用来制作皮草，或是有其他用处，比如防治害虫等。"
}
```

UpdataTime：2023-04-22 01:40:33
