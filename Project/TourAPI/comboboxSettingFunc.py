import urllib.request
import xml.etree.ElementTree as ET
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import re

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

def TouristDestinationSettingFunc(contentTypeId, cat3, areaCode, sigunguCode, touristDestBox):
    num = 0
    nameList = []
    idList = []
    url = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?ServiceKey=GY1KfpRH3x3fR4MpYAhLtGfpn%2BgzOAUXv86hfjkvhfZEi6BZSv2oEY%2BO28UjOyNhogZFh81Fv04pz5us%2FkIYkA%3D%3D&contentTypeId=" + str(contentTypeId) + "&areaCode=" + str(areaCode) + "&sigunguCode=" + str(sigunguCode) + "&cat1=A01&cat2=A0101&cat3=" + str(cat3) + "&listYN=Y&MobileOS=ETC&MobileApp=AppTesting&arrange=A&numOfRows=20&pageNo=1"

    url2 = urllib.request.urlopen(url).read()
    url2 = url2.decode("UTF-8")
    et = ET.fromstring(str(url2))
    iter = et.getiterator("item")
    for i in iter:
        name = i.find("title")
        contentId = i.find("contentid")
        nameList.append(name.text)
        idList.append(contentId.text)

    for i in nameList:
        touristDestBox.addItem(str(i), int(idList[num]))
        num = num + 1

    num = 0
    nameList.clear()
    idList.clear()

def infomationSettingFunc(Dest, lineEditZipcode, lineEditHomepage, lineEditAddress, textEditOverview, graphicsView, MapView):
    num = 0
    addrList = []
    zipcodeList = []
    overviewList = []
    firstimageList = []
    mapList = []
    homepageList = []
    url = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/detailCommon?ServiceKey=GY1KfpRH3x3fR4MpYAhLtGfpn%2BgzOAUXv86hfjkvhfZEi6BZSv2oEY%2BO28UjOyNhogZFh81Fv04pz5us%2FkIYkA%3D%3D&contentTypeId=12&contentId="+str(Dest)+"&MobileOS=ETC&MobileApp=TourAPI3.0_Guide&defaultYN=Y&firstImageYN=Y&areacodeYN=Y&catcodeYN=Y&addrinfoYN=Y&mapinfoYN=Y&overviewYN=Y&transGuideYN=Y"

    url2 = urllib.request.urlopen(url).read()
    url2 = url2.decode("UTF-8")
    et = ET.fromstring(str(url2))
    iter = et.getiterator("item")
    for i in iter:
        addr1 = i.find("addr1")
        firstimage = i.find("firstimage")
        homepage = i.find("homepage")
        #Rehompage = re.search('>"(.*?)"</a>',homepage)
        overview = i.find("overview")
        zipcode = i.find("zipcode")
        temp_map = Set_map_address(addr1)
        addrList.append(addr1.text)
        firstimageList.append(firstimage.text)
        homepageList.append(homepage.text)
        overviewList.append(overview.text)
        zipcodeList.append(zipcode.text)
        mapList.append(temp_map)

    for i in addrList:
        # 우편번호
        lineEditZipcode.setText(str(zipcodeList[num]))
        # 홈페이지
        lineEditHomepage.setText(str(homepageList[num]))
        # 주소
        lineEditAddress.setText(str(addrList[num]))
        # 개요
        textEditOverview.setText(str(overviewList[num]))
        # 사진 추가
        data = urllib.request.urlopen(firstimageList[num]).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        scaledImg = pixmap.scaled(graphicsView.size(), Qt.KeepAspectRatio)
        graphicsView.setPixmap(scaledImg)
        # 지도 추가
        map_data = urllib.request.urlopen(mapList[num]).read()
        map = QPixmap()
        map.loadFromData(map_data)
        MapView.setPixmap(map)

        num = num + 1

    num = 0
    addrList.clear()
    firstimageList.clear()
    homepageList.clear()
    overviewList.clear()
    zipcodeList.clear()
