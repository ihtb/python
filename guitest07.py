# -*- coding:utf-8 -*-

import wx

# ******************************
# Rootパネルクラス
# ******************************
class Root_class:
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, u"レイアウトテスト", size=(300. 300))

# ******************************
# sub1パネルクラス
# ******************************
class Sub1_class:

# ******************************
# sub2パネルクラス
# ******************************
class Sub2_class:

# ******************************
# sub3パネルクラス
# ******************************
class Sub3_class:

# ******************************
# アプリケーション起動
# ******************************
if __name__ == "__main__"
    applicaiton = wx.App()
    frame = Root_frame()
    frame.Show()
    application.MainLoop()
