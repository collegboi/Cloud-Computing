#!/usr/bin/python

import sys

#str =  sys.argv

str = raw_input("Some input please: ") # or`input("Some...`

print str

def palindrome(n):
    return n == n[::-1]

returnString = palindrome(str)

print returnString
