#!/usr/bin/env python

n=int(input())
num=list(map(int, input().split()))

mean=sum(num)/n
var=0
for i in num:
    var+=(i-mean)**2
var=var/n
std=round(var**0.5,1)
print(std)
