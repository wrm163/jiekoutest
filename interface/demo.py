'''
安装requests模块：模拟浏览器，jmeter发送http请求
'''
import requests
# 得到百度的所有返回数据
response = requests.get(url="http://www.baidu.com")
#先把 response进行编码utf-8
response.encoding = "utf-8"
#提取数据
data = response.text
#打印出来，写到 html页面里
f = open("百度.html","w+",encoding="utf-8")
f.write(data)