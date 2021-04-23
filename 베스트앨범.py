# https://programmers.co.kr/learn/courses/30/lessons/42579

genres = ['pop', 'pop', 'pop', 'rap', 'rap']
plays = [45, 50, 40, 60, 70]


def solution(genres, plays):
    dic = {}
    for i in range(len(genres)):
        if not genres[i] in dic:
            dic[genres[i]] = []
        dic[genres[i]].append((plays[i], i))

    topOfGenre = []
    for i in dic.keys():
        sumGenres = 0
        dic[i].sort(key=lambda play: play[0], reverse=True)
        for j in range(len(dic[i])):
            sumGenres += dic[i][j][0]
        topOfGenre.append((sumGenres, i))
    topOfGenre.sort(key=lambda sum: sum[0], reverse=True)  # sort best genres

    result = []
    for _, genre in topOfGenre:  # sorted by best
        if len(dic[genre]) < 2:  # filtering for length 1 of genre
            result.append(dic[genre][0][1])
        else:
            for i in range(2):
                result.append(dic[genre][i][1])
    return result


print(solution(genres, plays))
