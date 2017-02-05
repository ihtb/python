# -*- coding: utf-8 -*-

class Test_Class:

    def __init__(self, code, name):
        self.code = code
        self.name = name

classes = []
classes.append(Test_Class(1, u"Test_Class1"))
classes.append(Test_Class(2, u"Test_Class2"))

for cls in classes:
        print "======Class======="
        print "code :" + str(cls.code)
        print "name :" + str(cls.name)
