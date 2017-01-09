# -*- coding: utf-8 -*-

import sys

input = sys.argv

target = 100
initial = int(input[1])
Co = 0.5

output = [initial]
i = 0
while i <10:
	output.append((target - output[i]) * Co + output[i])
	i += 1

for data in output:
	print data
