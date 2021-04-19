# https://www.acmicpc.net/problem/11816
import sys

sys.stdin = open('input.txt')

N = sys.stdin.readline().strip()
result = 0
if N[0] == '0':
    if N[1] == 'x':
        j = 0
        for i in N[2:][::-1]:
            if i == 'a':
                result += 10 * 16 ** j
            elif i == 'b':
                result += 11 * 16 ** j
            elif i == 'c':
                result += 12 * 16 ** j
            elif i == 'd':
                result += 13 * 16 ** j
            elif i == 'e':
                result += 14 * 16 ** j
            elif i == 'f':
                result += 15 * 16 ** j
            else:
                result += int(i) * 16 ** j
            j += 1

        print(result)
    else:
        # 8
        j = 0
        for i in N[1:][::-1]:
            result += int(i) * 8 ** j
            j += 1

        print(result)


else:
    # 10
    print(N)
