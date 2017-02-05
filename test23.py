# -*- coding: utf-8 -*-

class TestClass:
    def __init__(self, code, name):
        self.code = code
        self.name = name

classes = []
classes.append(TestClass(1, u'テスト1'))
classes.append(TestClass(2, u'テスト2'))

for cls in classes:
    print "========== Class ============"
    print "code --> " + str(cls.code)
    print "name --> " + cls.name
