#!/usr/bin/env python

n=int(input())
num=list(map(int, input().split()))
weight=list(map(int, input().split()))
p=0
for i,j in zip(num,weight):
    p+=i*j
result=round(p/sum(weight),1)
print(result)
