# -*- coding: utf-8 -*-

import sys
input = sys.argv
print input[1]

flist = [0, 1]
i = 2

while i < 10:
	flist.append(flist[i - 1] + flist[i - 2])
	if flist[i] > input[1]:
		break
	i += 1

print flist
