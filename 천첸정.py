# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def CaseA(inputs):  # 중복없애기\
    beforechar = ''
    overlapcount = 0
    for char in inputs:
        if char == beforechar:
            overlapcount += 1
        beforechar = char
    return overlapcount
def CaseB(inputs):  # 중간부분 바꾸기
    inputlist= []
    for i in inputs:
        inputlist.append(i)

    beforechar = ''

    for i in range(len(inputlist)-1):
        # 전후가 같으면 아무거나로 바꿔도됨
        if inputlist[i - 1] == inputlist[i + 1]:
            inputlist[i]='*'
            continue

        # 현재와 다음이 같으면 맨뒤를 바꿈
        if inputlist[i] == inputlist[i + 1]:
            inputlist[i+1]='*'
            continue
    changecount=0
    for i in inputlist:
        if i =='*':
            changecount+=1
    return changecount

user_input = input()
print(CaseA(user_input),CaseB(user_input))
