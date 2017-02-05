# -*- coding: utf-8 -*-

class Base(object):
    def test_method(self, msg):
        print "Base : {}".format(msg)

class New(Base):
    def test_method(self, msg):
       print "New : {}" .format(msg)
       super(New, self).test_method(msg)

new = New()
new.test_method("Hello!")
