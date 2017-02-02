# -*- coding: utf-8 -*-

class Test:
    
    # スタティックメソッド
    @staticmethod
    def plus(x, y):
        return x + y

# インスタンス化しない
print Test.plus(1, 2)

# インスタンス化する
test = Test()
print test.plus(2, 3)
