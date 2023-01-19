#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    for i in range(1,len(arr)):
        temp = arr[i]
        j = i-1
        if arr[j]>temp:
            while j>=0 and arr[j]>temp:
                arr[j+1] = arr[j]
                print(" ".join([str(i) for i in arr]))
                j-=1
            arr[j+1] = temp
            print(" ".join([str(i) for i in arr]))
            
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
