class Dice():
    def __init__(self, N, M, initposition, maps):
        self.N = N
        self.M = M
        self.top = 1
        self.dice = [0 for _ in range(6)]
        self.maps = maps
        self.x = initposition[0]
        self.y = initposition[1]
        self.bottom = 5
        self.top = 0

    def rolling(self, order):
        (nextx, nexty) = self.getNextPosition(order)
        if self.isInBoundaries((nextx, nexty)):
            self.x = nextx
            self.y = nexty
            self.setBottomAfterDiceRoll(order)
            mapvalue = self.getMapValue((self.x, self.y))
            if mapvalue==0:
                self.setMapValue((self.x, self.y), self.getDiceValue(self.bottom))
            else:
                self.setDiceValue(self.bottom, self.getMapValue((self.x, self.y)))
                self.setMapValue((self.x, self.y), 0)
            self.printTopValue()

    def printTopValue(self):
        return print(self.dice[0])

    def isInBoundaries(self, nextposition):
        nextx, nexty = nextposition[0], nextposition[1]
        if 0 <= nextx < self.M and 0 <= nexty < self.N:
            return True
        return False

    def getNextPosition(self, order):
        if order == 3:
            nx = self.x
            ny = self.y - 1
        elif order == 4:
            nx = self.x
            ny = self.y + 1
        elif order == 1:
            nx = self.x + 1
            ny = self.y
        elif order == 2:
            nx = self.x - 1
            ny = self.y
        return (nx, ny)

    def getMapValue(self, position):
        return self.maps[position[1]][position[0]]

    def setMapValue(self, position,value):
        self.maps[position[1]][position[0]]=value


    def setBottomAfterDiceRoll(self, direction):
        if direction == 1:
            self.dice[0], self.dice[2], self.dice[3], self.dice[5] = self.dice[3], self.dice[0], self.dice[5], self.dice[2]
        elif direction == 2:
            self.dice[0], self.dice[2], self.dice[3], self.dice[5] = self.dice[2], self.dice[5], self.dice[0], self.dice[3]
        if direction == 3:
            self.dice[0], self.dice[1], self.dice[4], self.dice[5] = self.dice[4], self.dice[0], self.dice[5], self.dice[1]
        elif direction == 4:
            self.dice[0], self.dice[1], self.dice[4], self.dice[5] = self.dice[1], self.dice[5], self.dice[0], self.dice[4]

    def setDiceValue(self, currSide, value):
        self.dice[currSide] = value

    def getDiceValue(self, currSide):
        return self.dice[currSide]

import sys
sys.stdin = open('input.txt')
N, M,y, x, K = map(int, sys.stdin.readline().split())
maps = []
for ni in range(N):
    maps.append(list(map(int, sys.stdin.readline().split())))
orders = list(map(int, sys.stdin.readline().split()))

dice = Dice(N, M, (x, y), maps)

for order in orders:
    dice.rolling(order)
