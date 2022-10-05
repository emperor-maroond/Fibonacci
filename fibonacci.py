#!/usr/bin/python

import numpy as np
import sys

try:
    val = float(sys.argv[1])
except ValueError as err:
    print('Not a Number or No Value Entered!')
    exit(0)

n1 = 1; n2 = 1
n = 1

if val > 2:
    while n < val:
        tmp = n1 + n2
        n1 = n2
        n2 = tmp
        n += 1
    print(n1)

elif val==1 or val==2:
     print(1)
elif val==0:
    print(0)
elif val<0:
    print('Please Enter a Valid Number!')