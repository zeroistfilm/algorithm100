import sys
from itertools import permutations


def calculate(num1, opers, num2):
    if opers =='+':
        return num1+num2
    elif opers =='-':
        return num1-num2
    elif opers =='*':
        return num1*num2
    elif opers =='/':
        if num1<0 and num2>0:
            return -(-num1)//num2
        return num1/num2


minimun = 10**9
maximun =-10**9
sys.stdin = open('input.txt')
N = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().split()))
opers = list(map(int, sys.stdin.readline().split()))
opersChar = []

for i in range(len(opers)):
    for j in range(opers[i]):
        if i == 0:
            opersChar.append('+')
        elif i == 1:
            opersChar.append('-')
        elif i == 2:
            opersChar.append('*')
        elif i == 3:
            opersChar.append('/')

for opercombi in permutations(opersChar,N-1):
    tmpExpression=[]
    for i in range(len(opercombi)):
        tmpExpression.append(numList[i])
        tmpExpression.append(opercombi[i])
    tmpExpression.append(numList[-1])
    # print(tmpExpression)
    #앞에서부터 계산
    resultNumber = calculate(tmpExpression[0],tmpExpression[1],tmpExpression[2])

    for i in range(3, len(tmpExpression),2):
        resultNumber = calculate(resultNumber,tmpExpression[i],tmpExpression[i+1])

    if resultNumber > 10**9 or resultNumber < -10**9:
        continue

    if int(float(resultNumber))>maximun:
        maximun = int(float(resultNumber))
    if int(float(resultNumber))<minimun:
        minimun = int(float(resultNumber))

# print(result)
print(maximun)
print(minimun)