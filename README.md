# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![正在吃竹子的大熊猫，中国](https://cn.bing.com/th?id=OHR.PandaForest_ZH-CN0545156080_1920x1080.webp)
Today: [正在吃竹子的大熊猫，中国](https://cn.bing.com/th?id=OHR.PandaForest_ZH-CN0545156080_1920x1080.webp) - 走进熊猫世界

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
    "date": "2026-03-16",
    "headline": "走进熊猫世界",
    "title": "正在吃竹子的大熊猫，中国",
    "description": "凭借黑白相间的毛色与温顺的性格，大熊猫已成为全球保护的象征。每年的3月16日被定为国家熊猫日，以关注这一标志性物种及其面临的保护挑战。大熊猫原产于中国，由于栖息地破坏和低出生率，曾一度濒临灭绝。得益于全球保护努力，它们的数量正在缓慢回升，但仍需更多工作来保障其未来。",
    "image_url": "https://cn.bing.com/th?id=OHR.PandaForest_ZH-CN0545156080_1920x1080.webp",
    "main_text": "虽然属于食肉动物，大熊猫的食物几乎全是竹子。由于竹子的营养价值不高，它们每天需要花费数小时进食才能满足能量需求。"
}
```

UpdataTime：2026-03-16 09:09:55
