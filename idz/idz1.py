#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re

if __name__ == '__main__':
    s = list(input("Напечатайте предложение: ").split())
    c = input("Первый символ: ")
    b = input("Второй символ: ")


    for i in range(len(s)):
        if(c in s[i]): 
            print(s[i])
        elif(b in s[i]):
            print(s[i])


