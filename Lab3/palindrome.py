#!/usr/bin/python

import sys

#str =  sys.argv

str = raw_input("Enter the word: ") #taking in word from command line

print str #test to show the word

#function to return true or false
def palindrome(n):
    return n == n[::-1]

returnString = palindrome(str)

print returnString
