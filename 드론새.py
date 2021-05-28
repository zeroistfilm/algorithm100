# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

import sys
from collections import deque


def bfs(R, C, visited, r, c):
    dc = [-1, 1, 0, 0]
    dr = [0, 0, -1, 1]

    queue = deque()
    # 처음 (1,1)은 무조건 갈 수 있는 곳이므로 queue에 넣는다.
    queue.append((r, c))
    currAreaDronCount = 0
    currAreaBirdCount = 0
    while queue:
        r, c = queue.popleft()

        aaaaaaaaaa = maps[r][c]
        if (maps[r][c] == 'v'):
            currAreaBirdCount += 1
        if (maps[r][c] == 'o'):
            currAreaDronCount += 1

        for i in range(4):
            nc = c + dc[i]
            nr = r + dr[i]

            # 범위 밖
            if nc < 0 or nc >= C or nr < 0 or nr >= R:
                continue

            # 갈 수 없는 곳은 배제
            if maps[nr][nc] == '#':
                continue

            if visited[nr][nc] == False:
                if (maps[nr][nc] == '.' or maps[nr][nc] == 'v' or maps[nr][nc] == 'o'):
                    queue.append((nr, nc))
                    visited[nr][nc] = True

    return currAreaDronCount, currAreaBirdCount, visited


R, C = map(int, input().split())
maps = [[] for i in range(R)]
canMove = deque()
for i in range(R):
    tmp = input()
    for j in range(len(tmp)):
        char = tmp[j]
        maps[i].append(tmp[j])
        if char != "#":
            canMove.append((i, j))

visited = [[False for i in range(C)] for i in range(R)]

answerdrone = 0
answerbird = 0

while canMove:
    r, c = canMove.popleft()
    if visited[r][c] == True:
        continue
    currAreaDronCount, currAreaBirdCount, visited = bfs(R, C, visited, r, c)
    if not (currAreaBirdCount == 0 and currAreaBirdCount == 0):
        if currAreaDronCount > currAreaBirdCount:
            answerdrone += 1
        if currAreaDronCount <= currAreaBirdCount:
            answerbird += 1

print(answerdrone, answerbird)
