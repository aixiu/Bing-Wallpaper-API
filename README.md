# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![曼哈顿中央公园的秋天，纽约，美国](https://cn.bing.com/th?id=OHR.CentralParkAutumn_ZH-CN2757358246_1920x1080.webp)
Today: [曼哈顿中央公园的秋天，纽约，美国](https://cn.bing.com/th?id=OHR.CentralParkAutumn_ZH-CN2757358246_1920x1080.webp) - 邂逅秋日的林荫道

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
    "date": "2024-10-18",
    "headline": "邂逅秋日的林荫道",
    "title": "曼哈顿中央公园的秋天，纽约，美国",
    "description": "每年秋天，纽约中央公园18000棵树木中的许多树，都会染上黄色、红色和橙色的色调。秋天是中央公园出镜率最高的季节之一，它为《当哈利遇见莎莉》和《头发》等电影提供了标志性的拍摄背景。树木不仅通过温度来感知冬天的到来，还通过日出和日落时光线照射到树叶上的角度来感知。由于纽约高楼林立，光线、阴影和温度的独特相互作用往往导致公园里的秋叶比城市里的其他地方来得晚。",
    "image_url": "https://cn.bing.com/th?id=OHR.CentralParkAutumn_ZH-CN2757358246_1920x1080.webp",
    "main_text": "中央公园林荫大道是拥有世界上最大的美国榆树丛的地方之一。高耸的榆树遮天蔽日，是中央公园最具标志性和辨识度的景观之一。"
}
```

UpdataTime：2024-10-18 02:42:43
