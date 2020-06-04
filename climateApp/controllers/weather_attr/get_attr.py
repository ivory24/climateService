import os
from climateApp.controllers.typhoon.manage import *
import math
import json

# 目标区域页面，网格划分之后，获取某经纬度对应的网格index
def getIndex(lat, long, start_lat_v, start_long_v, precision, num_lat):
    start_long = float(start_long_v);
    start_lat = float(start_lat_v);
    long_index = math.ceil((long - start_long) / precision);
    lat_index = math.ceil((lat - start_lat) / precision) % num_lat;
    return long_index*num_lat+lat_index+1;


'''

def getTemperature(lat, long, precision, date):
    res = TemperatureAttrs.objects.filter(start_longitude__lte=long, start_latitude__lte=lat, end_longitude__gte=long,
                                    end_latitude__gte=lat,data_time=date, precision=precision);
    for one in res:
        json_data = one.json_temperature;
        list_data = json.loads(json_data);
        return list_data[getIndex(lat, long, one.start_latitude, one.start_longitude, precision, one.num_lat)]
    return;




def getPressure(lat, long, precision, date):
    res = PressureAttrs.objects.filter(start_longitude__lte=long, start_latitude__lte=lat, end_longitude__gte=long,
                                          end_latitude__gte=lat, data_time=date, precision=precision);
    for one in res:
        json_data = one.json_pressure;
        list_data = json.loads(json_data);
        return list_data[getIndex(lat, long, one.start_latitude, one.start_longitude, precision, one.num_lat)]
    return;


def getPrecipitation(lat, long, precision, date):
    res = PrecipitationAttrs.objects.filter(start_longitude__lte=long, start_latitude__lte=lat, end_longitude__gte=long,
                                       end_latitude__gte=lat, data_time=date, precision=precision);
    for one in res:
        json_data = one.json_precipitation;
        list_data = json.loads(json_data);
        return list_data[getIndex(lat, long, one.start_latitude, one.start_longitude, precision, one.num_lat)]
    return;


def getWindSpeed(lat, long, precision, date):
    res = WindSpeedAttrs.objects.filter(start_longitude__lte=long, start_latitude__lte=lat, end_longitude__gte=long,
                                       end_latitude__gte=lat, data_time=date, precision=precision);
    for one in res:
        json_data = one.json_wind_speed;
        list_data = json.loads(json_data);
        return list_data[getIndex(lat, long, one.start_latitude, one.start_longitude, precision, one.num_lat)]
    return;

def getWindComponent(lat, long, precision, date):
    res = WindComponentAttrs.objects.filter(start_longitude__lte=long, start_latitude__lte=lat, end_longitude__gte=long,
                                       end_latitude__gte=lat, data_time=date, precision=precision);
    for one in res:
        json_data = one.json_wind_component;
        list_data = json.loads(json_data);
        return list_data[getIndex(lat, long, one.start_latitude, one.start_longitude, precision, one.num_lat)]
    return;


def getVisibility(lat, long, precision, date):
    res = VisibilityAttrs.objects.filter(start_longitude__lte=long, start_latitude__lte=lat, end_longitude__gte=long,
                                       end_latitude__gte=lat, data_time=date, precision=precision);
    for one in res:
        json_data = one.json_visibility;
        list_data = json.loads(json_data);
        return list_data[getIndex(lat, long, one.start_latitude, one.start_longitude, precision, one.num_lat)]
    return;

def getSeaWave(lat, long, precision, date):
    res = SeaWaveAttrs.objects.filter(start_longitude__lte=long, start_latitude__lte=lat, end_longitude__gte=long,
                                       end_latitude__gte=lat, data_time=date, precision=precision);
    for one in res:
        json_data = one.json_sea_wave;
        list_data = json.loads(json_data);
        return list_data[getIndex(lat, long, one.start_latitude, one.start_longitude, precision, one.num_lat)]
    return;

def getHeightSwell(lat, long, precision, date):
    res = HeightSwellAttrs.objects.filter(start_longitude__lte=long, start_latitude__lte=lat, end_longitude__gte=long,
                                       end_latitude__gte=lat, data_time=date, precision=precision);
    for one in res:
        json_data = one.json_height_swell;
        list_data = json.loads(json_data);
        return list_data[getIndex(lat, long, one.start_latitude, one.start_longitude, precision, one.num_lat)]
    return;

def getPeriodSwell(lat, long, precision, date):
    res = PeriodSwellAttrs.objects.filter(start_longitude__lte=long, start_latitude__lte=lat, end_longitude__gte=long,
                                       end_latitude__gte=lat, data_time=date, precision=precision);
    for one in res:
        json_data = one.json_period_swell;
        list_data = json.loads(json_data);
        return list_data[getIndex(lat, long, one.start_latitude, one.start_longitude, precision, one.num_lat)]
    return;

def getDirectionSwell(lat, long, precision, date):
    res = DirectionSwellAttrs.objects.filter(start_longitude__lte=long, start_latitude__lte=lat, end_longitude__gte=long,
                                       end_latitude__gte=lat, data_time=date, precision=precision);
    for one in res:
        json_data = one.json_direction_swell;
        list_data = json.loads(json_data);
        return list_data[getIndex(lat, long, one.start_latitude, one.start_longitude, precision, one.num_lat)]
    return;

def getOceanCurrentU(lat, long, precision, date):
    res = OceanCurrentUAttrs.objects.filter(start_longitude__lte=long, start_latitude__lte=lat, end_longitude__gte=long,
                                       end_latitude__gte=lat, data_time=date, precision=precision);
    for one in res:
        json_data = one.json_ocean_current_u;
        list_data = json.loads(json_data);
        return list_data[getIndex(lat, long, one.start_latitude, one.start_longitude, precision, one.num_lat)]
    return;

def getOceanCurrentW(lat, long, precision, date):
    res = OceanCurrentWAttrs.objects.filter(start_longitude__lte=long, start_latitude__lte=lat, end_longitude__gte=long,
                                       end_latitude__gte=lat, data_time=date, precision=precision);
    for one in res:
        json_data = one.json_ocean_current_w;
        list_data = json.loads(json_data);
        return list_data[getIndex(lat, long, one.start_latitude, one.start_longitude, precision, one.num_lat)]
    return;

def getOceanCurrentV(lat, long, precision, date):
    res = OceanCurrentVAttrs.objects.filter(start_longitude__lte=long, start_latitude__lte=lat, end_longitude__gte=long,
                                       end_latitude__gte=lat, data_time=date, precision=precision);
    for one in res:
        json_data = one.json_ocean_current_v;
        list_data = json.loads(json_data);
        return list_data[getIndex(lat, long, one.start_latitude, one.start_longitude, precision, one.num_lat)]
    return;

def getOceanCurrentT(lat, long, precision, date):
    res = OceanCurrentTAttrs.objects.filter(start_longitude__lte=long, start_latitude__lte=lat, end_longitude__gte=long,
                                       end_latitude__gte=lat, data_time=date, precision=precision);
    for one in res:
        json_data = one.json_ocean_current_t;
        list_data = json.loads(json_data);
        return list_data[getIndex(lat, long, one.start_latitude, one.start_longitude, precision, one.num_lat)]
    return;

def getOceanCurrentH(lat, long, precision, date):
    res = OceanCurrentHAttrs.objects.filter(start_longitude__lte=long, start_latitude__lte=lat, end_longitude__gte=long,
                                       end_latitude__gte=lat, data_time=date, precision=precision);
    for one in res:
        json_data = one.json_ocean_current_h;
        list_data = json.loads(json_data);
        return list_data[getIndex(lat, long, one.start_latitude, one.start_longitude, precision, one.num_lat)]
    return;

def getHumidity(lat, long, precision, date):
    res = HumidityAttrs.objects.filter(start_longitude__lte=long, start_latitude__lte=lat, end_longitude__gte=long,
                                       end_latitude__gte=lat, data_time=date, precision=precision);
    for one in res:
        json_data = one.json_humidity;
        list_data = json.loads(json_data);
        return list_data[getIndex(lat, long, one.start_latitude, one.start_longitude, precision, one.num_lat)]
    return;
'''
# 根据经纬度、时间、精度获取叠加在一起的hash值，用于数据库的尽快查找
def getHashValue(lon, lat, precision_int, hour_int):
    if (precision_int == 5):
        return int(lon*1000000000 + lat*100000 + hour_int);
    else:
        return int(lon * 1000000000 + lat * 100000 + 100 + hour_int);


# log文件接口，调用这个接口，可以将命令行的输出信息保存到文件中
def debugOutputFile(content):
    f = open("/home/code/climateServices/log.txt", "a+")
    f.writelines(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "： ");
    f.writelines(str(content) + "\n")
    f.close()

# 获取特定数据表的经纬度对应的天气信息
def getWeatherAttrs20170101(lat, long, precision, hour_num):
    data_hv = getHashValue(long, lat, precision*100, hour_num)
    debugOutputFile(data_hv);
    if (len(WeatherAttrs20170101.objects.filter(idx_b_hyqx_20170101_uk=data_hv)) != 0):
        res = WeatherAttrs20170101.objects.filter(idx_b_hyqx_20170101_uk=data_hv);
        for one_weather_attrs in res:
            weather_attrs = {"temperature": str(one_weather_attrs.f_dl_wnd), "pressure": str(one_weather_attrs.f_dl_qy),
                         "precipitation": str(one_weather_attrs.f_dl_jyl),
                         "wind_speed": str(one_weather_attrs.f_dl_fs),
                         "wind_component": str(one_weather_attrs.f_dl_fx),
                         "visibility": str(one_weather_attrs.f_it_njd),
                         "sea_wave": str(one_weather_attrs.f_dl_hl),
                         "height_swell": str(one_weather_attrs.f_dl_ylgd),
                         "period_swell": str(one_weather_attrs.f_dl_ylzq),
                         "direction_swell": str(one_weather_attrs.f_dl_ylfx),
                         "ocean_current_h": str(one_weather_attrs.f_dl_hlsw),
                         "ocean_current_t": str(one_weather_attrs.f_dl_hlwd),
                         "ocean_current_u": str(one_weather_attrs.f_dl_xl),
                         "ocean_current_v": str(one_weather_attrs.f_dl_yl),
                         "ocean_current_w": str(one_weather_attrs.f_dl_zl),
                         "humidity": str(one_weather_attrs.f_dl_xdsd)}
    else:
        weather_attrs = {}
    return weather_attrs;

# 获取某经纬度、精度在当前时间对应的天气信息
def getWeatherAttrs(lat, long, precision):

    now_date = datetime.datetime.now()
    now_month = str(now_date.month)
    now_day = str(now_date.day)

    if (len(now_month) < 2):
        now_month = '0' + now_month
    if (len(now_day) < 2):
        now_day = '0' + now_day
    now_hour = now_date.hour

    data_hv = getHashValue(long, lat, precision*100, now_hour)
    res = eval("WeatherAttrs2017" + now_month + now_day + ".objects.filter(idx_b_hyqx_2017" + now_month + now_day + "_uk=data_hv)");
    if (len(res) != 0):
        for one_weather_attrs in res:
            #debugOutputFile("have value****************")
            weather_attrs = {"temperature": str(one_weather_attrs.f_dl_wnd+30), "pressure": str(one_weather_attrs.f_dl_qy),
                         "precipitation": str(one_weather_attrs.f_dl_jyl),
                         "wind_speed": str(one_weather_attrs.f_dl_fs),
                         "wind_component": str(one_weather_attrs.f_dl_fx),
                         "visibility": str(one_weather_attrs.f_it_njd),
                         "sea_wave": str(one_weather_attrs.f_dl_hl),
                         "height_swell": str(one_weather_attrs.f_dl_ylgd),
                         "period_swell": str(one_weather_attrs.f_dl_ylzq),
                         "direction_swell": str(one_weather_attrs.f_dl_ylfx),
                         "ocean_current_h": str(one_weather_attrs.f_dl_hlsw),
                         "ocean_current_t": str(one_weather_attrs.f_dl_hlwd),
                         "ocean_current_u": str(one_weather_attrs.f_dl_xl),
                         "ocean_current_v": str(one_weather_attrs.f_dl_yl),
                         "ocean_current_w": str(one_weather_attrs.f_dl_zl),
                         "humidity": str(one_weather_attrs.f_dl_xdsd)}
    else:
        weather_attrs = {}
    return weather_attrs;
# 获取某经纬度、精度在某年某月某小时+delay对应的天气信息
def getWeatherAttrsWithDelay(lat, long, precision, delay):

    now_date = datetime.datetime.now() + datetime.timedelta(days=delay);
    now_month = str(now_date.month)
    now_day = str(now_date.day)

    if (len(now_month) < 2):
        now_month = '0' + now_month
    if (len(now_day) < 2):
        now_day = '0' + now_day
    now_hour = now_date.hour

    data_hv = getHashValue(long, lat, precision*100, now_hour)
    res = eval("WeatherAttrs2017" + now_month + now_day + ".objects.filter(idx_b_hyqx_2017" + now_month + now_day + "_uk=data_hv)");
    if (len(res) != 0):
        for one_weather_attrs in res:
            #debugOutputFile("have value****************")
            weather_attrs = {"temperature": str(one_weather_attrs.f_dl_wnd+30), "pressure": str(one_weather_attrs.f_dl_qy),
                         "precipitation": str(one_weather_attrs.f_dl_jyl),
                         "wind_speed": str(one_weather_attrs.f_dl_fs),
                         "wind_component": str(one_weather_attrs.f_dl_fx),
                         "visibility": str(one_weather_attrs.f_it_njd),
                         "sea_wave": str(one_weather_attrs.f_dl_hl),
                         "height_swell": str(one_weather_attrs.f_dl_ylgd),
                         "period_swell": str(one_weather_attrs.f_dl_ylzq),
                         "direction_swell": str(one_weather_attrs.f_dl_ylfx),
                         "ocean_current_h": str(one_weather_attrs.f_dl_hlsw),
                         "ocean_current_t": str(one_weather_attrs.f_dl_hlwd),
                         "ocean_current_u": str(one_weather_attrs.f_dl_xl),
                         "ocean_current_v": str(one_weather_attrs.f_dl_yl),
                         "ocean_current_w": str(one_weather_attrs.f_dl_zl),
                         "humidity": str(one_weather_attrs.f_dl_xdsd)}
    else:
        weather_attrs = {}
    return weather_attrs;

# 获取某经纬度、精度在某年某月某小时+delay对应的天气信息
def getWeatherAttrsByTime(lat, long, precision, month_v, day_v, hour_v):
    if (len(month_v) < 2):
        month_v = '0' + month_v
    if (len(day_v) < 2):
        day_v = '0' + day_v
    if(month_v == "02" and day_v == "29"):
        day_v = "28";

    data_hv = getHashValue(long, lat, precision*100, hour_v)
    res = eval("WeatherAttrs2017" + month_v + day_v + ".objects.filter(idx_b_hyqx_2017" + month_v + day_v + "_uk=data_hv)");
    # debugOutputFile("hhhhhhhhhhhhhhhhhh")
    if (len(res) != 0):
        for one_weather_attrs in res:
            # debugOutputFile(str(lat) + " " + str(long))
            weather_attrs = {"temperature": str(one_weather_attrs.f_dl_wnd+30), "pressure": str(one_weather_attrs.f_dl_qy),
                         "precipitation": str(one_weather_attrs.f_dl_jyl),
                         "wind_speed": str(one_weather_attrs.f_dl_fs),
                         "wind_component": str(one_weather_attrs.f_dl_fx),
                         "visibility": str(one_weather_attrs.f_it_njd),
                         "sea_wave": str(one_weather_attrs.f_dl_hl),
                         "height_swell": str(one_weather_attrs.f_dl_ylgd),
                         "period_swell": str(one_weather_attrs.f_dl_ylzq),
                         "direction_swell": str(one_weather_attrs.f_dl_ylfx),
                         "ocean_current_h": str(one_weather_attrs.f_dl_hlsw),
                         "ocean_current_t": str(one_weather_attrs.f_dl_hlwd),
                         "ocean_current_u": str(one_weather_attrs.f_dl_xl),
                         "ocean_current_v": str(one_weather_attrs.f_dl_yl),
                         "ocean_current_w": str(one_weather_attrs.f_dl_zl),
                         "humidity": str(one_weather_attrs.f_dl_xdsd)}
    else:
        weather_attrs = {}
    return weather_attrs;
# 获取20120102的某经纬度、某精度、某小时对应的天气情况
def getWeatherAttrs20170102(lat, long, precision, hour_num):
    data_hv = getHashValue(long, lat, precision*100, hour_num);
    debugOutputFile(data_hv);
    if len(WeatherAttrs20170102.objects.filter(idx_b_hyqx_20170102_uk=data_hv)) != 0:
        res = WeatherAttrs20170102.objects.filter(idx_b_hyqx_20170102_uk=data_hv);
        for one_weather_attrs in res:
            weather_attrs = {"temperature": str(one_weather_attrs.f_dl_wnd), "pressure": str(one_weather_attrs.f_dl_qy),
                         "precipitation": str(one_weather_attrs.f_dl_jyl),
                         "wind_speed": str(one_weather_attrs.f_dl_fs),
                         "wind_component": str(one_weather_attrs.f_dl_fx),
                         "visibility": str(one_weather_attrs.f_it_njd),
                         "sea_wave": str(one_weather_attrs.f_dl_hl),
                         "height_swell": str(one_weather_attrs.f_dl_ylgd),
                         "period_swell": str(one_weather_attrs.f_dl_ylzq),
                         "direction_swell": str(one_weather_attrs.f_dl_ylfx),
                         "ocean_current_h": str(one_weather_attrs.f_dl_hlsw),
                         "ocean_current_t": str(one_weather_attrs.f_dl_hlwd),
                         "ocean_current_u": str(one_weather_attrs.f_dl_xl),
                         "ocean_current_v": str(one_weather_attrs.f_dl_yl),
                         "ocean_current_w": str(one_weather_attrs.f_dl_zl),
                         "humidity": str(one_weather_attrs.f_dl_xdsd)}
    else:
        weather_attrs = {}
    return weather_attrs;


'''
def getWeatherAttrs(lat, long, precision, date):
    if len(WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date, precision=precision)) == 0:
        temperature = getTemperature(lat, long, precision, date);
        if (temperature==None):
            return [];
        pressure = getPressure(lat, long, precision, date);
        precipitation = getPrecipitation(lat, long, precision, date);
        wind_speed = getWindSpeed(lat, long, precision, date);
        wind_component = getWindComponent(lat, long, precision, date);
        visibility = getVisibility(lat, long, precision, date);
        sea_wave = getSeaWave(lat, long, precision, date);
        height_swell = getHeightSwell(lat, long, precision, date);
        period_swell = getPeriodSwell(lat, long, precision, date);
        direction_swell = getDirectionSwell(lat, long, precision, date);
        ocean_current_h = getOceanCurrentH(lat, long, precision, date);
        ocean_current_t = getOceanCurrentT(lat, long, precision, date);
        ocean_current_u = getOceanCurrentU(lat, long, precision, date);
        ocean_current_v = getOceanCurrentV(lat, long, precision, date);
        ocean_current_w = getOceanCurrentW(lat, long, precision, date);
        humidity = getHumidity(lat, long, precision, date);

        res = WeatherAttrs.objects.create(longitude=long, latitude=lat, data_time=date, precision=precision,
                                temperature=temperature, pressure=pressure, precipitation=precipitation, wind_speed=wind_speed,
                                wind_component=wind_component, visibility=visibility, sea_wave=sea_wave,
                                height_swell=height_swell, period_swell=period_swell, direction_swell=direction_swell,
                                ocean_current_h=ocean_current_h, ocean_current_t=ocean_current_t, ocean_current_u=ocean_current_u,
                                ocean_current_v=ocean_current_v, ocean_current_w=ocean_current_w, humidity=humidity);
        res.save();
    one_weather_attrs = WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date, precision=precision)[0];
    if one_weather_attrs:
        weather_attrs = {"temperature": str(one_weather_attrs.temperature), "pressure": str(one_weather_attrs.pressure),
                      "precipitation": str(one_weather_attrs.precipitation),"wind_speed": str(one_weather_attrs.wind_speed),
                      "wind_component": str(one_weather_attrs.wind_component),"visibility": str(one_weather_attrs.visibility),
                      "sea_wave": str(one_weather_attrs.sea_wave), "height_swell": str(one_weather_attrs.height_swell),
                      "period_swell": str(one_weather_attrs.period_swell),"direction_swell": str(one_weather_attrs.direction_swell),
                      "ocean_current_h": str(one_weather_attrs.ocean_current_h),"ocean_current_t": str(one_weather_attrs.ocean_current_t),
                      "ocean_current_u": str(one_weather_attrs.ocean_current_u),"ocean_current_v": str(one_weather_attrs.ocean_current_v),
                      "ocean_current_w": str(one_weather_attrs.ocean_current_w),
                      "humidity": str(one_weather_attrs.humidity)}
    else:
        weather_attrs={}
    return weather_attrs;
'''
# 获取某经纬度、某精度在未来2天时间内的天气属性信息
def getWeatherAttrsForWeek(lat, long, precision):
    res={};
    res['temperature']=[]
    res['date_info']=[]
    res['humidity']=[]
    res["wind_speed"]=[]
    res["wind_component"]=[]
    res["precipitation"]=[]
    res["visibility"]=[]
    res["sea_wave"]=[]
    res["height_swell"]=[]
    res["ocean_current_h"]=[]

    now_date = datetime.datetime.now()

    for i in range(48):
        cur_date = now_date + datetime.timedelta(hours=i);
        cur_month = str(cur_date.month)
        cur_day = str(cur_date.day)
        cur_hour = cur_date.hour

        data = getWeatherAttrsByTime(lat, long, precision, cur_month, cur_day, cur_hour);
        res['temperature'].append(data["temperature"]);
        res['date_info'].append(cur_date.strftime('%Y年%m月%d日 %H时'));
        res['humidity'].append(data["humidity"]);
        res['wind_speed'].append(data["wind_speed"]);
        res['wind_component'].append(data["wind_component"]);
        res['precipitation'].append(data["precipitation"]);
        res['visibility'].append(data["visibility"]);
        res['sea_wave'].append(data["sea_wave"]);
        res['height_swell'].append(data["height_swell"]);
        res['ocean_current_h'].append(data["ocean_current_h"])
    return res;
