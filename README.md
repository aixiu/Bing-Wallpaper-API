# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![冰山上天然形成的拱门, 南极洲](https://cn.bing.com/th?id=OHR.AntarcticArch_ZH-CN1622701432_1920x1080.webp)
Today: [冰山上天然形成的拱门, 南极洲](https://cn.bing.com/th?id=OHR.AntarcticArch_ZH-CN1622701432_1920x1080.webp) - 冰雪凝息之处

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
    "date": "2025-12-01",
    "headline": "冰雪凝息之处",
    "title": "冰山上天然形成的拱门, 南极洲",
    "description": "有些照片定格了自然的宏伟瞬间，而真正出色的作品更能揭示深层的故事：在一帧之中，力量与脆弱的微妙平衡，提醒我们地球的脆弱与伟大。今日这张展现南极冰山天然拱门的照片正是如此，它开启了关于宏伟、脆弱、环境与未来的对话。",
    "image_url": "https://cn.bing.com/th?id=OHR.AntarcticArch_ZH-CN1622701432_1920x1080.webp",
    "main_text": "《南极条约》将南极确立为和平与科学研究的保护区，最初由12个国家签署并生效。如今，已有50多个国家认可这一条约。它奠定了数十年来科学探索与成果的基石。"
}
```

UpdataTime：2025-12-01 08:42:52
