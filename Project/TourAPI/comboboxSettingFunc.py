import urllib.request
import xml.etree.ElementTree as ET

def CitycomboboxSettingFunc(areaNum, groupBox):
    num = 0
    nameList = []
    numList = []
    url = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaCode?ServiceKey=GY1KfpRH3x3fR4MpYAhLtGfpn%2BgzOAUXv86hfjkvhfZEi6BZSv2oEY%2BO28UjOyNhogZFh81Fv04pz5us%2FkIYkA%3D%3D&areaCode=" + str(
        areaNum) + "&numOfRows=25&pageNo=1&MobileOS=ETC&MobileApp=AppTesting"
    url2 = urllib.request.urlopen(url).read()
    url2 = url2.decode("UTF-8")
    et = ET.fromstring(str(url2))
    iter = et.getiterator("item")
    for i in iter:
        code = i.find("code")
        name = i.find("name")
        nameList.append(name.text)
        numList.append(code.text)
    for i in nameList:
        groupBox.addItem(str(i), int(numList[num]))
        num = num + 1
    num = 0
    nameList.clear()
    numList.clear()

def smallServicecomboboxSettingFunc(serviceNum, groupBox):
    num = 0
    nameList = []
    codeList = []
    if (serviceNum == 12):
        url =  "http://api.visitkorea.or.kr/openapi/service/rest/KorService/categoryCode?ServiceKey=GY1KfpRH3x3fR4MpYAhLtGfpn%2BgzOAUXv86hfjkvhfZEi6BZSv2oEY%2BO28UjOyNhogZFh81Fv04pz5us%2FkIYkA%3D%3D&contentTypeId="+ str(serviceNum) + "&cat1=A01&cat2=A0101&numOfRows=20&pageNo=1&MobileOS=ETC&MobileApp=AppTesting"
    elif (serviceNum == 32):
        url = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/categoryCode?ServiceKey=GY1KfpRH3x3fR4MpYAhLtGfpn%2BgzOAUXv86hfjkvhfZEi6BZSv2oEY%2BO28UjOyNhogZFh81Fv04pz5us%2FkIYkA%3D%3D&contentTypeId="+ str(serviceNum) + "&cat1=B02&cat2=B0201&numOfRows=20&pageNo=1&MobileOS=ETC&MobileApp=AppTesting"
    url2 = urllib.request.urlopen(url).read()
    url2 = url2.decode("UTF-8")
    et = ET.fromstring(str(url2))
    iter = et.getiterator("item")
    for i in iter:
        code = i.find("code")
        name = i.find("name")
        nameList.append(name.text)
        codeList.append(code.text)
    for i in nameList:
        groupBox.addItem(str(i), str(codeList[num]))
        num = num + 1
    num = 0
    nameList.clear()
    codeList.clear()