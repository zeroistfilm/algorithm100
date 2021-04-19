# https://www.acmicpc.net/problem/1269
import sys

sys.stdin = open('input.txt')
N, M = map(int, sys.stdin.readline().split())
A = dict.fromkeys(list(map(int, sys.stdin.readline().split())))
B = dict.fromkeys(list(map(int, sys.stdin.readline().split())))

tmpAB=[]
for i in A:
    if not i in B:
        tmpAB.append(i)

tmpBA=[]
for i in B:
    if not i in A:
        tmpBA.append(i)

print(len(tmpAB)+len(tmpBA))