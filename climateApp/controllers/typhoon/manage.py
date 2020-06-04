from climateApp.models import *
import sys
import datetime
import urllib
import json
import math
import urllib.request

# 将时间字符串转换成datatime格式
def getFullTimeHour(str):
    #str="2017041406"
    year = str[0:4];
    month = str[4:6];
    date = str[6:8];
    hour = str[8:10];
    #显示的时间格式
    res = year+'-'+month+'-'+date+' '+hour+':00:00'
    return datetime.datetime.strptime(res, '%Y-%m-%d %H:%M:%S')

# 将时间字符串转换成datatime格式
def getFullTimeDate(str):
    year = str[0:4];
    month = str[4:6];
    date = str[6:8];
    #显示的时间格式
    res = year + '-' + month + '-' + date
    return datetime.datetime.strptime(res, '%Y-%m-%d')

# 将文本中的台风信息解析，写入数据库
def insertFileInfo():
    Typhoon.objects.all().delete()
    filename = "/home/data/CH2017BST.txt";
    f = open(filename, "r");
    lines = f.readlines()
    nums = 0;
    i = 0;
    while i < len(lines):
        # 对每一行数据进行解析
        one_typhoon = Typhoon();
        data = lines[i].split();
        one_typhoon.resource_type = data[0];
        one_typhoon.international_num = data[1];
        one_typhoon.path_nums = data[2];
        one_typhoon.cyclone_num = data[3];
        one_typhoon.cn_cyclone_id = data[4];
        one_typhoon.cyclone_end = data[5];
        one_typhoon.interval_hours = data[6];
        one_typhoon.name = data[7][1:-1];
        one_typhoon.data_date = getFullTimeDate(data[8]);
        for j in range(int(one_typhoon.path_nums)):
            i+=1;
            data = lines[i].split();
            one_typhoon.data_time = getFullTimeHour(data[0]);
            one_typhoon.strength_grade = data[1];
            one_typhoon.latitude = data[2];
            one_typhoon.longitude = data[3];
            one_typhoon.pressure = data[4];
            one_typhoon.wind_speed = data[5];
            # 检测数据库是否存在，不存在则插入该数据
            if len(Typhoon.objects.filter(name=one_typhoon.name, data_time=one_typhoon.data_time)) == 0:
                Typhoon.objects.create(resource_type=one_typhoon.resource_type, international_num=one_typhoon.international_num,
                                       path_nums=one_typhoon.path_nums, cyclone_num=one_typhoon.cyclone_num,
                                       cn_cyclone_id=one_typhoon.cn_cyclone_id, cyclone_end=one_typhoon.cyclone_end,
                                       interval_hours=one_typhoon.interval_hours, name=one_typhoon.name,
                                       data_date=one_typhoon.data_date, data_time=one_typhoon.data_time,
                                       strength_grade=one_typhoon.strength_grade, latitude=one_typhoon.latitude,
                                       longitude=one_typhoon.longitude, pressure=one_typhoon.pressure,
                                       wind_speed=one_typhoon.wind_speed);
        i+=1


# 搜索某时间之后的一段时间内的台风信息
def search_data(search_time, period):
    start = getFullTimeDate(search_time);
    end = start + datetime.timedelta(days=period);
    # 从数据库查询某个时间段内的所有台风
    res = Typhoon.objects.filter(f_dt_tfsj__gte=start, f_dt_tfsj__lte=end).values("f_vc_mz").distinct();
    names = [];
    startTime = [];
    strength_grade_max = [];
    pressure_min = [];
    wind_speed_max = [];
    for one in res:
        # 获取某台风在某时间段的台风数据
        res = Typhoon.objects.filter(f_dt_tfsj__gte=start, f_dt_tfsj__lte=end, f_vc_mz=one["f_vc_mz"]);
        names.append(one["f_vc_mz"]);
        startTime.append(res.order_by("f_dt_tfsj").values("f_dt_tfsj")[0]["f_dt_tfsj"]);
        strength_grade_max.append(res.order_by("f_dl_qd").reverse().values("f_dl_qd")[0]["f_dl_qd"]);
        pressure_min.append(res.order_by("f_dl_zdqy").values("f_dl_zdqy")[0]["f_dl_zdqy"]);
        wind_speed_max.append(res.order_by("f_dl_zdfs").reverse().values("f_dl_zdfs")[0]["f_dl_zdfs"]);

    finalRes = {"name":names, "start_time":startTime, "strength_grade_max":strength_grade_max, "pressure_min": pressure_min, "wind_speed_max":wind_speed_max};
    return finalRes;

# 搜索某时间之后的一段时间内的台风信息
def search_typhoon_info(search_time, period):
    start = getFullTimeDate(search_time);
    end = start + datetime.timedelta(days=period);
    res = Typhoon.objects.filter(f_dt_tfsj__gte=start, f_dt_tfsj__lte=end).values("f_vc_mz").distinct();
    names = [];
    typhoons_infos = {};
    one_typhoon_infos = [];
    for one in res:
        # 从数据库获取某台风的信息
        infos = Typhoon.objects.filter(f_dt_tfsj__gte=start, f_vc_mz=one["f_vc_mz"]).order_by('f_dt_tfsj');
        name = str(infos.values("f_dl_bh")[0]["f_dl_bh"]) + " " + one["f_vc_mz"];
        names.append(name);
        one_typhoon_infos = []
        for info in infos:
            one_typhoon_infos.append({'data_time':str(info.f_dt_tfsj.year)+'年'+str(info.f_dt_tfsj.month)+'月'
                                                  +str(info.f_dt_tfsj.day)+'日' +str(info.f_dt_tfsj.hour)+'时',
                                      'pressure':str(info.f_dl_zdqy)+'hPa',
                                 'strength_grade':str(info.f_dl_qd), 'wind_speed':str(info.f_dl_zdfs)+"m/s"});
        typhoons_infos[name] = one_typhoon_infos;
    finalRes = {"name":names, 'typhoons_infos':typhoons_infos};
    #print(finalRes)
    return finalRes;

# 获取所有的台风信息
def search_all_typhoon_info():
    res = Typhoon.objects.filter().values("f_vc_mz").distinct();
    names = [];
    typhoons_infos = {};
    one_typhoon_infos = [];
    for one in res:
        # 从数据库获取某台风的信息
        infos = Typhoon.objects.filter(f_vc_mz=one["f_vc_mz"]).order_by('f_dt_tfsj');
        if one["f_vc_mz"] == "nameless":
            continue
        name = str(infos.values("f_dl_bh")[0]["f_dl_bh"]) + " " + one["f_vc_mz"];
        names.append(name);
        one_typhoon_infos = []
        for info in infos:
            one_typhoon_infos.append({'data_time':str(info.f_dt_tfsj.year)+'年'+str(info.f_dt_tfsj.month)+'月'
                                                  +str(info.f_dt_tfsj.day)+'日' +str(info.f_dt_tfsj.hour)+'时',
                                      'pressure':str(info.f_dl_zdqy)+'hPa',
                                 'strength_grade':str(info.f_dl_qd), 'wind_speed':str(info.f_dl_zdfs)+"m/s"});
        typhoons_infos[name] = one_typhoon_infos;
    finalRes = {"name":names, 'typhoons_infos':typhoons_infos};
    return finalRes;
    
# 获取某台风的路径信息，不同的路径节点因为台风强度不同，显示不同的颜色
def search_typhoon_path_info(search_time, name):
    time = getFullTimeHour(search_time);
    data = {"passed": [],
            "unpassed": [],
            "current_pos": [],
            "path":[],
            "point_color":[]
            };
    # 不同等级对应的颜色
    points_colors=["#6BA4E8", "#333338", "#82ED6A", "#F3914B","#6D6CE3","#EA426D","#DDCB43","","","#82E4DA"]
    if len(Typhoon.objects.filter(f_dt_tfsj=time, f_vc_mz=name)) ==0:
        return data;
    # 数据库查询数据，按照台风时间排序
    infos = Typhoon.objects.filter(f_dt_tfsj__lte=time, f_vc_mz=name).order_by('f_dt_tfsj');
    for info in infos:
        lon = str(info.f_dl_jd/10);
        lat = str(info.f_dl_wd/10);
        data["passed"].append([lon, lat]);
    infos = Typhoon.objects.filter(f_dt_tfsj__gte=time, f_vc_mz=name).order_by('f_dt_tfsj');
    for info in infos:
        lon = str(info.f_dl_jd / 10);
        lat = str(info.f_dl_wd / 10);
        data["unpassed"].append([lon, lat]);
    infos = Typhoon.objects.filter(f_dt_tfsj=time, f_vc_mz=name).order_by('f_dt_tfsj');
    for info in infos:
        lon = str(info.f_dl_jd / 10);
        lat = str(info.f_dl_wd / 10);
        data["current_pos"].append([lon, lat]);
    infos = Typhoon.objects.filter(f_vc_mz=name).order_by('f_dt_tfsj');
    for info in infos:
        lon = str(info.f_dl_jd / 10);
        lat = str(info.f_dl_wd / 10);
        data["path"].append([lon, lat]);
        data["point_color"].append(points_colors[int(info.f_dl_qd)])
    #print(data)
    return data;
    
# 根据台风名称，获取台风的路径信息
def search_histoty_typhoon_path_info(name):
    data = {"passed": [],
            "unpassed": [],
            "current_pos": [],
            "path":[],
            "point_color": []
            };
    points_colors = ["#6BA4E8", "#333338", "#82ED6A", "#F3914B", "#6D6CE3", "#EA426D", "#DDCB43", "", "", "#82E4DA"]
    radius = []
    if len(Typhoon.objects.filter(f_vc_mz=name)) ==0:
        return data;
    # 从数据库查找该台风的信息，按照时间排序
    infos = Typhoon.objects.filter(f_vc_mz=name).order_by('f_dt_tfsj');
    strength_infos=[]
    strengths=[]
    one_strength_infos=[]
    for info in infos:
        # 根据强度值确定台风影响半径
        if (int(info.f_dl_qd) >= 3 ):
            radius.append("100");
        else:
            radius.append("450");
        lon = str(info.f_dl_jd/10);
        lat = str(info.f_dl_wd/10);
        data["passed"].append([lon, lat]);
        data["path"].append([lon, lat]);
        data["point_color"].append(points_colors[int(info.f_dl_qd)])
        if len(strengths) == 0:
            strengths.append(str(info.f_dl_qd))
            one_strength_infos=[]
            one_strength_infos.append(info.f_dt_tfsj)
        else:
            if str(info.f_dl_qd) != strengths[-1]:
                one_strength_infos.append(last_time)
                strength_infos.append(one_strength_infos)
                strengths.append(str(info.f_dl_qd))
                one_strength_infos = []
                one_strength_infos.append(info.f_dt_tfsj)
        if infos[len(infos)-1] == info:
            one_strength_infos.append(info.f_dt_tfsj)
            strength_infos.append(one_strength_infos)
        last_time = info.f_dt_tfsj

    if len(data["passed"]) > 0:
        #data["current_pos"].append(data["passed"][math.floor(len(data["passed"])/2)]);
        data["current_pos"].append(data["passed"][-1]);
    else:
        data["current_pos"]=[120.00, 20.00];
    # 获取台风路径上的时间信息，按照特定的时间格式显示
    for index in range(len(strength_infos)):
        strength_infos[index][0] = strength_infos[index][0].strftime('%Y-%m/%d %H:%M:%S.0')
        strength_infos[index][1] = strength_infos[index][1].strftime('%Y/%m/%d %H:%M:%S.0')
    for info in infos:
        data['info'] = str(info.f_dl_bh) + ' ' + info.f_vc_mz;
        break;

    data["strength_infos"] = strength_infos;
    data["strengths"] = strengths;
    data['radius'] = radius;
    #print(data)
    return data;


# 获取船只信息
def getShipInfo():
    html = urllib.request.urlopen(r'http://218.205.125.142:10080/transMethod.do?cmd=0x51fe&param=eyJzZXEiOjAsInBzIjoxMDAsInBpIjowLCJsYiI6IjEyMS4xMDg2OTIzOTMzNTY3MiwzMS4wNjczNTk3OTAzMjk1MSIsInJ0IjoiMTIyLjEyMDEyMTIyNjM2MTAyLDMxLjU5NjM5MDEzNjQxMjkxNCIsImNpcmNsZSI6IiJ9');
    hjson = json.loads(html.read().decode('utf-8'))
    ShipInfo.objects.all().delete();
    for i in range(len(hjson['ships'])):
        mmsi = hjson['ships'][i]['mmsi']
        info_time = int(hjson['ships'][i]['time'])
        time = datetime.datetime.fromtimestamp(info_time)
        lon = hjson['ships'][i]['lon']
        lat = hjson['ships'][i]['lat']
        name = hjson['ships'][i]['name']
        ship_type = hjson['ships'][i]['ship_type']
        callsign = hjson['ships'][i]['callsign']
        # 将船只接口的船只信息写入数据库
        if len(ShipInfo.objects.filter(mmsi=mmsi, time=time, lon=lon, lat=lat, name=name, ship_type=ship_type, callsign=callsign)) == 0:
            res = ShipInfo.objects.create(mmsi=mmsi, time=time, lon=lon, lat=lat, name=name, ship_type=ship_type,callsign=callsign);
            res.save();

# 定义地球半径
EARTH_REDIUS = 6378.137

def rad(d):
    return d * math.pi / 180.0

# 获取两个经纬度节点之间的距离
def getDistance(lat1, lng1, lat2, lng2):
    radLat1 = rad(lat1)
    radLat2 = rad(lat2)
    a = radLat1 - radLat2
    b = rad(lng1) - rad(lng2)
    s = 2 * math.asin(math.sqrt(math.pow(math.sin(a/2), 2) + math.cos(radLat1) * math.cos(radLat2) * math.pow(math.sin(b/2), 2)))
    s = s * EARTH_REDIUS
    return s


# 获取经纬度为中心，带半径范围内的船只
def getCirclesShips(lat, lng, radius):
    res = TyphoonShipInfo.objects.all();
    ships = [];
    ship_infos=[];
    for one in res:
        #print(float(one.lat))
        #print(float(one.lon))
        # 计算两个点之间的距离
        dis = getDistance(float(one.f_dl_wd), float(one.f_dl_jd), lat, lng);
        #print(dis);
        # 小于半径的船只信息，添加到返回值
        if  dis <= radius:
            one_ship = {'name':one.f_vc_mz, 'mmsi':one.f_vc_mmsi, 'callsign':one.f_vc_hh, 'ship_type':str(one.f_it_czlx), 'distance':'{:.2f}'.format(dis)};
            ships.append(one_ship);
    return ships;

# 获取经纬度为中心，带半径范围内的船只
def getCirclesShipsWithPos(lat, lng, radius):
    res = TyphoonShipInfo.objects.all();
    ship_infos=[];
    for one in res:
        # 计算两个点之间的距离
        dis = getDistance(float(one.f_dl_wd), float(one.f_dl_jd), lat, lng);
        if  dis <= radius:
            ship_infos.append({'name':one.f_vc_mz, 'mmsi':one.f_vc_mmsi, 'callsign':one.f_vc_hh,
                               'ship_type':str(one.f_it_czlx), 'distance':'{:.2f}'.format(dis),
                               'lon': str(one.f_dl_jd), 'lat': str(one.f_dl_wd)})
    return ship_infos;




