# https://www.acmicpc.net/problem/11728
import sys
from collections import deque

sys.stdin = open('input.txt')


def deq(shortlist, shortdeque, longdeque):
    result = []
    for i in shortlist:
        while True:
            if longdeque[0] < i:
                result.append(longdeque.popleft())
            else:
                result.append(shortdeque.popleft())
                break
    return result


N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
Atmp = deque(A)
Btmp = deque(B)
if len(A) < len(B):
    result = deq(A, Atmp, Btmp)
else:
    result = deq(B, Btmp, Atmp)

print(result)
