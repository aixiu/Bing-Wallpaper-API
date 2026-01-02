# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![威尼斯鸟瞰图, 意大利](https://cn.bing.com/th?id=OHR.VeniceView_ZH-CN3088407995_1920x1080.webp)
Today: [威尼斯鸟瞰图, 意大利](https://cn.bing.com/th?id=OHR.VeniceView_ZH-CN3088407995_1920x1080.webp) - 威尼斯的灵魂

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
    "date": "2026-01-02",
    "headline": "威尼斯的灵魂",
    "title": "威尼斯鸟瞰图, 意大利",
    "description": "从高空俯瞰威尼斯，宛如一幅迷人的水上画卷，但这座意大利瑰宝真正的魅力，藏在古老墙垣与曲折水巷之间。公元5世纪，它在潟湖中的一簇岛屿上诞生，由沼泽蜕变为海上霸主。中世纪时期，威尼斯成为连接欧洲与东方的重要贸易枢纽，财富与文化在此交织。如今，哥特式宫殿、文艺复兴艺术，以及圣马可大教堂、公爵宫、里亚托桥等地标，仍在诉说这座城市的辉煌历史。",
    "image_url": "https://cn.bing.com/th?id=OHR.VeniceView_ZH-CN3088407995_1920x1080.webp",
    "main_text": "威尼斯的灵魂，古老而迷人，由118座岛屿织成水上锦图，400余座桥梁将它们串联。纵横的运河如脉络般流淌，贡多拉与船只穿梭不止，宛若一场永恒的奇迹。"
}
```

UpdataTime：2026-01-02 08:40:14
