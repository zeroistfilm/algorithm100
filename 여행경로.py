from collections import deque
import copy


def travel(dic, start, result):
    if not start in dic:
        return 0
    if len(dic[start]) == 0:
        return 0
    destination = dic[start].popleft()
    result.append(destination)
    travel(dic, destination, result)


def solution(tickets):
    dic = {}
    result = ['ICN']
    for ticket in tickets:
        if not ticket[0] in dic:
            dic[ticket[0]] = []
        dic[ticket[0]].append(ticket[1])

    tmpdic = copy.deepcopy(dic)

    for key in dic.keys():
        dic[key].sort()
        dic[key] = deque(dic[key])
    travel(dic, 'ICN', result)

    if not len(result) == len(tickets)+1:
        result = ['ICN']
        for key in tmpdic.keys():
            tmpdic[key].sort(reverse=True)
            tmpdic[key] = deque(tmpdic[key])
        travel(tmpdic, 'ICN', result)


    return result


tickets = [["ICN", "SFO"], ["SFO", "ICN"], ["ICN", "SFO"],["SFO","QRE"]]
print(solution(tickets))
