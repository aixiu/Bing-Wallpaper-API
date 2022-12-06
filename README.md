# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![大沼泽国家公园里的一只大白鹭，美国佛罗里达州](https://cn.bing.com/th?id=OHR.GreatEgret_ZH-CN4088261519_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [大沼泽国家公园里的一只大白鹭，美国佛罗里达州](https://cn.bing.com/th?id=OHR.GreatEgret_ZH-CN4088261519_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 白鹭亮羽

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
    "date": "2022-12-06",
    "headline": "白鹭亮羽",
    "title": "大沼泽国家公园里的一只大白鹭，美国佛罗里达州",
    "description": "今天是佛罗里达州的大沼泽国家公园成立75周年。该公园建于1947年，旨在保护脆弱的生态系统，覆盖了大沼泽湿地面积的20%。尽管有公园管理局的保护，在人类活动干扰之下，大沼泽的生态还是受到了严重影响，尤其是当地的淡水资源。",
    "image_url": "https://cn.bing.com/th?id=OHR.GreatEgret_ZH-CN4088261519_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "已知年龄最大的白鹭发现于俄亥俄州，当时是22岁10个月。"
}
```

UpdataTime：2022-12-06 01:51:28
