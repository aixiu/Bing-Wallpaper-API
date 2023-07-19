# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![敦煌月牙泉，甘肃省，中国](https://cn.bing.com/th?id=OHR.CrescentLake_ZH-CN8294493832_1920x1080.webp)
Today: [敦煌月牙泉，甘肃省，中国](https://cn.bing.com/th?id=OHR.CrescentLake_ZH-CN8294493832_1920x1080.webp) - 这片湖泊可不是海市蜃楼

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
    "date": "2023-07-19",
    "headline": "这片湖泊可不是海市蜃楼",
    "title": "敦煌月牙泉，甘肃省，中国",
    "description": "月牙泉位于中国甘肃省敦煌市附近，是隐藏在广袤戈壁滩上的一个摄人心魄的自然奇观。数百年来，这片因独特的月牙形状而闻名的绿洲，一直是一个重要的水源地。人们认为，月牙泉是风蚀形成的，其水源是地下泉水。由于附近有山脉遮挡，月牙泉才不会被该地的风沙所淹没。当地采取了许多保护措施，确保月牙泉不会干涸。游客不仅可以在湖上划船、骑骆驼在沙漠徜徉，还可以在附近的莫高窟欣赏古代佛教壁画及雕塑。",
    "image_url": "https://cn.bing.com/th?id=OHR.CrescentLake_ZH-CN8294493832_1920x1080.webp",
    "main_text": "自汉朝起，月牙泉就是“敦煌八景”之一。"
}
```

UpdataTime：2023-07-19 03:06:35
