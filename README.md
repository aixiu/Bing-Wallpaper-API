# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![大白鹭，匈牙利](https://cn.bing.com/th?id=OHR.WhiteEgret_ZH-CN4425921150_1920x1080.webp)
Today: [大白鹭，匈牙利](https://cn.bing.com/th?id=OHR.WhiteEgret_ZH-CN4425921150_1920x1080.webp) - 这只白鹭毫无遗憾

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
    "date": "2025-08-28",
    "headline": "这只白鹭毫无遗憾",
    "title": "大白鹭，匈牙利",
    "description": "今天让我们来认识一下大白鹭吧。它们分布在美洲、亚洲、非洲和欧洲部分地区，经常在湿地、潮滩和平静的溪流中涉水。它们耐心而精准，会一动不动地站上几分钟，等待着最佳时机发动闪电般的攻击。鱼类是它们的主要猎物，但也捕食青蛙、爬行动物，甚至小型哺乳动物。大白鹭广泛分布在世界各地。在中国见于东北、河北、江苏、云南、广东、海南、台湾等地。栖息于河川、海滨、沼泽湿地或水田中。性颇机警，见人即飞去。白天多单独寻觅食物，在食物丰富的区域内，也成小群活动。",
    "image_url": "https://cn.bing.com/th?id=OHR.WhiteEgret_ZH-CN4425921150_1920x1080.webp",
    "main_text": "大白鹭于1758年由瑞典自然学家卡尔·林奈在《自然系统》第十版中正式描述，其学名为Ardea alba。"
}
```

UpdataTime：2025-08-28 08:34:27
