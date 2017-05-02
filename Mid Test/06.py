#2013182034 이용선 중간고사 6번
# 각 자리숫자들의 곱

def multiplyDigits(n):
    if n < 10:
        return n
    return (n % 10) * multiplyDigits(n//10)

def main():
    n = int(input("정수를 입력하세요:"))
    print(multiplyDigits(n))

main()