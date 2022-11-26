#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re

if __name__ == '__main__':
    s1 = input("Напечатайте предложение: ")
    s = list(s1.split(" "))
    k = []
    
    for i in s1:
        if i in s[0] and i in s[1] and i in s[2]: 
            if i not in k:
                k.append(i)
                
    print(k)
        
