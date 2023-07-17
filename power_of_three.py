#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'isPowerOfThree' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts INTEGER n as parameter.
#

def isPowerOfThree(n):
    # Write your code here
    # use recursion
    # need to separate out possible values of n
    
    # n can't be negative 
    if n <= 0:
        return False
    # if n is equal to one, then return True -> b/c 3^0 == 1. 
    elif n == 1:
        return True
    # otherwise n > 1 so either return False if it's not a multiple of 3, or recurse
    # again with the value n floor div'ed by 3. 
    # The HAPPY PATH is hopefully to push the value n to 1 which returns True,
    # or to push it to a value that isn't a multiple of 3 anymore.
    else:
        if n % 3 != 0:
            return False
        else:
            return isPowerOfThree(n // 3)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = isPowerOfThree(n)

    fptr.write(str(int(result)) + '\n')

    fptr.close()
