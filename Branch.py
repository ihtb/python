# -*- coding:utf-8 -*-
"""条件分岐のまとめ"""

def Branch_If(num):
    if num > 5:
        print("この変数は5以上です")
    elif num == 5:
        print("この変数は5です")
    else:
        print("この変数は5未満です")

a = 10
b = 5
c = 0
print("a =", a)
print("b =", b)
print("c =", c)

separate = "********************"
print(separate)
print("aの判定")
Branch_If(a)
print(separate)
print("bの判定")
Branch_If(b)
print(separate)
print("cの判定")
Branch_If(c)
