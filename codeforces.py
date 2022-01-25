from functools import lru_cache as cache
from collections import Counter
import math
from heapq import *

import sys
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()

def main():
	testcases = get_int()
	for i in range(testcases):
		n, k = get_ints()
		s = get_string()
		print(solve(s, k, n))


def solve(s, k, n):
	counter = Counter()
	for l in s:
		counter[l] += 1
	
	
if __name__ == "__main__":
	main()