#!/usr/bin/env python3.6
# -*- coding:utf-8 -*-

'a test module'

__author__='harry hujie'  

import sys

def test():
    args=sys.argv
    if len(args)==1:
        print('hello,world!')
    elif len(args)==2:
        print('hello,%s!' %args[1])
    else:
        print('too many arguments!')


if __name__ ==  '__main__':
    test()
#run python hello.py  -->hello world!
#run python hello.py hujie -->hello hujie!
