# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![万圣节南瓜灯](https://cn.bing.com/th?id=OHR.HalloweenCuteAI_ZH-CN1079713117_1920x1080.webp)
Today: [万圣节南瓜灯](https://cn.bing.com/th?id=OHR.HalloweenCuteAI_ZH-CN1079713117_1920x1080.webp) - 恶灵们只想玩个开心。

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
    "date": "2023-10-31",
    "headline": "恶灵们只想玩个开心。",
    "title": "万圣节南瓜灯",
    "description": "万圣节来了！当你今晚外出时，很有可能会看到一个发光的南瓜，它的名字是“jack-o'-lantern”（南瓜灯）！这个名字源于一则爱尔兰民间传说，故事的主人公是一个名叫吝啬鬼杰克的骗子，他会提着一个挖空了的芜菁做成的灯笼四处游荡。另外，南瓜雕刻也起源于爱尔兰。最初，这种雕刻可怕的面孔和复杂图案的万圣节活动是用芜菁和马铃薯完成的。当爱尔兰人移民到北美时，他们发现南瓜产量很大，而且比其他蔬菜更易于雕刻，于是就改用了南瓜。",
    "image_url": "https://cn.bing.com/th?id=OHR.HalloweenCuteAI_ZH-CN1079713117_1920x1080.webp",
    "main_text": "万圣节南瓜灯起源于一则爱尔兰传说，故事的主人公名叫“吝啬鬼杰克”。"
}
```

UpdataTime：2023-10-31 01:28:06
