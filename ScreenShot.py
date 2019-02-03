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

# 导入模块
# 标准库模块
import sys
import time

#第三方扩展模块
import keyboard
from PIL import ImageGrab

#自己写的模块
from baidu import BaiDuAPI

def screenShot(x:int)->int:
    #监测键盘事件  开始键
    if keyboard.wait('Ctrl+Alt+a') == None:
        if keyboard.wait('enter') == None:
            time.sleep(0.51)    #暂停0.01秒
            #获取剪切板里面的照片
            im = ImageGrab.grabclipboard()
            im.save('grabImage.png')

if __name__ == '__main__':

    baiduapi = BaiDuAPI('passwd.ini')
    for _ in range(sys.maxsize):

        screenShot(6)

        print(baiduapi.picture2Text('grabImage.png'))
