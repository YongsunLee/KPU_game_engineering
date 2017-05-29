# -*- coding : UTF-8 -*-
import urllib.request
import xml.etree.ElementTree as ET

def main():
    list = []
    areaCode = 1
    url = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaCode?ServiceKey=GY1KfpRH3x3fR4MpYAhLtGfpn%2BgzOAUXv86hfjkvhfZEi6BZSv2oEY%2BO28UjOyNhogZFh81Fv04pz5us%2FkIYkA%3D%3D&areaCode="+str(areaCode)+"&numOfRows=20&pageNo=1&MobileOS=ETC&MobileApp=AppTesting"

    url2 = urllib.request.urlopen(url).read()
    url2 = url2.decode("UTF-8")
    et = ET.fromstring(str(url2))
    iter = et.getiterator("item")

    for i in iter:
        code = i.find("code")
        name = i.find("name")
        list.append((code.text, name.text))

    print(list)

if __name__ == '__main__':
    main()
