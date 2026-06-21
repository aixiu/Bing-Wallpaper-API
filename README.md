# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![企鹅爸爸正在检查蛋的情况](https://cn.bing.com/th?id=OHR.EggDad_ZH-CN6045387630_1920x1080.webp)
Today: [企鹅爸爸正在检查蛋的情况](https://cn.bing.com/th?id=OHR.EggDad_ZH-CN6045387630_1920x1080.webp) - 鸟类好爸爸

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
    "date": "2026-06-21",
    "headline": "鸟类好爸爸",
    "title": "企鹅爸爸正在检查蛋的情况",
    "description": "六月的第三个星期日是父亲节——一个感谢那些默默守护、悉心照料孩子成长的长辈们的日子。在世界各地，父亲的角色可以呈现出令人意想不到的非凡形式。",
    "image_url": "https://cn.bing.com/th?id=OHR.EggDad_ZH-CN6045387630_1920x1080.webp",
    "main_text": "对海马而言，雄性会将受精卵放入自己的育儿袋中，并在孵化前为它们提供氧气、养分和全方位的保护。"
}
```

UpdataTime：2026-06-21 05:10:59
