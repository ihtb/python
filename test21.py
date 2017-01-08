# -*- coding: shift-jis -*-

import sys

def factorial(num):
	if num != 0:
		return num * factorial(num - 1)
	else:
		return 1

args = sys.argv
print "Input1 : " + args[1]

print ""
print "*******************"
print factorial(int(args[1]))
print "*******************"
