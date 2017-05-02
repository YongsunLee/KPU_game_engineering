#2013182034 이용선 중간고사 3번
# 정렬된 두 리스트 병합하기

def merge(list1, list2):
    # 먼저 두개의 리스트를 합치고
    list3 = list1 + list2

    #정렬
    temp = -1
    for i in reversed(range(len(list3))):
        for j in range(i):
            if list3[j] > list3[j+1]:
                list3[j] , list3[j+1] = list3[j+1], list3[j]

    return print(list3)
    pass


list1 = [111, 61, 15, 5, 1]
list2 = [6, 5, 3, 2]

merge(list1, list2)

