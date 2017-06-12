import urllib.request
import xml.etree.ElementTree as ET

level = 13
width = 491
height = 221

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

def Set_map_point(x_point, y_point):
    client_id = "SmUpG9NpShByzd1X1LbU"
    client_secret = "AcoyKCqpsb"

    global level, width, height
    url_png = "https://openapi.naver.com/v1/map/staticmap.bin?clientId=" + client_id + "&url=file://c&crs=EPSG:4326&center=" + str(x_point) + "," + str(y_point) + "&level=" + str(level) + "&w=" + str(width) + "&h=" + str(height) + "&baselayer=default&markers=" + str(x_point) + "," + str(y_point)
    request = urllib.request.Request(url_png)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        return url_png
    else:
        print("Error Code:" + rescode)

def Set_map_address(address):
    client_id = "SmUpG9NpShByzd1X1LbU"
    client_secret = "AcoyKCqpsb"
    encText = urllib.parse.quote(address)
    url = "https://openapi.naver.com/v1/map/geocode.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        f = open("map.xml","wb")
        f.write(response_body)
        f.close()

        tree = ET.parse("map.xml")
        root = tree.getroot()

        for x in root.iter("x"):
            x_point = x.text
        for y in root.iter("y"):
            y_point = y.text

        global level, width, height
        url_png = "https://openapi.naver.com/v1/map/staticmap.bin?clientId=" + client_id + "&url=file://c&crs=EPSG:4326&center=" + str(x_point) + "," + str(y_point) + "&level=" + str(level) + "&w=" + str(width) + "&h=" + str(height) + "&baselayer=default&markers=" + str(x_point) + "," + str(y_point)
        request = urllib.request.Request(url_png)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()

        if (rescode == 200):
            return url_png
        else:
            print("Error Code:" + rescode)
    else:
        print("Error Code:" + rescode)
