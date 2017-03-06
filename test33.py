# -*- coding:utf-8 -*-
"""畳み込み計算を行う"""

i_list = [0, 1, 2, 3, 5, 7, 11]  #入力
g_list = [32, 16, 8, 4, 2, 1, 0] #インパルス応答
o_list = [0, 0, 0, 0, 0, 0, 0]   #出力

for i in range(len(i_list)):
    for j in range(i+1):
        o_list[i] += i_list[j] * g_list[i-j]

print("入力 : ", end="")
print(i_list)
print("インパルス応答 : ", end="")
print(g_list)
print("出力 : ", end="")
print(o_list)
