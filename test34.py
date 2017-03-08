# -*- coding:utf-8 -*-

""" 関数内で変数を変更した場合のテスト """

def Increment(in_num):
    in_num += 1
    print("インクリメント完了")

out_num = 0
print(out_num)
Increment(out_num)
print(out_num)
