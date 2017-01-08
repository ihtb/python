# -*- coding: utf-8 -*-

import sys
input = sys.argv
print input[1]

flist = [0, 1]
i = 1

while flist[i] < int(input[1]):
	flist.append(flist[i] + flist[i-1])
	i += 1

print flist
