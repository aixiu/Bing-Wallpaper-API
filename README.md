# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![正在吃竹子的大熊猫，中国成都](https://cn.bing.com/th?id=OHR.BambooPanda_ZH-CN8455481760_1920x1080.webp)
Today: [正在吃竹子的大熊猫，中国成都](https://cn.bing.com/th?id=OHR.BambooPanda_ZH-CN8455481760_1920x1080.webp) - 被竹子包围了

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
    "date": "2024-03-16",
    "headline": "被竹子包围了",
    "title": "正在吃竹子的大熊猫，中国成都",
    "description": "你喜欢观看熊猫“滚滚”那令人轻松视频吗？这些啃食竹子的动物有着独特的黑白外衣和俏皮的举止，多年来一直吸引着人们的目光。以至于在1961年，世界自然基金会将这种动物作为其标志性标识。但你知道有一天是用来庆祝它们的吗？3月16日是国家熊猫日，旨在提高人们保护大熊猫和生态环境的意识。大熊猫的自然栖息地遭到破坏，这意味着它们变得十分脆弱；为了遏制这种威胁，中国建立了大约50个保护区。幸运的是，2016年，大熊猫从濒危物种重新归类为易危物种了。不过，现如今野外大熊猫数量不足2000只，保护大熊猫的战斗远未结束。",
    "image_url": "https://cn.bing.com/th?id=OHR.BambooPanda_ZH-CN8455481760_1920x1080.webp",
    "main_text": "大熊猫只有两个亚种，即四川亚种和秦岭亚种。它们的主要栖息地是中国四川、陕西和甘肃的山区。"
}
```

UpdataTime：2024-03-16 01:19:02
