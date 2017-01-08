# -*- coding: shift-jis -*-

import sys

args = sys.argv
print "Input1 : " + args[1]

def factorial(num1):
	answer = 1
	for i in range(1, num1 + 1):
		answer *= i
	return answer

print ""
print "*******************"
print factorial(int(args[1]))
print "*******************"
