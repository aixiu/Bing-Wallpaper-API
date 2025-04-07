# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![美洲海狸, Moran, 怀俄明州, 美国](https://cn.bing.com/th?id=OHR.BeaverDay_ZH-CN2889563041_1920x1080.webp)
Today: [美洲海狸, Moran, 怀俄明州, 美国](https://cn.bing.com/th?id=OHR.BeaverDay_ZH-CN2889563041_1920x1080.webp) - 你好，海狸！

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
    "date": "2025-04-07",
    "headline": "你好，海狸！",
    "title": "美洲海狸, Moran, 怀俄明州, 美国",
    "description": "今天，我们迎来国际海狸日！该节日由湿地与野生海狸组织于2009 年设立，旨在强调海狸在生态系统中的重要作用。海狸是了不起的动物，以筑坝技能闻名，它们建造的湿地为众多物种提供了栖息地。作为北美最大的啮齿动物，成年海狸体长可达3 英尺，还不包括其独特的扁平尾巴。它们的门牙不断生长，并因覆盖着厚厚的橙色珐琅质而呈现独特的色泽。海狸啃食树木不仅能保持牙齿健康，还能帮助调节环境。难怪它们坚固的门牙让它们成为大自然最优秀的工程师之一。",
    "image_url": "https://cn.bing.com/th?id=OHR.BeaverDay_ZH-CN2889563041_1920x1080.webp",
    "main_text": "海狸主要在夜间活动，并且是出色的游泳健将，能在水下潜伏长达 15 分钟。"
}
```

UpdataTime：2025-04-07 02:02:46
