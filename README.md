# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![菲莱神庙 (aka Temple of Isis), 阿斯旺, 埃及](https://cn.bing.com/th?id=OHR.TemplePhilae_ZH-CN1232015188_1920x1080.webp)
Today: [菲莱神庙 (aka Temple of Isis), 阿斯旺, 埃及](https://cn.bing.com/th?id=OHR.TemplePhilae_ZH-CN1232015188_1920x1080.webp) - 伊西斯女神的光辉照耀下

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
    "date": "2025-07-16",
    "headline": "伊西斯女神的光辉照耀下",
    "title": "菲莱神庙 (aka Temple of Isis), 阿斯旺, 埃及",
    "description": "菲莱神庙，常被称为伊西斯神庙，是埃及最迷人的古迹之一。它最初建在菲莱岛上，后来为避免被洪水淹没而迁至附近的阿吉勒基亚岛。这项迁移工程是20世纪60年代由联合国教科文组织发起的国际文物拯救项目，历时多年，搬运了逾4万块石块，才得以完整重建并保存这座古老神庙。如今，它坐落在尼罗河环绕的静谧之地，是乘船游览和探寻往昔的绝佳去处。",
    "image_url": "https://cn.bing.com/th?id=OHR.TemplePhilae_ZH-CN1232015188_1920x1080.webp",
    "main_text": "菲莱岛虽小，仅长约450米、宽不足150米，却自古以来便吸引着无数前来埃及的游客。因其秀美的景致，这座小岛素有“埃及明珠”之称。"
}
```

UpdataTime：2025-07-16 08:38:51
