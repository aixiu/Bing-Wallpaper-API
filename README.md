# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![地坛公园秋日美景，北京，中国](https://cn.bing.com/th?id=OHR.AutumnEquinoxY26_ZH-CN7957453091_1920x1080.webp)
Today: [地坛公园秋日美景，北京，中国](https://cn.bing.com/th?id=OHR.AutumnEquinoxY26_ZH-CN7957453091_1920x1080.webp) - 金秋平分，地坛染黄

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
    "date": "2026-09-23",
    "headline": "金秋平分，地坛染黄",
    "title": "地坛公园秋日美景，北京，中国",
    "description": "金色地毯通常只出现在童话世界里，但在金秋时节的北京，它们却铺展在你的脚下。地坛公园（方泽坛）著名的银杏大道汇聚了200多株历史悠久的银杏树。每当秋风掠过，数以万计的扇形金叶翩翩飘落，将这座古老的皇家坛庙铺垫成一片如梦似幻的金黄海洋。",
    "image_url": "https://cn.bing.com/th?id=OHR.AutumnEquinoxY26_ZH-CN7957453091_1920x1080.webp",
    "main_text": "秋分标志着昼夜平分，也预示着老北京最美丽的仲秋金色画卷正式展开。"
}
```

UpdataTime：2026-09-23 04:36:49
