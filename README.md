# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![巢中的乌林鸮, 芬兰](https://cn.bing.com/th?id=OHR.LaplandOwl_ZH-CN6070251232_1920x1080.webp)
Today: [巢中的乌林鸮, 芬兰](https://cn.bing.com/th?id=OHR.LaplandOwl_ZH-CN6070251232_1920x1080.webp) - 这是谁的家？

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
    "date": "2025-08-03",
    "headline": "这是谁的家？",
    "title": "巢中的乌林鸮, 芬兰",
    "description": "作为夜空中的无声猎手，猫头鹰是动物王国中最迷人的动物之一。它们能够将头部旋转多达270度，再加上无声的飞行和卓越的夜视能力，充分展现了其非凡的适应性。全球已知有200多种猫头鹰，它们在维护生态平衡中发挥着关键作用，并深深融入人类的文化传统。每年的8月4日是国际猫头鹰意识日，这一天不仅是对它们在自然界中重要角色的致敬，也是提醒人们关注它们所面临威胁的重要时刻。",
    "image_url": "https://cn.bing.com/th?id=OHR.LaplandOwl_ZH-CN6070251232_1920x1080.webp",
    "main_text": "乌林鸮体型庞大，因而需要定期进食，在冬季，它们每天要捕食多达7只田鼠大小的小型哺乳动物。"
}
```

UpdataTime：2025-08-03 16:35:33
