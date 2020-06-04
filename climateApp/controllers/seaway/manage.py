from climateApp.models import *
import MySQLdb
import base64

from math import radians, cos, sin, asin, sqrt
import math

from climateApp.controllers.weather_attr.get_attr import *

def getPort(name):
    db = MySQLdb.connect("localhost", "root", "climate123", "climate_services", charset='utf8')# 获得港口信息

    cursor = db.cursor()
    cursor.execute("select NAMECN from t41_port where PORTID=55281")
    data = cursor.fetchall();
    print(data)
    db.close()
    return 0

def getPortByName(name):
    debugOutputFile(name)# 获得港口信息
    data = PortInfo.objects.filter(f_vc_zwm=name);
    if (len(data) > 0):
        debugOutputFile(data[0].f_it_gkh)
        return data[0].f_it_gkh;
    return -1;

def  InsertAllSeaway():
    ports = PortInfo.objects.filter(f_dl_jd__gte=105, f_dl_jd__lte=135, f_dl_wd__gte=0, f_dl_wd__lte=40).order_by('f_it_gkh');
    debugOutputFile(len(ports))# 将根据港口获得的航线保存到数据库中
    for i in range(len(ports)-1):
        for j in range(i+1, len(ports)):
            data = getSeaway(ports[i].f_it_gkh,ports[j].gkh);
            json_text_datas = json.dumps(data);
            SeawayInfo.objects.create(f_it_gkhx=ports[i].f_it_gkh, f_it_gkhd=ports[j].f_it_gkh, f_tf_hx=json_text_datas);


def getSeaway(port1, port2):
    url = 'http://fleet.shiplinker.com/transMethod.do?cmd=0x0501&param='# 利用港口号从外部接口获得航线信息
    s = '{"rp_id":"","orig_rp_id":"","leg":-1,"rp_group":"","pointList":"' + str(port1) + '#' + str(port2) + '"}'
    # print(s)
    url += str(base64.b64encode(s.encode('utf-8')))[2:-2]
    # print(url)
    try:
        html = urllib.request.urlopen(url);
        # print(html)
        debugOutputFile(html);
        htmldata = json.loads(html.read().decode('utf-8'));
        debugOutputFile(htmldata)
        # print(htmldata)
        routes = htmldata[1]['routes']
        paths = []
        for route in routes:
            pointsets = route['pointset'].split('|')
            for pointset in pointsets:
                pointset = pointset.split(',')
                if pointset not in paths:
                    paths.append(pointset)
    except Exception as e:
        paths=[]
    return paths;

def getSeawayFastly(port1, port2):
    reverse_flag = 0;# 根据港口号从数据库中获得航线信息，没有的话再从外部接口中获得
    if (port1 > port2):
        temp = port1;
        port1 = port2;
        port2 = temp;
        reverse_flag = 1;
    res = SeawayInfo.objects.filter(f_it_gkhx=port1, f_it_gkhd=port2)
    if (len(res) > 0):
        paths = json.loads(res[0].f_tf_hx);
        if (len(paths) >0):
            if reverse_flag == 0:
                return paths;
            else:
                return list(reversed(paths))

    '''url = 'http://fleet.shiplinker.com/transMethod.do?cmd=0x0501&param='
    s = '{"rp_id":"","orig_rp_id":"","leg":-1,"rp_group":"","pointList":"' + str(port1) + '#' + str(port2) + '"}'
    # print(s)
    url += str(base64.b64encode(s.encode('utf-8')))[2:-2]
    # print(url)
    try:
        html = urllib.request.urlopen(url);
        # print(html)
        debugOutputFile(html);
        htmldata = json.loads(html.read().decode('utf-8'));
        debugOutputFile(htmldata)
        # print(htmldata)
        routes = htmldata[1]['routes']
        paths = []
        for route in routes:
            pointsets = route['pointset'].split('|')
            for pointset in pointsets:
                pointset = pointset.split(',')
                if pointset not in paths:
                    paths.append(pointset)
        if reverse_flag == 0:
            return paths;
        else:
            return list(reversed(paths))
    except Exception as e:
        paths=[]'''
    return [];

def haversine(lat1, lon1, lat2, lon2):  # 经度1，纬度1，经度2，纬度2 （十进制度数）
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine公式
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r


def divideHangxianoldwithBug(hangxian, N):
    # 求distance
    # 根据需求把航线平均分成N段，找到航线上每个关键点用于画图
    new_hangxian=[]
    for one in hangxian:
        new_hangxian.append([float(one[0]), float(one[1])])
    hangxian = new_hangxian
    distance = 0
    for i in range(0, len(hangxian) - 1):
        # print(haversine(hangxian[i][0], hangxian[i][1], hangxian[i+1][0], hangxian[i+1][1]))
        distance += haversine(hangxian[i][0], hangxian[i][1], hangxian[i + 1][0], hangxian[i + 1][1])
    avgSpeed = 40  # 30km/h
    time = distance / avgSpeed
    T = math.floor(time / (N - 1))  # T 时间间隔
    #print(distance, T, time)
    restime = []
    for i in range(0, N):
        restime.append(i * T)
    restime.append(time)
    #print(restime)

    resHangxian = []
    resHangxian.append(hangxian[0])

    onedivide = 0
    for i in range(0, len(hangxian) - 1):
        dis = haversine(hangxian[i][0], hangxian[i][1], hangxian[i + 1][0], hangxian[i + 1][1])
        onedivide += dis
        if (onedivide < avgSpeed * T):
            # 再看下一个点
            i += 1
        else:
            # 找到点i和点i+1之间的分隔点
            k = (onedivide - avgSpeed * T) / dis
            lat = hangxian[i + 1][0] - k * (hangxian[i + 1][0] - hangxian[i][0])
            lon = hangxian[i + 1][1] - k * (hangxian[i + 1][1] - hangxian[i][1])
            resHangxian.append([lat, lon])
            onedivide = onedivide - avgSpeed * T
            while onedivide >= avgSpeed * T:
                k = (onedivide - avgSpeed * T) / onedivide
                lat = hangxian[i + 1][0] - k * (hangxian[i + 1][0] - lat)
                lon = hangxian[i + 1][1] - k * (hangxian[i + 1][1] - lon)
                resHangxian.append([lat, lon])
                onedivide = onedivide - avgSpeed * T

    resHangxian.append(hangxian[len(hangxian) - 1])
    if len(resHangxian) > (N + 1):
        resHangxian.pop()
        resHangxian[len(resHangxian) - 1] = hangxian[len(hangxian) - 1]
    return [hangxian, resHangxian, restime, distance]  # 返回旧航线，新航线，时间序列，总路程


def divideHangxian(hangxian, N):

    new_hangxian = []
    for one in hangxian:
        new_hangxian.append([float(one[0]), float(one[1])])
    hangxian = new_hangxian
    # 求distance
    distance = 0
    for i in range(0, len(hangxian) - 1):
        # print(haversine(hangxian[i][0], hangxian[i][1], hangxian[i+1][0], hangxian[i+1][1]))
        distance += haversine(hangxian[i][0], hangxian[i][1], hangxian[i + 1][0], hangxian[i + 1][1])
    avgSpeed = 40  # 30km/h
    time = distance / avgSpeed
    T = math.floor(time / (N - 1))  # T 时间间隔
    if T == 0:
        T = (math.floor(time * 10 / (N - 1)) * 1.00) / 10
    #print(distance, T, time)
    restime = []
    for i in range(0, N):
        restime.append(i * T)
    restime.append(time)
    #print(restime)

    resHangxian = []
    resHangxian.append(hangxian[0])

    onedivide = 0
    for i in range(0, len(hangxian) - 1):
        dis = haversine(hangxian[i][0], hangxian[i][1], hangxian[i + 1][0], hangxian[i + 1][1])
        onedivide += dis
        if (onedivide < avgSpeed * T):
            # 再看下一个点
            i += 1
        else:
            # 找到点i和点i+1之间的分隔点
            k = (onedivide - avgSpeed * T) / dis
            lat = hangxian[i + 1][0] - k * (hangxian[i + 1][0] - hangxian[i][0])
            lon = hangxian[i + 1][1] - k * (hangxian[i + 1][1] - hangxian[i][1])
            resHangxian.append([lat, lon])
            onedivide = onedivide - avgSpeed * T
            while onedivide >= avgSpeed * T:
                k = (onedivide - avgSpeed * T) / onedivide
                lat = hangxian[i + 1][0] - k * (hangxian[i + 1][0] - lat)
                lon = hangxian[i + 1][1] - k * (hangxian[i + 1][1] - lon)
                resHangxian.append([lat, lon])
                onedivide = onedivide - avgSpeed * T

    resHangxian.append(hangxian[len(hangxian) - 1])
    if len(resHangxian) > (N + 1):
        resHangxian.pop()
        resHangxian[len(resHangxian) - 1] = hangxian[len(hangxian) - 1]
    return [hangxian, resHangxian, restime, distance]  # 返回旧航线，新航线，时间序列，总路程
