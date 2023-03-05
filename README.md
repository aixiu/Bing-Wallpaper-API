# Bing Wallpaper

> 数据缓存开始时间: 2022/11/1

![袋鼠妈妈和宝宝](https://cn.bing.com/th?id=OHR.HuggingKanga_ZH-CN1045131695_1920x1080.jpg&rf=LaDigue_1920x1080.jpg)
Today: [袋鼠妈妈和宝宝](https://cn.bing.com/th?id=OHR.HuggingKanga_ZH-CN1045131695_1920x1080.jpg&rf=LaDigue_1920x1080.jpg) - 来自妈妈的拥抱和爱

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
    "date": "2023-03-05",
    "headline": "来自妈妈的拥抱和爱",
    "title": "袋鼠妈妈和宝宝",
    "description": "袋鼠是一种属于袋鼠目的有袋动物，主要分布于澳大利亚大陆和巴布亚新几内亚的部分地区。其中，有些种类为澳大利亚独有。不同种类的袋鼠在澳大利亚各种不同的自然环境中生活，从凉性气候的雨林和沙漠平原到热带地区。袋鼠是跳得最高最远的哺乳动物。所有雌性袋鼠都长有前开的育儿袋， “幼崽”或小袋鼠就在育儿袋里被抚养长大，直到它们能在外部世界生存。",
    "image_url": "https://cn.bing.com/th?id=OHR.HuggingKanga_ZH-CN1045131695_1920x1080.jpg&rf=LaDigue_1920x1080.jpg",
    "main_text": "据传说，“Kangaroo”是袋鼠的英文名，源自于澳洲原住民Guugu Yimidhirr:“gangurru”，意思是指“不知道”。而这一切其实只是一场误会..."
}
```

UpdataTime：2023-03-05 02:12:49
