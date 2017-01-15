# -*- coding:utf-8 -*-

Ilist = [1, 10, 100, 110, 200]
Glist = [100, 50, 25, 12, 6]
anslist = range(5)

tmplist = range(5)

for i in range(5):
    anslist[i] = Ilist[i] * Glist[4-i]

answer = 0
for i in range(5):
    answer += anslist[i]

print Ilist
print Glist
print answer
