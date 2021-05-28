import bisect
def solution(A, B):
    A.sort()
    B.sort()
    i = 0
    for a in A:
        if i < len(B) - 1 and B[i] < a:
            i = bisect.bisect_right(B, a)-1
        if a == B[i]:
            return a
    return -1

print(solution([1,3,2,1],[4,2,5,3,2]))
print(solution([2,1],[3,3]))
print(solution([1],[0]))
print(solution([5, 6, 7, 8, 9],[5, 2, 3] ))
print(solution([5, 2, 3], [5, 6, 7, 8, 9]))

print(solution([3, 5, 6, 6, 7] ,[1, 2, 3, 3]))
print(solution([1, 2, 3, 3],[3, 5, 6, 6, 7]))
print(solution([3, 5, 6, 6, 7], [1, 2, 3, 0]))
print(solution([3, 5, 6, 6, 7], [1, 2, 3, 4]))
print(solution([3, 5, 6, 6, 7], [2, 3, 4, 5]))
print(solution([3, 5, 6, 6, 7], [3, 4, 5, 6]))
