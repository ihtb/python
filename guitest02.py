# -*- coding: utf-8 -*-

import wx

application = wx.App()

frame = wx.Frame(None, wx.ID_ANY, u"テストフレーム", size=(300,300), pos=(0,100))
frame.SetBackgroundColour("#000000")

r_panel = wx.Panel(frame, wx.ID_ANY, pos=(0,0), size=(80,300))
r_panel.SetBackgroundColour("#00ff00")

r_panel = wx.Panel(frame, wx.ID_ANY, pos=(80,0), size=(80,300))
r_panel.SetBackgroundColour("#0000ff")

r_panel = wx.Panel(frame, wx.ID_ANY, pos=(160,0), size=(80,300))
r_panel.SetBackgroundColour("#ff0000")

frame.Show()

application.MainLoop()
