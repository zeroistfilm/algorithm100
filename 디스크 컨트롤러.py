jobs = [[0, 3], [1, 9], [2, 6]]


def solution(jobs):
    import heapq

    answer, 현재시간, i = 0, 0, 0
    직전에시작한시간 = -1
    작업리스트 = []

    while i < len(jobs):
        for job in jobs:
            if 직전에시작한시간 < job[0] <= 현재시간: # 현재시간에 가능한 작업들 넣기
                heapq.heappush(작업리스트, [job[1], job[0]])

        if len(작업리스트) > 0:
            작업시간, 시작하기원했던시간 = heapq.heappop(작업리스트)
            직전에시작한시간 = 현재시간
            현재시간 += 작업시간
            answer += (현재시간 - 시작하기원했던시간)
            i += 1
        else:
            현재시간 += 1
    return int(answer / len(jobs))


print(solution(jobs))
