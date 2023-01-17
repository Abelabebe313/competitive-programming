#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    swap = 0
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0,len(a)-1):
            if a[i] > a[i+1]:
                sorted = False
                a[i],a[i+1] = a[i+1], a[i]
                swap += 1
       
        
    print("Array is sorted in", swap, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])
    return

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
