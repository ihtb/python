# -*- coding:utf-8 -*-

import sys

print("表示したいフィボナッチ数列の上限を入力してください:")
max_num = int(sys.stdin.readline())

fibnacci_list = [0,1]

print(fibnacci_list[0], end="")

while fibnacci_list[-1] < max_num:
    print(", ", end="")
    print(fibnacci_list[-1], end="")
    fibnacci_list.append(fibnacci_list[-2] + fibnacci_list[-1])
print("")
print("表示が完了しました。")
print("作成したフィボナッチ数列のリストを表示します。")
print(fibnacci_list)
