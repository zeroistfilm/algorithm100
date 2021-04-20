#https://programmers.co.kr/learn/courses/30/lessons/42579

genres = ['pop', 'pop', 'pop', 'rap', 'rap']
plays = [45, 50, 40, 60, 70]


def solution(genres, plays):
    dic = {}
    for i in range(len(genres)):
        if not genres[i] in dic:
            dic[genres[i]] = []
        dic[genres[i]].append((plays[i], i))

    tmp = []
    result = []
    for i in dic.keys():
        dic[i].sort(key=lambda x: -x[0])
        sumGenres = 0
        for j in range(len(dic[i])):
            sumGenres += dic[i][j][0]
        tmp.append((sumGenres, i))
    # sort genres
    tmp.sort(key=lambda x: -x[0])

    for j in range(len(dic.keys())):
        genres = tmp[j][1]  # sorted by best
        if len(dic[genres]) < 2:
            result.append(dic[genres][0][1])
        else:
            for i in range(2):
                result.append(dic[genres][i][1])
    return result


print(solution(genres, plays))
