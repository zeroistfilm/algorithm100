def solution(A):
    # write your code in Python 3.6
    A.sort()
    frontIdx = 0
    backIdx = len(A) - 1

    while True:
        if frontIdx == backIdx:
            return 0
        if abs(A[frontIdx]) != abs(A[backIdx]):
            if abs(A[frontIdx]) > abs(A[backIdx]):
                frontIdx += 1
            if abs(A[frontIdx]) < abs(A[backIdx]):
                backIdx -= 1
        else:
            if A[frontIdx] == A[backIdx]:
                return 0
            return abs(A[frontIdx])


print(solution([3, 2, -2, 5, -3]))
print(solution([1, 1, 2, -1, 2, -1]))
print(solution([1,2,3,-4]))
print(solution([1,-2,1,1,1,2,1,1,1,1,1,1]))
