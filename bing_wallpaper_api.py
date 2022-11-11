# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/11/01 08:33:23

# 必应每日一图接口

import json
import os
import re
import time
from datetime import datetime
from urllib.parse import urljoin

import requests


class BingWallpaper():
    def __init__(self) -> None:
        self.url = 'https://cn.bing.com/'
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.26'
        self.headers = {'User-Agent': self.user_agent}
        
        
    def get_json_data(self, fa='js', idx=0, n=1, mkt='zh-CN'):
        try:
            json_url = f'{self.url}HPImageArchive.aspx?format={fa}&idx={idx}&n={n}&mkt={mkt}'
            if fa == 'xml':
                data = requests.get(url=json_url, headers=self.headers).text
                return data
            else:                
                data = requests.get(url=json_url, headers=self.headers).json()
                return data
        except Exception as e:
            print(f'get_json_data:{e}')
            
    def get_bing_img(self):
        response = requests.get(self.url, headers=self.headers)
        response.encoding = response.apparent_encoding
        try:
            ret = re.search(r"var _model =({.*?});", response.text)
        except:
            return None
        
        # print(ret.group())  # 默认返回匹配的整个字符串，同分组0，且且无法处理成pythoy格式
        data = json.loads(ret.group(1))   # 是将字符串转化为字典
        
        ImageContent = data['MediaContents'][0]['ImageContent']
        
        return {
            'date': datetime.now().strftime(r'%Y-%m-%d'),
            'headline': ImageContent['Headline'],
            'title': ImageContent['Title'],
            'description': ImageContent['Description'],            
            'image_url': urljoin(self.url, ImageContent['Image']['Url']), # 连接两个参数的url, 将第二个参数中缺的部分用第一个参数的补齐,如果第二个有完整的路径，则以第二个为主
            'main_text': ImageContent['QuickFact']['MainText']
        }
        
    def get_now_time(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        
    # 读取 2022/11/01.json 文件，生成 README.md 文件
    def buildReadme(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            json_w = json.dumps(json_data, ensure_ascii=False, indent=4)
            
            head_img = json_data['image_url']            
            head_title = json_data['title']
            head_headline = json_data['headline']
            
            with open('./README.md', mode='w', encoding='utf-8') as fp:
                fp.write("# Bing Wallpaper\n\n")
                fp.write("> 数据缓存开始时间: 2022/11/1\n\n")
                fp.write(f"![{head_title}]({head_img})\nToday: [{head_title}]({head_img}) - { head_headline}\n\n")                
                fp.write("## 接口\n\n")
                fp.write("接口地址：\n\n")
                fp.write("```html\n")
                fp.write("https://aixiu.github.io/Bing-Wallpaper-API/\n")
                fp.write("```\n\n")
                fp.write("请求方式：\n\n")
                fp.write("```html\n")
                fp.write("https://aixiu.github.io/Bing-Wallpaper-API/<year>/<month>/<day>.json\n")
                fp.write("```\n\n")
                fp.write("参数说明\n\n")
                fp.write("| 参数 | 类型 | 说明 |\n")
                fp.write("| - | - | - |\n")
                fp.write("| year | str | 4位年份, 例如：2022 |\n")
                fp.write("| year | str | 4位年份, 例如：2022 |\n")
                fp.write("| day | str | 2位日期, 例如：02、25 |\n\n")
                fp.write("例如\n\n")
                fp.write("[https://aixiu.github.io/Bing-Wallpaper-API/2022/10/27.json](https://aixiu.github.io/Bing-Wallpaper-API/2022/10/27.json)\n\n")
                fp.write("返回数据\n\n")
                fp.write("```json\n")
                fp.write(f"{json_w}\n")
                fp.write("```\n\n")
                fp.write(f"UpdataTime：{data.get_now_time()}\n")
                
    def main(self):
        response = data.get_bing_img()
        date = datetime.strptime(response.get('date'), r'%Y-%m-%d')
        dirname = date.strftime(r'%Y/%m')
        name = date.strftime(r'%d')
        filename = f'{dirname}/{name}.json'
        
        # 创建一个文件夹，保存所有的图片
        if not os.path.exists(filename):
            os.makedirs(dirname, exist_ok=True)
            # makedirs(path,[mode])作用:创建递归的目录树,可以是相对路径或者绝对路径.默认的模式也是0777,如果子目录创建失败或者已经存在就会抛出一个OSError的异常,exist_ok：只有在目录不存在时创建目录，目录已存在时不会抛出异常。
            
        with open(filename, 'w', encoding='utf-8') as fp:
            fp.write(json.dumps(response, ensure_ascii=False, indent=4))  # 用于将字典转换为字符串格式
        
        data.buildReadme(filename)
            
        
if __name__ == '__main__':
    data = BingWallpaper()  # 实例化对象
    data.main()
    
    
    
    
'''
strftime是转换为特定格式输出，而strptime是将一个（时间）字符串解析为时间的一个类型对象。一个是按照想要的格式，去转换。重点是格式！另外一个不管什么格式，我只要把特定的时间字符串转成时间类型即可！
https://blog.csdn.net/weixin_42139375/article/details/81105479

参考了：
https://github.com/mouday/wallpaper-database
https://www.cnblogs.com/wilson-wu/p/8386598.html
https://blog.csdn.net/mouday/article/details/127526950
'''
    

