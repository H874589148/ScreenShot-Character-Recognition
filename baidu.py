# file:         baidu.py
# project:      ScreenShot-Character-Recognition
# version:      Python 3.4.1
# Author:       Hawkeye
# File Created: Sunday,3rd Feb 2019 08:50:03 am
# Last Modified:Sunday,3rd Feb 2019 15:04:06 pm
# ━━━━━神兽出没━━━━━━
# 　　　┏┓　　　┏┓
# 　　┏┛┻━━━┛┻┓
# 　　┃　　　　　　　┃
# 　　┃　　　━　　　┃
# 　　┃　┳┛　┗┳　┃
# 　　┃　　　　　　　┃
# 　　┃　　　┻　　　┃
# 　　┃　　　　　　　┃
# 　　┗━┓　　　┏━┛Code is far away from bug with the animal protecting
# 　　　　┃　　　┃    神兽保佑,代码无bug
# 　　　　┃　　　┃
# 　　　　┃　　　┗━━━┓
# 　　　　┃　　　　　　　┣┓
# 　　　　┃　　　　　　　┏┛
# 　　　　┗┓┓┏━┳┓┏┛
# 　　　　　┃┫┫　┃┫┫
# 　　　　　┗┻┛　┗┻┛
#
# ━━━━━━感觉萌萌哒━━━━━━

import configparser # 配置文件模块 读写配置文件

from aip import AipOcr # 文字识别模块

class BaiDuAPI(object):
    #特殊 构造函数 初始化函数
    def __init__(self,filePath):
        target = configparser.ConfigParser()
        target.read(filePath,encoding='utf-8-sig')
        app_id = target.get('工单密码','APP_ID')
        api_key = target.get('工单密码', 'API_KEY')
        secret_key = target.get('工单密码', 'SECRET_KEY')

        self.client = AipOcr(app_id,api_key,secret_key)

    def picture2Text(self,filePath):
        # 读取图片
        images = self.getPicture(filePath)
        texts = self.client.basicGeneral(images)
        allTexts = ''
        for word in texts['words_result']:
            allTexts = allTexts +word.get('words','')
        return allTexts
        #print(texts)

    def getPicture(self,filePath):
        with open(filePath,'rb') as fp:
            return fp.read()

if __name__ == '__main__':
    #第一种调用方式
    #BaiDuAPI.abc(BaiDuAPI(),666)
    #第二种调用方式
    baiduapi = BaiDuAPI('passwd.ini')
    print(baiduapi.picture2Text('grabImage.png'))
    #baiduapi.asd()
    #BaiDuAPI()
    #""" 你的 APPID AK SK """
    #APP_ID = '你的 App ID'
    #API_KEY = '你的 Api Key'
    #SECRET_KEY = '你的 Secret Key'

    #client = AipOcr(APP_ID, API_KEY, SECRET_KEY)