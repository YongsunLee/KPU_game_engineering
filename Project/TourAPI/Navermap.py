import os
import sys
import urllib.request
import xml.etree.ElementTree as ET

def Set_map(x_point, y_point):
    client_id = "SmUpG9NpShByzd1X1LbU"
    client_secret = "AcoyKCqpsb"
    #encText = urllib.parse.quote(address)
    # url = "https://openapi.naver.com/v1/map/geocode?query=" + encText  # json 결과
    #url = "https://openapi.naver.com/v1/map/geocode.xml?query=" + encText # xml 결과
    #request = urllib.request.Request(url)
    #request.add_header("X-Naver-Client-Id", client_id)
    #request.add_header("X-Naver-Client-Secret", client_secret)
    #response = urllib.request.urlopen(request)
    #rescode = response.getcode()
    #if (rescode == 200):
        #response_body = response.read()
        #f = open("map.xml","wb")
        #f.write(response_body)
        #f.close()

        #tree = ET.parse("map.xml")
        #root = tree.getroot()

        #for x in root.iter("x"):
        #    x_point = x

        #for y in root.iter("y"):
        #    y_point = y

    level = 10
    width = 491
    height = 221
    url_png = "https://openapi.naver.com/v1/map/staticmap.bin?clientId=" + client_id + "&url=file://c&crs=EPSG:4326&center=" + str(x_point) + "," + str(y_point) + "&level=" + str(level) + "&w=" + str(width) + "&h=" + str(height) + "&baselayer=default&markers=" + str(x_point) + "," + str(y_point)
    request = urllib.request.Request(url_png)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if (rescode == 200):
        #webbrowser.open_new(url_png)
        return url_png
    else:
        print("Error Code:" + rescode)
    #print(response_body.decode('utf-8'))
    #else:
    #    print("Error Code:" + rescode)
