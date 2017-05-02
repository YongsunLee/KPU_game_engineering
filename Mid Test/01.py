# 2013182034 이용선 중간고사 1번
# 정수의 자릿수 나누기

class class1:
    # 생성자
    def __init__(self, n):
        self.n = n
        self.a = self.n // 1000
        self.b = self.n // 100
        self.c = (self.n % 100) // 10
        self.d = self.n % 10

    # 기능
    def func(self):
        print("천의 자리: ", self.a)
        print("백의 자리: ", self.b)
        print("십의 자리: ", self.c)
        print("일의 자리: ", self.d)


def main():
    n = int(input("숫자 입력:"))
    c1 = class1(n)
    c1.func()

main()