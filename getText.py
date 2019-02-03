import win32con

import win32clipboard as w


class GetText:
    #把图像识别出来的文字，保存到剪切板
    @staticmethod
    def getText():
        w.OpenClipboard()
        d = w.GetClipboardData(win32con.CF_UNICODETEXT)
        w.CloseClipboard()
        return d

    @classmethod
    def setText(cls,aString):

        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_UNICODETEXT,aString)
        w.CloseClipboard()


if __name__ == '__main__':

    GetText.setText('Hawkeye')
    GetText.getText()