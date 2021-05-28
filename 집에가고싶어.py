# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N, B = map(int, input().split())
playlist=[]
for i in range(N):
    playlist.append(tuple(map(int, input().split())))
playlist.sort(key=lambda x:(-x[0],-x[1]))
currtime=0
while playlist:
    wantstarttime, wanttime = playlist.pop()
    if currtime<wantstarttime:
        currtime+=wantstarttime
        currtime+=wanttime
    else:
        currtime+=wanttime
    currtime+=B #배터리충전
print(currtime)