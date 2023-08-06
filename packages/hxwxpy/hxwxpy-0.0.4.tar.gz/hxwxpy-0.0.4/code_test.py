"""
    作者：mldsh
    日期：2022年09月22日09:21
    使用工具：PyCharm
"""
import re

# print(snow)
# print(uid)
#
# url = "https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh#zh/en/send_url%20%E8%A6%81%E6%B1%82%E6%98%AF%E4%B8%80%E4%B8%AA%20url%EF%BC%8C%E5%BF%85%E9%A1%BB%E4%BB%A5%20https%20%E6%88%96%E8%80%85%20http%20%E5%BC%80%E5%A4%B4%E7%9A%84%E3%80%82%E5%AE%8C%E6%95%B4%E7%9A%84%E8%BF%9E%E6%8E%A5"
# regular = re.compile(r'[a-zA-Z]+://[^\s]*[.com|.cn]')
# result = re.findall(regular, url)
# print(result)

from hxwxpy import api_sendtext


api = api_sendtext.SendText()
api.bot_send_text()