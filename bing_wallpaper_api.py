# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2026/10/01 17:50:57

# 必应每日一图接口

import json
import os
import time
from datetime import datetime
from urllib.parse import urljoin

import requests


class BingWallpaper:
    def __init__(self) -> None:
        self.url = "https://cn.bing.com/"
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.26"
        self.headers = {"User-Agent": self.user_agent}

    def get_hp_model(self):
        """
        直接请求 /hp/api/model，返回首页 _model 的完整 JSON。
        等价于原来从首页 HTML 里抠出来的 var _model = {...};，
        但不用正则，直接 json.loads，稳定得多。
        """
        try:
            model_url = f"{self.url}hp/api/model"
            resp = requests.get(url=model_url, headers=self.headers, timeout=15)
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            print(f"get_hp_model:{e}")
            return None

    def get_bing_img(self):
        data = self.get_hp_model()
        if not data or not data.get("MediaContents"):
            print("未获取到 /hp/api/model 数据")
            return None

        ImageContent = data["MediaContents"][0]["ImageContent"]
        Image = ImageContent.get("Image", {})

        # Image.Url       -> ts1.tc.mm.bing.net 上的 webp 原图，适合程序展示（体积小）
        # Image.Wallpaper -> cn.bing.com 上的 jpg 壁纸版，适合用户下载（兼容性好）
        image_url_webp = urljoin(self.url, Image.get("Url", ""))
        image_url_jpg = urljoin(self.url, Image.get("Wallpaper", Image.get("Url", "")))

        # 从 Image.Url 提取图片 ID，用于拼 UHD 4K 地址
        # 例：https://ts1.tc.mm.bing.net/th?id=OHR.OlmstedPoint_ZH-CN4182671075_1920x1080.webp
        #     -> OHR.OlmstedPoint_ZH-CN4182671075
        img_id = ""
        url = Image.get("Url", "")
        if "?id=" in url:
            # 先剥掉 ?id= 前缀，再剥掉 &rf=... 参数，最后切掉尺寸后缀
            img_id = url.split("?id=")[-1].split("&")[0].rsplit("_", 1)[0]

        if img_id:
            image_url_uhd = f"https://cn.bing.com/th?id={img_id}_UHD.jpg"
        else:
            # 提取失败时回退到 jpg 地址，保证字段不为空
            image_url_uhd = image_url_jpg

        return {
            "date": datetime.now().strftime(r"%Y-%m-%d"),
            "headline": ImageContent.get("Headline", ""),
            "title": ImageContent.get("Title", ""),
            "description": ImageContent.get("Description", ""),
            "image_url": image_url_webp,  # webp，程序展示用
            "image_url_jpg": image_url_jpg,  # jpg 1920x1200，用户下载用（带水印）
            "image_url_uhd": image_url_uhd,  # jpg 4K，用户下载用（新增）
            "main_text": (ImageContent.get("QuickFact") or {}).get("MainText", ""),
        }

    def get_now_time(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # 读取 2022/11/01.json 文件，生成 README.md 文件
    def buildReadme(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            json_data = json.load(f)

        json_w = json.dumps(json_data, ensure_ascii=False, indent=4)
        head_img = json_data.get("image_url", "")
        head_title = json_data.get("title", "")
        head_headline = json_data.get("headline", "")

        with open("./README.md", mode="w", encoding="utf-8") as fp:
            fp.write("# Bing Wallpaper\n\n")
            fp.write("> 数据缓存开始时间: 2022/11/1\n\n")
            fp.write(
                f"![{head_title}]({head_img})\nToday: [{head_title}]({head_img}) - {head_headline}\n\n"
            )
            fp.write("## 接口\n\n")
            fp.write("接口地址：\n\n")
            fp.write("```html\n")
            fp.write("https://aixiu.github.io/Bing-Wallpaper-API/\n")
            fp.write("```\n\n")
            fp.write("请求方式：\n\n")
            fp.write("```html\n")
            fp.write(
                "https://aixiu.github.io/Bing-Wallpaper-API/<year>/<month>/<day>.json\n"
            )
            fp.write("```\n\n")
            fp.write("参数说明\n\n")
            fp.write("| 参数 | 类型 | 说明 |\n")
            fp.write("| - | - | - |\n")
            fp.write("| year | str | 4位年份, 例如：2022 |\n")
            fp.write("| month | str | 2位月份, 例如：02、12 |\n")
            fp.write("| day | str | 2位日期, 例如：02、25 |\n\n")
            fp.write("例如\n\n")
            fp.write(
                "[https://aixiu.github.io/Bing-Wallpaper-API/2022/11/01.json](https://aixiu.github.io/Bing-Wallpaper-API/2022/11/01.json)\n\n"
            )
            fp.write("返回数据\n\n")
            fp.write("```json\n")
            fp.write(f"{json_w}\n")
            fp.write("```\n\n")
            fp.write(f"UpdateTime：{self.get_now_time()}\n")

    def main(self):
        response = self.get_bing_img()
        if not response:
            print("本次未获取到数据，跳过")
            return

        date = datetime.strptime(response.get("date"), r"%Y-%m-%d")
        dirname = date.strftime(r"%Y/%m")
        name = date.strftime(r"%d")
        filename = f"{dirname}/{name}.json"

        # 创建一个文件夹，保存所有的图片
        if not os.path.exists(filename):
            os.makedirs(dirname, exist_ok=True)
            # makedirs(path,[mode])作用:创建递归的目录树,可以是相对路径或者绝对路径.默认的模式也是0777,如果子目录创建失败或者已经存在就会抛出一个OSError的异常,exist_ok：只有在目录不存在时创建目录，目录已存在时不会抛出异常。

        with open(filename, "w", encoding="utf-8") as fp:
            fp.write(
                json.dumps(response, ensure_ascii=False, indent=4)
            )  # 用于将字典转换为字符串格式

        self.buildReadme(filename)


if __name__ == "__main__":
    data = BingWallpaper()  # 实例化对象
    data.main()


"""
strftime是转换为特定格式输出，而strptime是将一个（时间）字符串解析为时间的一个类型对象。一个是按照想要的格式，去转换。重点是格式！另外一个不管什么格式，我只要把特定的时间字符串转成时间类型即可！
https://blog.csdn.net/weixin_42139375/article/details/81105479

参考了：
https://github.com/mouday/wallpaper-database
https://www.cnblogs.com/wilson-wu/p/8386598.html
https://blog.csdn.net/mouday/article/details/127526950
"""
