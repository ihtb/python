# -*- coding:utf-8 -*-
"""ユーザーの選んだ数値に応じて、ランダムに文字列を表示する"""

import random

def Int_Input():
    """コマンドラインからの入力の値を1~9の範囲内の整数を返す"""
    while True:
        num = input("1から9の好きな数字を入力してください : ")
        if num.isdigit():
            num = int(num)
            if num < 1 or num > 9:
                print("入力する整数は指定した範囲内に収めてください！")
            else:
                print("あなたが入力したのは", num, "ですね")
                return int(num)
        else:
            print("整数を入力してください!")

def Out_Rand_Str(num):
    Omikuji_text_list = ["最高の人生", "火星と金星が10の交わり、それを尊ぶと吉", "怨敵を見る", "贖罪は夜明け前におこなうべし", "他者からの憐憫を気に留めてはならない", "本質的な白い球体の夢に囚われる", "10番目の世界に飛ばされる", "塔を平地に作ってはならない", "災厄が訪れる。鏡を西に配すると吉"]
    print(Omikuji_text_list[num-1])

Out_Rand_Str(Int_Input())
