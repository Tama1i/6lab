#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re

if __name__ == '__main__':
   s = input("Напечатайте предложение: ")
   a = input("введите букву ")
   i = 0

   while s[i] != ".":
       if s[i] == "и":
           c = i
       i += 1
   o = s[:c] + a + s[c:]
   print(o)
        
