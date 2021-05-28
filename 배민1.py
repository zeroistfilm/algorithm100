class Array():
    def __init__(self, U, L, C):
        self.array = [[0 for _ in range(len(C))] for _ in range(2)]
        self.U = U
        self.L = L

    def fillArray(self, idx, numbers):
        if numbers == 0:
            self.array[0][idx] = 0
            self.array[1][idx] = 0
        elif numbers == 1:
            if self.U > 0:
                self.array[0][idx] = 1
                self.U -= 1
            elif self.L > 0:
                self.array[1][idx] = 1
                self.L -= 1

        elif numbers == 2:
            self.array[0][idx] = 1
            self.array[1][idx] = 1
            self.U -= 1
            self.L -= 1

def solution(U, L, C):
    # write your code in Python 3.6
    array = Array(U, L, C)

    for idx in range(len(C)):
        array.fillArray(idx, C[idx])

    if array.L > 0 or array.U > 0:
        return 'impossible'

    result =''
    for i in range(len(array.array)):
        for elem in array.array[i]:
            result +=str(elem)
        if i==0:
            result += ','

    return result

print(solution(2, 2 ,[2, 0, 2, 0]))
