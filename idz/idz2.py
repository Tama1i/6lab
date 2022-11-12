#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re

if __name__ == '__main__':
    s = input("Напечатайте предложение: ")

    b = s.replace("чя", "ча")
    a = b.replace("щя", "ща")
    print(a)

   
