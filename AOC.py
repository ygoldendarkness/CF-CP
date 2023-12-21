import sys
from functools import lru_cache as cache
from collections import Counter, defaultdict, deque
import math
import bisect
import math
import copy
import itertools
from heapq import heappush, heappop
import json
import re
from copy import copy, deepcopy
import ast
def get_int(): return int(input())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()


class BreakOutException(Exception):
    pass

def f(n):
    a0 = 3849
    a1 = 34318
    a2 = 95133

    b0 = a0
    b1 = a1-a0
    b2 = a2-a1
    return b0 + b1*n + (n*(n-1)//2)*(b2-b1)


def main():
    lines = sys.stdin.read().splitlines()
    grid = [[c for c in line] for line in lines]
    m, n = len(grid), len(grid[0])
    ds = [(0,1),(1,0),(-1,0),(0,-1)]
    s = set()
    for r in range(m):
        for c in range(n):
            if grid[r][c] == "S":
                grid[r][c] = "."
                s.add((r, c, 0, 0))
                break
    for _ in range(65):
        ns = set()
        for tr, tc, r, c in s:
            for dr, dc in ds:
                nr, nc = r + dr, c + dc
                ntr, ntc = tr, tc
                if nr < 0:
                    nr += m
                    ntr = tr - 1
                if nc < 0:
                    nc += n
                    ntc = tc - 1
                if nr >= m:
                    nr -= m
                    ntr = tr + 1
                if nc >= n:
                    nc -= n
                    ntc = tc + 1
                if grid[nr][nc] == ".":
                    ns.add((ntr, ntc, nr, nc))

        s = ns
    print(len(s))
            

if __name__ == "__main__":
    main()
    print(f(26501365//131))


