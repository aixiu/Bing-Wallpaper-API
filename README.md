# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![贝弗利·韦斯特伍德，东约克郡，英格兰](https://cn.bing.com/th?id=OHR.BeverleyWestwood_ZH-CN3729041588_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [贝弗利·韦斯特伍德，东约克郡，英格兰](https://cn.bing.com/th?id=OHR.BeverleyWestwood_ZH-CN3729041588_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 阖家欢乐的一天

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
    "date": "2022-12-26",
    "headline": "阖家欢乐的一天",
    "title": "贝弗利·韦斯特伍德，东约克郡，英格兰",
    "description": "今天的照片拍摄于东约克郡黑磨坊附近的贝弗利·韦斯特伍德庄园，人们正在积雪的山坡上玩耍，欢度节礼日。传统上，节礼日是在圣诞节狂欢之后放松的一天。那么，节礼日（boxing day）的名字从何而来？对此有多种不同说法，但被广泛认可的说法是，在圣诞节过后的第一天，穷人们会收到“盒子（box）”，也就是圣诞节礼物。也许，我们今天也应该延续这个传统。当我们吃着圣诞节剩菜，听着余音缭绕的颂歌时，想想怎样才能给那些身处困境的人一点帮助呢?",
    "image_url": "https://cn.bing.com/th?id=OHR.BeverleyWestwood_ZH-CN3729041588_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "传统上，人们会在这个节日向贫困的人捐赠物品。"
}
```

UpdataTime：2022-12-26 01:47:44
