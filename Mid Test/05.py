#2013182034 이용선 중간고사 5번
# CabCompany 클래스

class CabCompany:
    def __init__(self, companyName):
        self.comName = companyName
    pass

class Driver(CabCompany):
    def __init__(self, companyName, driverName):
        CabCompany.__init__(self, companyName)
        self.driverName = driverName
        pass
    def printInfo(self):
        print("[회사이름]", self.comName, "[기사 이름]", self.driverName)


def main():
    driver_1 = list()
    for i in range(2):
        companyName = input("회사 이름 입력")
        driverName = input("운전기사 이름 입력")
        driver_1.append(Driver(companyName, driverName))

    for i in driver_1:
        i.printInfo()

main()