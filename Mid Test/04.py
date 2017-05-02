#2013182034 이용선 중간고사 4번
# 알파벳 및 숫자 빈도수

s = input("숫자 및 영단어 입력:")

# 리스트에 넣습니다.
list1 = []
for i in s:
    list1.append(i)

# 딕셔너리에 넣습니다.
d = dict()
for c in list1:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1

# 출력합니다.
print(d)

#print(list1)