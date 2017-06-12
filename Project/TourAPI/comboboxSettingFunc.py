import urllib.request
import xml.etree.ElementTree as ET
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import re
import Navermap

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
    if contentTypeId == 12:
        url = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?ServiceKey=GY1KfpRH3x3fR4MpYAhLtGfpn%2BgzOAUXv86hfjkvhfZEi6BZSv2oEY%2BO28UjOyNhogZFh81Fv04pz5us%2FkIYkA%3D%3D&contentTypeId=" + str(contentTypeId) + "&areaCode=" + str(areaCode) + "&sigunguCode=" + str(sigunguCode) + "&cat1=A01&cat2=A0101&cat3=" + str(cat3) + "&listYN=Y&MobileOS=ETC&MobileApp=AppTesting&arrange=A&numOfRows=100"
    elif contentTypeId == 32:
        url = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?ServiceKey=GY1KfpRH3x3fR4MpYAhLtGfpn%2BgzOAUXv86hfjkvhfZEi6BZSv2oEY%2BO28UjOyNhogZFh81Fv04pz5us%2FkIYkA%3D%3D&contentTypeId=" + str(contentTypeId) + "&areaCode=" + str(areaCode) + "&sigunguCode=" + str(sigunguCode) + "&cat1=B02&cat2=B0201&cat3=" + str(cat3) + "&listYN=Y&MobileOS=ETC&MobileApp=AppTesting&arrange=A&numOfRows=100"

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

def infomationSettingFunc(contentTypeId, Dest, lineEditZipcode, lineEditHomepage, lineEditAddress, textEditOverview, graphicsView, MapView):
    num = 0
    addrList = []
    zipcodeList = []
    overviewList = []
    firstimageList = []
    mapList = []
    homepageList = []
    x_points = []
    y_points = []

    url = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/detailCommon?ServiceKey=GY1KfpRH3x3fR4MpYAhLtGfpn%2BgzOAUXv86hfjkvhfZEi6BZSv2oEY%2BO28UjOyNhogZFh81Fv04pz5us%2FkIYkA%3D%3D&contentTypeId="+str(contentTypeId)+"&contentId="+str(Dest)+"&MobileOS=ETC&MobileApp=TourAPI3.0_Guide&defaultYN=Y&firstImageYN=Y&areacodeYN=Y&catcodeYN=Y&addrinfoYN=Y&mapinfoYN=Y&overviewYN=Y&transGuideYN=Y"

    url2 = urllib.request.urlopen(url).read()
    url2 = url2.decode("UTF-8")
    et = ET.fromstring(str(url2))
    iter = et.getiterator("item")
    for i in iter:
        addr1 = i.find("addr1")
        firstimage = i.find("firstimage")
        homepage = i.find("homepage")
        overview = i.find("overview")
        zipcode = i.find("zipcode")
        x_point = i.find("x")
        y_point = i.find("y")
        if(x_point == None):
            temp_map = Navermap.Set_map_address(addr1.text)
        else:
            temp_map = Navermap.Set_map_point(x_point.text, y_point.text)
        addrList.append(addr1.text)
        if firstimage == None:
            firstimage = "None"
            firstimageList.append(firstimage)
        else:
            firstimageList.append(firstimage.text)
        if homepage == None:
            homepage = " "
            homepageList.append(homepage)
            Rehompage = re.search("(.*?)",homepageList[num]).group(1)
        else :
            homepageList.append(homepage.text)
            try:
                Rehompage = re.search('>(.*?)</a>', homepageList[num]).group(1)
            except:
                Rehompage = homepage.text
        if overview == None:
            overview = " "
            overviewList.append(overview)
        else:
            overviewList.append(overview.text)
        if zipcode == None:
            zipcode = " "
            zipcodeList.append(zipcode)
        else:
            zipcodeList.append(zipcode.text)
        mapList.append(temp_map)

    for i in addrList:
        # 우편번호
        lineEditZipcode.setText(str(zipcodeList[num]))
        # 홈페이지
        lineEditHomepage.setText(Rehompage)
        # 주소
        lineEditAddress.setText(str(addrList[num]))
        # 개요
        textEditOverview.setText(str(overviewList[num]))
        # 사진 추가
        if(firstimageList[num] == "None"):
            pass
        else:
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

    num = 0
    addrList.clear()
    firstimageList.clear()
    homepageList.clear()
    overviewList.clear()
    zipcodeList.clear()
    mapList.clear()
