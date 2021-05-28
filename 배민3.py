import heapq
def solution(A):
    # write your code in Python 3.6
    maximum=[]
    minumum=[]

    for elem in A:
        heapq.heappush(maximum, -elem)
        heapq.heappush(minumum, elem)


    while True:
        largestNum = -maximum[0]
        smallestNum = minumum[0]
        if abs(largestNum) !=abs(smallestNum):
            if abs(largestNum) >abs(smallestNum):
                heapq.heappop(maximum)
                if largestNum in minumum:
                    minumum.remove(largestNum)

            if abs(largestNum) < abs(smallestNum):
                heapq.heappop(minumum)
                if -smallestNum in maximum:
                    maximum.remove(-smallestNum)

        else:
            break
    print(largestNum, smallestNum)

solution([1,2,3,-4])