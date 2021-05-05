priorities = [2]
location = 0


def solution(priorities, location):
    from collections import deque
    dq = deque()
    for i in range(len(priorities)):
        dq.append((priorities[i], i))
    order = 0
    while True:
        paperPriority = dq[0][0]
        comparePriority = max(dq)[0]
        if paperPriority < comparePriority:
            dq.append(dq.popleft())
        else:
            out = dq.popleft()
            order += 1
            if out[1] == location:
                return order


print(solution(priorities, location))
