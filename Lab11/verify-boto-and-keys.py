#AKIAIBKC3KC4HZNSXFIA:6DLuJWrLRu6RsxwqP8jheSo4pcTy4ZH6U+7k2gk

import requests
import sys
import boto
import pkg_resources

res = requests.get('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')

result = res.text

mylist = result.split(':')


print 'KEY ID = ' + mylist[0];
print 'ACCESS KEY = ' + mylist[1];
print 'Boto Version = ' + boto.Version