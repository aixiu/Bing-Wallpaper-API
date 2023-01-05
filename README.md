# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![白鼬 (Mustela erminea), 上巴伐利亚，德国](https://cn.bing.com/th?id=OHR.HermelinSchnee_ZH-CN8839783506_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [白鼬 (Mustela erminea), 上巴伐利亚，德国](https://cn.bing.com/th?id=OHR.HermelinSchnee_ZH-CN8839783506_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 软萌雪中小精灵

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
    "date": "2023-01-05",
    "headline": "软萌雪中小精灵",
    "title": "白鼬 (Mustela erminea), 上巴伐利亚，德国",
    "description": "白鼬（Mustela erminea），又称欧亚白鼬、白令亚貂和貂，是一种原产于欧亚大陆和北美洲北部的鼬科动物。多栖息于沼泽、林地、农田，食肉动物，主食为鸟类和小型哺乳动物。白鼬是一种软萌可爱的动物，它的体长在170~330毫米，体重为25~116克，身材非常娇小。随着季节变化，白鼬的毛发颜色会发生变化。到了冬季，就像它的名字一样，会变为一身漂亮的纯白色皮毛，哦对了，尾巴尖还有一点点黑色，这是无冬历夏始终如一的。",
    "image_url": "https://cn.bing.com/th?id=OHR.HermelinSchnee_ZH-CN8839783506_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "外型上，春夏季节黄鼠狼和白鼬确实有几分相似，但是到了冬天，两者区分就非常明显了。"
}
```

UpdataTime：2023-01-05 01:52:02
