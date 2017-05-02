#2013182034 이용선 중간고사 2번
#중복된 숫자 출력하기

num = input("10개 숫자 입력: ")

# 리스트에 넣습니다.
list1 = []
for i in num:
    list1.append(i)

print(list1)

list2 = []
list3 = []

for i in list1:
    # list2에 있으면 list3에 넣습니다.
    if i in list2:
        list3.append(i)
    # 없으면 2에 넣습니다.
    else:
        list2.append(i)

print("중복된 숫자:", list3)