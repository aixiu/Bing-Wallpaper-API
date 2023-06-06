# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![The chalk cliffs of Étretat, Normandy, France](https://cn.bing.com/th?id=OHR.CliffsEtretat_ZH-CN1961838068_1920x1080.webp)
Today: [The chalk cliffs of Étretat, Normandy, France](https://cn.bing.com/th?id=OHR.CliffsEtretat_ZH-CN1961838068_1920x1080.webp) - 诺曼底登陆日

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
    "date": "2023-06-06",
    "headline": "诺曼底登陆日",
    "title": "The chalk cliffs of Étretat, Normandy, France",
    "description": "第二次世界大战期间，1944年6月6日，经过数月计划和无数次的拖延，盟军在法国诺曼底海滩登陆，诺曼底战役由此拉开序幕。这是历史上最雄心勃勃的军事袭击之一，为盟军战胜轴心国奠定了坚实基础。",
    "image_url": "https://cn.bing.com/th?id=OHR.CliffsEtretat_ZH-CN1961838068_1920x1080.webp",
    "main_text": "1927年，法国两位飞行员驾驶双翼飞机“白鸟”跨越大西洋，途经埃特尔塔之后，他们便神秘失踪了。埃特尔塔也因此闻名于世。"
}
```

UpdataTime：2023-06-06 02:03:37
