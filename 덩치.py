import sys

def isBiggerThenMe(me,other):
    if me[0]<other[0] and me[1]<other[1]:
        return True
    else:
        return False

sys.stdin= open('input.txt')

N = int(sys.stdin.readline())
people=[]

for i in range(N):
    weight, height = map(int, sys.stdin.readline().split())
    people.append((weight, height))

result =[]
for pi in people:
    rank = 1
    for pj in people:
        if not pi==pj:
            rank += isBiggerThenMe(pi,pj)
    result.append(rank)
print(*result, sep=' ')



