from climateApp.models import *
import sys
import datetime
import urllib
import json
import math
import urllib.request

'''
def insertAreaShipInfo():
    html = urllib.request.urlopen(r'http://218.205.125.144:9600/RTData/AisPosArea?left=105&right=135&top=0&bottom=40');
    hjson = json.loads(html.read().decode('utf-8'))
    ShipInfo.objects.all().delete();
    for i in range(len(hjson)):
        mmsi = hjson[i]['i']
        info_time = int(hjson[i]['time'])
        time = datetime.datetime.fromtimestamp(info_time)
        lon = hjson[i]['lon']
        lat = hjson[i]['lat']
        ship_type = hjson[i]['ship_type']
        cog = hjson[i]['cog']

        if len(ShipInfo.objects.filter(mmsi=mmsi, time=time, lon=lon, lat=lat, ship_type=ship_type, cog=cog)) == 0:
            res = ShipInfo.objects.create(id=i+1, mmsi=mmsi, time=time, lon=lon, lat=lat, ship_type=ship_type,cog=cog);
            res.save();
    print(len(hjson))
'''
# 根据船只编号，对船只进行分类
def getColorIndex(num):
    if num >=60 and num<=69:
        return 0;
    if num >=70 and num<=79:
        return 1;
    if num >=80 and num<=89:
        return 2;
    if num==51 or num==55:
        return 3;
    if num==54:
        return 4;
    return 5;
# 获取所有船只信息     
def getAreaShipInfo():
    res = ShipInfo.objects.all();
    mmsi_ships={}
    color_dicts={0:"blue", 1:"Chartreuse",2:"Brown",3:"DarkCyan",4:"DarkOrchid", 5: "DarkGray"}
    color_nums= {0:0, 1:0,2:0,3:0,4:0, 5:0}
    # 遍历每一只船，根据编号获取其对应的显示颜色等信息
    for one in res:
        if getColorIndex(one.f_it_czlx) in color_dicts.keys():
            if color_nums[getColorIndex(one.f_it_czlx)] <1000 :
                mmsi_ships[one.f_vc_mmsi] = [str(one.f_dl_jd), str(one.f_dl_wd), color_dicts[getColorIndex(one.f_it_czlx)], str(one.f_vc_mmsi)]
                color_nums[getColorIndex(one.f_it_czlx)] +=1;
    return mmsi_ships;

# 根据mmsi编号，获取某只船的信息
def getShipInfoBymmsi(mmsi):
    res = ShipInfo.objects.filter(f_vc_mmsi=mmsi);
    if len(res) == 0:
        return {}
    else:
        for one in res:
            return {"mmsi": one.f_vc_mmsi, 'cog':str(one.f_it_hjx), 'lon':str(one.f_dl_jd), 'lat':str(one.f_dl_wd), 'ship_type':str(getColorIndex(one.f_it_czlx))}



