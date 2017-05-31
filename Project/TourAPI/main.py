# -*- coding : UTF-8 -*-
import urllib.request
import xml.etree.ElementTree as ET

def main():
    list = []
    areaCode = 2
    url = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaCode?ServiceKey=GY1KfpRH3x3fR4MpYAhLtGfpn%2BgzOAUXv86hfjkvhfZEi6BZSv2oEY%2BO28UjOyNhogZFh81Fv04pz5us%2FkIYkA%3D%3D&areaCode="+str(areaCode)+"&numOfRows=40&pageNo=1&MobileOS=ETC&MobileApp=AppTesting"

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

    for x_point in root.iter("code"):
        x_points.append(x_point.text)
    for y_point in root.iter("name"):
        y_points.append(y_point.text)

    for i in x_points:
        print(i)
    for y in y_points:
        print(y)


    #for i in iter:
    #    code = i.find("code")
    #    name = i.find("name")
    #    list.append((code.text, name.text))

    #print(list)

if __name__ == '__main__':
    main()
