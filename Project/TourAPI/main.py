# -*- coding : UTF-8 -*-
import urllib.request
import xml.etree.ElementTree as ET
import Navermap
import webbrowser

def temp_main():
    list = []
    areaCode = 35
    #url = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaCode?ServiceKey=GY1KfpRH3x3fR4MpYAhLtGfpn%2BgzOAUXv86hfjkvhfZEi6BZSv2oEY%2BO28UjOyNhogZFh81Fv04pz5us%2FkIYkA%3D%3D&areaCode=" + str(areaCode) + "&numOfRows=100&MobileOS=ETC&MobileApp=AppTesting"
    url = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?ServiceKey=GY1KfpRH3x3fR4MpYAhLtGfpn%2BgzOAUXv86hfjkvhfZEi6BZSv2oEY%2BO28UjOyNhogZFh81Fv04pz5us%2FkIYkA%3D%3D&areaCode="+ str(areaCode) +"&numOfRows=10&MobileOS=ETC&MobileApp=AppTesting"
    url2 = urllib.request.urlopen(url).read()
    #url2 = url2.decode("UTF-8")
    #et = ET.fromstring(str(url2))
    #iter = et.getiterator("item")

    f = open("tour_01.xml", "wb")
    f.write(url2)
    f.close()

    tree = ET.parse("tour_01.xml")
    root = tree.getroot()

    x_points = []
    y_points = []
    nameList = []
    addrList = []

    for addr in root.iter("addr1"):
        addrList.append(addr.text)
    for x_point in root.iter("mapx"):
        x_points.append(x_point.text)
    for y_point in root.iter("mapy"):
        y_points.append(y_point.text)
    for name in root.iter("title"):
        nameList.append(name.text)


    url_3 = Navermap.Set_map_point(x_points[0], y_points[0])
    url_4 = Navermap.Set_map_address(addrList[0])
    num = 0
    for i in addrList:
        print(x_points[num])
        print(y_points[num])
        print(nameList[num])
        print(addrList[num])
        num += 1
    webbrowser.open_new(url_3)
    webbrowser.open_new(url_4)

    #for i in iter:
    #    code = i.find("code")
    #    name = i.find("name")
    #    list.append((code.text, name.text))

    #print(list)

def search_local(area_code, sigungu_code ,service_code):
    url = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?ServiceKey=GY1KfpRH3x3fR4MpYAhLtGfpn%2BgzOAUXv86hfjkvhfZEi6BZSv2oEY%2BO28UjOyNhogZFh81Fv04pz5us%2FkIYkA%3D%3D&areaCode=" + str(
        area_code) + "&sigunguCode=" + str(sigungu_code) + "&numOfRows=20000&arrange=C&MobileOS=ETC&MobileApp=AppTesting"
    url2 = urllib.request.urlopen(url).read()
    print(url)

    f = open("tour_area.xml", "wb")
    f.write(url2)
    f.close()

    tree = ET.parse("tour_area.xml")
    root = tree.getroot()

    x_points = []
    y_points = []
    nameList = []
    addrList = []
    contentid = []

    num = 0
    for addr in root.iter("addr1"):
        addrList.append(addr.text)
    for x_point in root.iter("mapx"):
        x_points.append(x_point.text)
    for y_point in root.iter("mapy"):
        y_points.append(y_point.text)
    for name in root.iter("title"):
        nameList.append(name.text)
    for content in root.iter("contenttypeid"):
        contentid.append(content.text)

    for i in addrList:
        if(contentid[num] == str(service_code)):
            print(x_points[num])
            print(y_points[num])
            print(nameList[num])
            print(addrList[num])
            print()
        num += 1


#if __name__ == '__main__':
#    main()
search_local(5, 1, 32)