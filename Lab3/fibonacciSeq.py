#!/usr/bin/python

counter = 0
value = 0




def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
  return a
