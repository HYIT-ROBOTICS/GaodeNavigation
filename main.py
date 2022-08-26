import json

import requests


def get_location_x_y(place):
    url = 'https://restapi.amap.com/v3/geocode/geo?parameters'
    parameters = {
        'key': '8c80f4eec8ebb16b23dfd21620f162c0',
        'address': '%s' % place
    }
    page_resource = requests.get(url, params=parameters)
    text = page_resource.text  # 获得数据是json格式
    data = json.loads(text)  # 把数据变成字典格式
    location = data["geocodes"][0]['location']
    print(location)
    return location


def route_planning():
    from_place = input("请输入起始地址")
    from_location = get_location_x_y(from_place)

    to_place = input("请输入目的地")
    to_location = get_location_x_y(to_place)

    url = 'https://restapi.amap.com/v3/direction/walking?parameters'
    parameters = {
        'key': '8c80f4eec8ebb16b23dfd21620f162c0',
        'origin': str(from_location),
        'destination': str(to_location)
    }

    response = requests.get(url, parameters)
    txt = response.text
    #print(txt)
    txt=json.loads(txt)
    print(txt)
    paths0=txt['route']['paths']
    paths1=paths0[0]
    paths2=paths1['steps']
    paths3=paths2[0]
    paths=paths3['polyline']
    polyline=paths.split(';')
    print(polyline)
    print(1)


if __name__ == '__main__':
    route_planning()