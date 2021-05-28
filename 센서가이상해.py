def combination(order):
    orderlist = list(map(int, order.split()))
    candidate = [0, 1]
    A = ''
    B = ''
    j = 0
    for i in range(len(orderlist)):
        if j > len(candidate) - 1:
            j = 0
        for k in range(orderlist[i]):
            A += str(candidate[j])
        j += 1

    j = 1
    for i in range(len(orderlist)):
        if j > len(candidate) - 1:
            j = 0
        for k in range(orderlist[i]):
            B += str(candidate[j])
        j += 1

    return A, B


def compareDiff(sensor, tmp):
    count = 0
    for i in range(len(sensor)):
        if sensor[i] != tmp[i]:
            count += 1
    return count

def calcSwitch(first, selected):
    result =0
    firstlist= []
    selectedlist = []
    for i in first:
        firstlist.append(i)
    for i in selected:
        selectedlist.append(i)

    for i in range(len(firstlist)):
        if firstlist[i] ==selectedlist[i]:
            #순서대로 비교하면서 같으면 넘어가고
            continue
        else:#다를경우에 뒷부분을 살펴본다
            for j in range(i,len(firstlist)):
                #뒷부분을 보면서 원본값에 해당하는 위치를 반환하고, 그게 이동한 횟수가된다다
                if firstlist[i] == selectedlist[j]:
                    selectedlist[i] ,selectedlist[j] =selectedlist[j], selectedlist[i]
                    break
                result+=1
    return  result




N,M = map(int,input().split())
first = input()
second = input()

first = first.replace(" ", "")
A, B = combination(second)

diffA = compareDiff(first, A)
diffB = compareDiff(first, B)
if diffA > diffB:
    selected = B
else:
    selected = A

print(calcSwitch(first, selected))
