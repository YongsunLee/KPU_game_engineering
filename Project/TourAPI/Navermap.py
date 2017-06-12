import os
import sys
import urllib.request
import xml.etree.ElementTree as ET

level = 10
width = 471
height = 221

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
