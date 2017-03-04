# -*- coding:utf-8 -*-

test_str_list = [u"abcde", u"fghij", u"klmno"]

for word in test_str_list:
    for char in word:
        print(char,end="")
    print("")
