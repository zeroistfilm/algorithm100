# https://www.acmicpc.net/problem/11720
import sys

sys.stdin = open('input.txt', 'r')
N = int(sys.stdin.readline())
M = sys.stdin.readline()
result=0
for i in range(N):
    result +=(int(M[i]))
print(result)