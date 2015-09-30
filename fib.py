#!/usr/bin/python

total = 0

for i in range(10):
  print ((i-1) + (i-2))
  if ((i-1) + (i-2)) / 2 == 0:
    total = total + ((i-1) + (i-2))

print (total)