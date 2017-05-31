# -*- coding : UTF-8 -*-
import urllib.request
import xml.etree.ElementTree as ET
import Navermap
import webbrowser

def main():
    list = []
    areaCode = 35
    #url = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaCode?ServiceKey=GY1KfpRH3x3fR4MpYAhLtGfpn%2BgzOAUXv86hfjkvhfZEi6BZSv2oEY%2BO28UjOyNhogZFh81Fv04pz5us%2FkIYkA%3D%3D&areaCode=" + str(areaCode) + "&numOfRows=100&MobileOS=ETC&MobileApp=AppTesting"

    url = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?ServiceKey=GY1KfpRH3x3fR4MpYAhLtGfpn%2BgzOAUXv86hfjkvhfZEi6BZSv2oEY%2BO28UjOyNhogZFh81Fv04pz5us%2FkIYkA%3D%3D&areaCode="+ str(areaCode) +"&numOfRows=100&MobileOS=ETC&MobileApp=AppTesting"
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

    for x_point in root.iter("mapx"):
        x_points.append(x_point.text)
    for y_point in root.iter("mapy"):
        y_points.append(y_point.text)

    url_3 = Navermap.Set_map(x_points[0], y_points[0])
    print(x_points[0])
    print(y_points[0])
    webbrowser.open_new(url_3)

    #for i in iter:
    #    code = i.find("code")
    #    name = i.find("name")
    #    list.append((code.text, name.text))

    #print(list)

if __name__ == '__main__':
    main()
