#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re

if __name__ == '__main__':
    s = list(input("Напечатайте предложение: ").split())
    c = input("Первый символ: ")
    b = input("Второй символ: ")

    for i,val in enumerate(s):
        if c in val: 
            print(val)
        elif b in val:
            print(val)


