# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![大堡礁的航拍图，澳大利亚](https://cn.bing.com/th?id=OHR.ReefAwareness_ZH-CN8840949729_1920x1080.webp)
Today: [大堡礁的航拍图，澳大利亚](https://cn.bing.com/th?id=OHR.ReefAwareness_ZH-CN8840949729_1920x1080.webp) - 一望无际的湛蓝

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
    "date": "2023-06-01",
    "headline": "一望无际的湛蓝",
    "title": "大堡礁的航拍图，澳大利亚",
    "description": "澳大利亚的大堡礁是世界上最大的珊瑚礁，沿澳大利亚海岸蔓延1430英里。许多海洋生物生活在这个珊瑚礁生态系统中，包括鲸鱼、海豚、海龟以及1500多种鱼类。遗憾的是，这处世界自然遗产正受到气候变化、污染和过度捕捞的威胁。每年的六月一日是世界珊瑚礁日，旨在让人们意识到海洋珊瑚礁系统的脆弱性和重要性，提醒我们每一个人、每一个组织和企业保护这些宝藏、维持自然的平衡。",
    "image_url": "https://cn.bing.com/th?id=OHR.ReefAwareness_ZH-CN8840949729_1920x1080.webp",
    "main_text": "大堡礁岛上有215种鸟类在此筑巢或栖息。"
}
```

UpdataTime：2023-06-01 02:23:07
