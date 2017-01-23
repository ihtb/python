# -*- coding:utf-8 -*-

import wx

application = wx.App()
frame = wx.Frame(None, wx.ID_ANY, "テストフレーム", size=(300,200))

panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour("#AFAFAF")

s_text_1 = wx.StaticText(panel, wx.ID_ANY, "テキスト1")
s_text_2 = wx.StaticText(panel, wx.ID_ANY, "テキスト2")
s_text_3 = wx.StaticText(panel, wx.ID_ANY, "テキスト3")
s_text_4 = wx.StaticText(panel, wx.ID_ANY, "テキスト4")
s_text_5 = wx.StaticText(panel, wx.ID_ANY, "テキスト5")

layout = wx.BoxSizer(wx.VERTICAL)
layout.Add(s_text_1)
layout.Add(s_text_2)
layout.Add(s_text_3)
layout.Add(s_text_4)
layout.Add(s_text_5)

panel.SetSizer(layout)

frame.Show()
application.MainLoop()
