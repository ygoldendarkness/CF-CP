from functools import lru_cache as cache
from collections import Counter, defaultdict
import math
import bisect
from heapq import *
# from sortedcontainers import SortedSet, SortedList, SortedDict

import sys
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()

def main():
    testcases = get_int()
    for tc in range(testcases):
        n = get_int()
        t = get_string()
        print(solve(n, t))

def solve(n, t):
    t = list(t)
    result = 0
    for num in range(1, n+1):
        cur = num
        while cur <= n:
            if t[cur-1] == "0":
                t[cur-1] = "2"
                result += num
            if t[cur-1] == "1":
                break
            cur += num
    return result


        
            
            
            

if __name__ == "__main__":
    main()

