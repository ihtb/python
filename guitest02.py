# -*- coding: utf-8 -*-

import wx

application = wx.App()

frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム")
frame.Show()

application.MainLoop()
