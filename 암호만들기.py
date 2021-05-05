from itertools import combinations
import sys

sys.stdin = open('input.txt')
L,C = map(int,sys.stdin.readline().split())
char = list(map(str,sys.stdin.readline().split()))
char.sort()
vowels=['a','e','i','o','u']
result=[]
for password in combinations(char,L):
    count=0
    for i in password:
        if i in vowels:
            count+=1

    if 1<=count<=L-2:
        result.append(password)


for i in result:
    print(''.join(i))