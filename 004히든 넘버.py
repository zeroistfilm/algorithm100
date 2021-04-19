# https://www.acmicpc.net/problem/8595

import sys

sys.stdin = open('input.txt')

N = sys.stdin.readline()
M = sys.stdin.readline()
tmp = ""
result=0
for i in M:  # 30~39
    if 48 <= int(ord(i)) <= 57:
        tmp += i
    else:
        if tmp != "":
            result+=int(tmp)
        tmp = ""

print(result)