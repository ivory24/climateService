from climateApp.models import *
import os
from climateApp.controllers.typhoon.manage import *
import math
import json
import numpy as np
from climateApp.controllers.weather_attr.get_attr import *

'''
def insertWeather_attr():
    #insert 起始点 经度long105 纬度lat0
    if len(WeatherAttrs.objects.filter(longitude=105, latitude=0, data_time="2017-01-01 00:00:00", precision=0.05)) == 0:
        WeatherAttrs.objects.create(longitude=105, latitude=0, data_time="2017-01-01 00:00:00", precision=0.05,
                                temperature=28.26, pressure=934.70, precipitation=0.00, wind_speed=1.94,
                                wind_component=306.81, visibility=0, sea_wave=0.81,
                                height_swell=2.31, period_swell=2.50, direction_swell=126.81,
                                ocean_current_h=0.86, ocean_current_t=19.08, ocean_current_u=-1.45, ocean_current_v=-29.22, ocean_current_w=-0.0019,
                                humidity=100.00);
    return;

def clearAttrsTables():
    TemperatureAttrs.objects.all().delete();
    PressureAttrs.objects.all().delete();
    PrecipitationAttrs.objects.all().delete();
    WindSpeedAttrs.objects.all().delete();
    WindComponentAttrs.objects.all().delete();
    VisibilityAttrs.objects.all().delete();
    SeaWaveAttrs.objects.all().delete();

    HeightSwellAttrs.objects.all().delete();
    PeriodSwellAttrs.objects.all().delete();
    DirectionSwellAttrs.objects.all().delete();

    OceanCurrentWAttrs.objects.all().delete();
    OceanCurrentVAttrs.objects.all().delete();
    OceanCurrentUAttrs.objects.all().delete();
    OceanCurrentTAttrs.objects.all().delete();
    OceanCurrentHAttrs.objects.all().delete();
    HumidityAttrs.objects.all().delete();


def insertAttrFileData(file_dir):
    clearAttrsTables();
    res = file_name(file_dir);
    i = 0;
    for one in res:
        parseFilePattern3(file_dir, one);
        i+=1;
        print("*********" + str(i) + "************");

def parseFilePattern2(file_dir, filename):
    file = open(file_dir+ "/" + filename, 'r')
    header = file.readline();
    timeinfo = file.readline();
    if timeinfo[0]=='1':
        dateinfo = "20" + timeinfo.strip().replace(' ','')[0:-2];
    else:
        dateinfo = timeinfo.strip().replace(' ', '')[0:-2];
    print(filename);
    date = getFullTimeHour(dateinfo);
    slices = filename.split('_');
    attr = ""
    for i in range(len(slices)-2):
        attr += slices[i]
    #if date.strftime('%Y-%m-%d %H:%M:%S') != "2017-01-01 04:00:00":
    #   return 0

    #WeatherAttrs.objects.all().delete();
    type = slices[-2]

    posinfo = file.readline().split(' ');
    precision = float(posinfo[0])
    startlat = float(posinfo[4])
    endlat = float(posinfo[5])
    startlong = float(posinfo[2])
    endlong = float(posinfo[3])

    otherinfo = file.readline().split(' ');
    longnum = int(otherinfo[0])
    latnum = int(otherinfo[1])

    line_info = file.readline().strip('\n');
    count = 0;
    all_datas = []

    while line_info:
        datainfo = line_info.split(' ');
        all_datas += datainfo;
        line_info = file.readline().strip('\n');

    json_all_datas = json.dumps(all_datas);

    if attr == "Temperatureheightaboveground":
        if len(TemperatureAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat, end_longitude=endlong, end_latitude=endlat,
                                               data_time=date, precision=precision, num_long=longnum, num_lat=latnum)) == 0:
            temp = TemperatureAttrs.objects.create(start_longitude=startlong, start_latitude=startlat, end_longitude=endlong, end_latitude=endlat,
                                               data_time=date, precision=precision, num_long=longnum, num_lat=latnum, json_temperature=json_all_datas);
            temp.save()
        else:
            return 0;
            #TemperatureAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat, end_longitude=endlong, end_latitude=endlat,
            #                                  data_time=date, precision=precision, num_long=longnum, num_lat=latnum).update(json_temperature=json_all_datas);
    elif (attr == "directionswell"):
        if len(DirectionSwellAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
                                               end_longitude=endlong, end_latitude=endlat,
                                               data_time=date, precision=precision, num_long=longnum,
                                               num_lat=latnum)) == 0:
            temp = DirectionSwellAttrs.objects.create(start_longitude=startlong, start_latitude=startlat,
                                                   end_longitude=endlong, end_latitude=endlat,
                                                   data_time=date, precision=precision, num_long=longnum,
                                                   num_lat=latnum, json_direction_swell=json_all_datas);
            temp.save()
        else:
            return 0;
            #DirectionSwellAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
            #                                       end_longitude=endlong, end_latitude=endlat,
            #                                       data_time=date, precision=precision, num_long=longnum,
            #                                       num_lat=latnum).update(json_direction_swell=json_all_datas);
    elif attr == "oceancurrenth":
        if len(OceanCurrentHAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
                                                  end_longitude=endlong, end_latitude=endlat,
                                                  data_time=date, precision=precision, num_long=longnum,
                                                  num_lat=latnum)) == 0:
            temp = OceanCurrentHAttrs.objects.create(start_longitude=startlong, start_latitude=startlat,
                                                      end_longitude=endlong, end_latitude=endlat,
                                                      data_time=date, precision=precision, num_long=longnum,
                                                      num_lat=latnum, json_ocean_current_h=json_all_datas);
            temp.save()
        else:
            return 0;
            #OceanCurrentHAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
            #                                          end_longitude=endlong, end_latitude=endlat,
            #                                          data_time=date, precision=precision, num_long=longnum,
            #                                          num_lat=latnum).update(json_ocean_current_h=json_all_datas);
    elif attr == "oceancurrentt":
        if len(OceanCurrentTAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
                                                 end_longitude=endlong, end_latitude=endlat,
                                                 data_time=date, precision=precision, num_long=longnum,
                                                 num_lat=latnum)) == 0:
            temp = OceanCurrentTAttrs.objects.create(start_longitude=startlong, start_latitude=startlat,
                                                     end_longitude=endlong, end_latitude=endlat,
                                                     data_time=date, precision=precision, num_long=longnum,
                                                     num_lat=latnum, json_ocean_current_t=json_all_datas);
            temp.save()
        else:
            return 0;
            #OceanCurrentTAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
            #                                         end_longitude=endlong, end_latitude=endlat,
            #                                         data_time=date, precision=precision, num_long=longnum,
            #                                         num_lat=latnum).update(json_ocean_current_t=json_all_datas);
    elif attr == "oceancurrentu":
        if len(OceanCurrentUAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
                                                 end_longitude=endlong, end_latitude=endlat,
                                                 data_time=date, precision=precision, num_long=longnum,
                                                 num_lat=latnum)) == 0:
            temp = OceanCurrentUAttrs.objects.create(start_longitude=startlong, start_latitude=startlat,
                                                     end_longitude=endlong, end_latitude=endlat,
                                                     data_time=date, precision=precision, num_long=longnum,
                                                     num_lat=latnum, json_ocean_current_u=json_all_datas);
            temp.save()
        else:
            return 0;
            #OceanCurrentUAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
            #                                         end_longitude=endlong, end_latitude=endlat,
            #                                         data_time=date, precision=precision, num_long=longnum,
            #                                         num_lat=latnum).update(json_ocean_current_u=json_all_datas);

    elif attr == "oceancurrentv":
        if len(OceanCurrentVAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
                                                 end_longitude=endlong, end_latitude=endlat,
                                                 data_time=date, precision=precision, num_long=longnum,
                                                 num_lat=latnum)) == 0:
            temp = OceanCurrentVAttrs.objects.create(start_longitude=startlong, start_latitude=startlat,
                                                     end_longitude=endlong, end_latitude=endlat,
                                                     data_time=date, precision=precision, num_long=longnum,
                                                     num_lat=latnum, json_ocean_current_v=json_all_datas);
            temp.save()
        else:
            return 0;
            #OceanCurrentVAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
            #                                         end_longitude=endlong, end_latitude=endlat,
            #                                         data_time=date, precision=precision, num_long=longnum,
            #                                         num_lat=latnum).update(json_ocean_current_v=json_all_datas);

    elif attr == "oceancurrentw":
        if len(OceanCurrentWAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
                                                 end_longitude=endlong, end_latitude=endlat,
                                                 data_time=date, precision=precision, num_long=longnum,
                                                 num_lat=latnum)) == 0:
            temp = OceanCurrentWAttrs.objects.create(start_longitude=startlong, start_latitude=startlat,
                                                     end_longitude=endlong, end_latitude=endlat,
                                                     data_time=date, precision=precision, num_long=longnum,
                                                     num_lat=latnum, json_ocean_current_w=json_all_datas);
            temp.save()
        else:
            return 0;
            #OceanCurrentWAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
            #                                         end_longitude=endlong, end_latitude=endlat,
            #                                         data_time=date, precision=precision, num_long=longnum,
            #                                         num_lat=latnum).update(json_ocean_current_w=json_all_datas);
    elif attr == "Windspeedheightaboveground":
        if len(WindSpeedAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
                                                 end_longitude=endlong, end_latitude=endlat,
                                                 data_time=date, precision=precision, num_long=longnum,
                                                 num_lat=latnum)) == 0:
            temp = WindSpeedAttrs.objects.create(start_longitude=startlong, start_latitude=startlat,
                                                     end_longitude=endlong, end_latitude=endlat,
                                                     data_time=date, precision=precision, num_long=longnum,
                                                     num_lat=latnum, json_wind_speed=json_all_datas);
            temp.save()
        else:
            return 0;
            #WindSpeedAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
            #                                  end_longitude=endlong, end_latitude=endlat,
            #                                  data_time=date, precision=precision, num_long=longnum,
            #                                  num_lat=latnum).update(json_wind_speed=json_all_datas);

    elif attr == "Windcomponentheightaboveground":
        if len(WindComponentAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
                                                 end_longitude=endlong, end_latitude=endlat,
                                                 data_time=date, precision=precision, num_long=longnum,
                                                 num_lat=latnum)) == 0:
            temp = WindComponentAttrs.objects.create(start_longitude=startlong, start_latitude=startlat,
                                                     end_longitude=endlong, end_latitude=endlat,
                                                     data_time=date, precision=precision, num_long=longnum,
                                                     num_lat=latnum, json_wind_component=json_all_datas);
            temp.save()
        else:
            return 0;
            #WindComponentAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
            #                                  end_longitude=endlong, end_latitude=endlat,
            #                                  data_time=date, precision=precision, num_long=longnum,
            #                                  num_lat=latnum).update(json_wind_component=json_all_datas);

    elif attr == "Visibilitysurface":
        if len(VisibilityAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
                                                 end_longitude=endlong, end_latitude=endlat,
                                                 data_time=date, precision=precision, num_long=longnum,
                                                 num_lat=latnum)) == 0:
            temp = VisibilityAttrs.objects.create(start_longitude=startlong, start_latitude=startlat,
                                                     end_longitude=endlong, end_latitude=endlat,
                                                     data_time=date, precision=precision, num_long=longnum,
                                                     num_lat=latnum, json_visibility=json_all_datas);
            temp.save()
        else:
            return 0;
            #VisibilityAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
            #                                  end_longitude=endlong, end_latitude=endlat,
            #                                  data_time=date, precision=precision, num_long=longnum,
            #                                  num_lat=latnum).update(json_visibility=json_all_datas);

    elif attr == "Totalprecipitationsurface1HourAccumulation":
        if len(PrecipitationAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
                                                 end_longitude=endlong, end_latitude=endlat,
                                                 data_time=date, precision=precision, num_long=longnum,
                                                 num_lat=latnum)) == 0:
            temp = PrecipitationAttrs.objects.create(start_longitude=startlong, start_latitude=startlat,
                                                     end_longitude=endlong, end_latitude=endlat,
                                                     data_time=date, precision=precision, num_long=longnum,
                                                     num_lat=latnum, json_precipitation=json_all_datas);
            temp.save()
        else:
            return 0;
            #PrecipitationAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
            #                                  end_longitude=endlong, end_latitude=endlat,
            #                                  data_time=date, precision=precision, num_long=longnum,
            #                                  num_lat=latnum).update(json_precipitation=json_all_datas);

    elif attr == "significantheightswell":
        if len(HeightSwellAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
                                                 end_longitude=endlong, end_latitude=endlat,
                                                 data_time=date, precision=precision, num_long=longnum,
                                                 num_lat=latnum)) == 0:
            temp = HeightSwellAttrs.objects.create(start_longitude=startlong, start_latitude=startlat,
                                                     end_longitude=endlong, end_latitude=endlat,
                                                     data_time=date, precision=precision, num_long=longnum,
                                                     num_lat=latnum, json_height_swell=json_all_datas);
            temp.save()
        else:
            return 0;
            #HeightSwellAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
            #                                  end_longitude=endlong, end_latitude=endlat,
            #                                  data_time=date, precision=precision, num_long=longnum,
            #                                  num_lat=latnum).update(json_height_swell=json_all_datas);
    elif attr == "Seawavehigh":
        if len(SeaWaveAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
                                                 end_longitude=endlong, end_latitude=endlat,
                                                 data_time=date, precision=precision, num_long=longnum,
                                                 num_lat=latnum)) == 0:
            temp = SeaWaveAttrs.objects.create(start_longitude=startlong, start_latitude=startlat,
                                                     end_longitude=endlong, end_latitude=endlat,
                                                     data_time=date, precision=precision, num_long=longnum,
                                                     num_lat=latnum, json_sea_wave=json_all_datas);
            temp.save()
        else:
            return 0;
            #SeaWaveAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
            #                                  end_longitude=endlong, end_latitude=endlat,
            #                                  data_time=date, precision=precision, num_long=longnum,
            #                                  num_lat=latnum).update(json_sea_wave=json_all_datas);

    elif attr == "Sealevelpressure":
        if len(PressureAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
                                                 end_longitude=endlong, end_latitude=endlat,
                                                 data_time=date, precision=precision, num_long=longnum,
                                                 num_lat=latnum)) == 0:
            temp = PressureAttrs.objects.create(start_longitude=startlong, start_latitude=startlat,
                                                     end_longitude=endlong, end_latitude=endlat,
                                                     data_time=date, precision=precision, num_long=longnum,
                                                     num_lat=latnum, json_pressure=json_all_datas);
            temp.save()
        else:
            return 0;
            #PressureAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
            #                                  end_longitude=endlong, end_latitude=endlat,
            #                                  data_time=date, precision=precision, num_long=longnum,
            #                                  num_lat=latnum).update(json_pressure=json_all_datas);

    elif attr == "Relativehumidityheightaboveground":
        if len(HumidityAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
                                                 end_longitude=endlong, end_latitude=endlat,
                                                 data_time=date, precision=precision, num_long=longnum,
                                                 num_lat=latnum)) == 0:
            temp = HumidityAttrs.objects.create(start_longitude=startlong, start_latitude=startlat,
                                                     end_longitude=endlong, end_latitude=endlat,
                                                     data_time=date, precision=precision, num_long=longnum,
                                                     num_lat=latnum, json_humidity=json_all_datas);
            temp.save()
        else:
            return 0;
            #HumidityAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
            #                                  end_longitude=endlong, end_latitude=endlat,
            #                                  data_time=date, precision=precision, num_long=longnum,
            #                                  num_lat=latnum).update(json_humidity=json_all_datas);
    elif attr == "meanperiodswell":
        if len(PeriodSwellAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
                                                 end_longitude=endlong, end_latitude=endlat,
                                                 data_time=date, precision=precision, num_long=longnum,
                                                 num_lat=latnum)) == 0:
            temp = PeriodSwellAttrs.objects.create(start_longitude=startlong, start_latitude=startlat,
                                                     end_longitude=endlong, end_latitude=endlat,
                                                     data_time=date, precision=precision, num_long=longnum,
                                                     num_lat=latnum, json_period_swell=json_all_datas);
            temp.save()
        else:
            return 0;
            #PeriodSwellAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
            #                                  end_longitude=endlong, end_latitude=endlat,
            #                                  data_time=date, precision=precision, num_long=longnum,
            #                                  num_lat=latnum).update(json_period_swell=json_all_datas);
    return 0;

def parseFilePattern3(file_dir, filename):
    file = open(file_dir+ "/" + filename, 'r')
    header = file.readline();
    timeinfo = file.readline();
    if timeinfo[0]=='1':
        dateinfo = "20" + timeinfo.strip().replace(' ','')[0:-2];
    else:
        dateinfo = timeinfo.strip().replace(' ', '')[0:-2];
    print(filename);
    date = getFullTimeHour(dateinfo);
    slices = filename.split('_');
    attr = ""
    for i in range(len(slices)-2):
        attr += slices[i]
    #if date.strftime('%Y-%m-%d %H:%M:%S') != "2017-01-01 04:00:00":
    #   return 0

    #WeatherAttrs.objects.all().delete();
    type = slices[-2]

    posinfo = file.readline().split(' ');
    precision = float(posinfo[0])
    startlat = float(posinfo[4])
    endlat = float(posinfo[5])
    startlong = float(posinfo[2])
    endlong = float(posinfo[3])

    otherinfo = file.readline().split(' ');
    longnum = int(otherinfo[0])
    latnum = int(otherinfo[1])

    line_info = file.readline().strip('\n');
    count = 0;
    all_datas = []

    while line_info:
        datainfo = line_info.split(' ');
        all_datas += datainfo;
        line_info = file.readline().strip('\n');
    entry_long_precision = 0.3;
    longEntryNum = math.ceil(entry_long_precision / precision);
    dataEntryNum = (int)(longnum/longEntryNum);
    for i in range(0, dataEntryNum):
        entry_startlong = startlong + i*entry_long_precision;
        entry_endlong = entry_startlong + entry_long_precision - precision;
        #print("start：" + str(i * latnum * longEntryNum)  + " end: "  + str((i + 1) * latnum * longEntryNum));
        json_all_datas = json.dumps(all_datas[i * latnum * longEntryNum : (i + 1) * latnum * longEntryNum]);
        insertData(attr, entry_startlong, startlat, entry_endlong, endlat, date, precision, longEntryNum, latnum, json_all_datas);

    insertData(attr, startlong + dataEntryNum *entry_long_precision, startlat, endlong,  endlat, date, precision, 1, latnum,
               json.dumps(all_datas[dataEntryNum * latnum * longEntryNum:]));

    return 0;

def insertData(attr, startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data):
    if attr == "Temperatureheightaboveground":
        insertOne2TemperatureAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data);
    elif (attr == "directionswell"):
        insertOne2DirectionSwellAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data);
    elif attr == "oceancurrenth":
        insertOne2OceanCurrentHAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data);
    elif attr == "oceancurrentt":
        insertOne2OceanCurrentTAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data);
    elif attr == "oceancurrentu":
        insertOne2OceanCurrentUAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data);
    elif attr == "oceancurrentv":
        insertOne2OceanCurrentVAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data);
    elif attr == "oceancurrentw":
        insertOne2OceanCurrentWAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data);
    elif attr == "Windspeedheightaboveground":
        insertOne2WindSpeedAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data);
    elif attr == "Windcomponentheightaboveground":
        insertOne2WindComponentAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data);
    elif attr == "Visibilitysurface":
        insertOne2VisibilityAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data);
    elif attr == "Totalprecipitationsurface1HourAccumulation":
        insertOne2PrecipitationAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data);
    elif attr == "significantheightswell":
        insertOne2HeightSwellAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data);
    elif attr == "Seawavehigh":
        insertOne2SeaWaveAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data);
    elif attr == "Sealevelpressure":
        insertOne2PressureAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data);
    elif attr == "Relativehumidityheightaboveground":
        insertOne2HumidityAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data);
    elif attr == "meanperiodswell":
        insertOne2PeriodSwellAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data);

'''

'''
def insertOne2TemperatureAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data):
    print("startlong:" + str(startlong));
    print("endlong:" + str(endlong));
    print("startlat:" + str(startlat));
    print("endlat:" + str(endlat));
    print("longnum:" + str(longnum));
    print("latnum" + str(latnum));
    print("**************************************");

    if len(TemperatureAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat, end_longitude=endlong,
                                           end_latitude=endlat,data_time=date, precision=precision, num_long=longnum, num_lat=latnum)) == 0:
        temp = TemperatureAttrs.objects.create(start_longitude=startlong, start_latitude=startlat,
                                               end_longitude=endlong, end_latitude=endlat,
                                               data_time=date, precision=precision, num_long=longnum, num_lat=latnum,
                                               json_temperature=data);
        temp.save()
    else:
        return 0;
    return 1;

def insertOne2DirectionSwellAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data):
    if len(DirectionSwellAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
                                               end_longitude=endlong, end_latitude=endlat,
                                               data_time=date, precision=precision, num_long=longnum,
                                               num_lat=latnum)) == 0:
        temp = DirectionSwellAttrs.objects.create(start_longitude=startlong, start_latitude=startlat,
                                                   end_longitude=endlong, end_latitude=endlat,
                                                   data_time=date, precision=precision, num_long=longnum,
                                                   num_lat=latnum, json_direction_swell=data);
        temp.save()
    else:
        return 0;
    return 1;

def insertOne2OceanCurrentHAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data):
    if len(OceanCurrentHAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
                                                  end_longitude=endlong, end_latitude=endlat,
                                                  data_time=date, precision=precision, num_long=longnum,
                                                  num_lat=latnum)) == 0:
        temp = OceanCurrentHAttrs.objects.create(start_longitude=startlong, start_latitude=startlat,
                                                      end_longitude=endlong, end_latitude=endlat,
                                                      data_time=date, precision=precision, num_long=longnum,
                                                      num_lat=latnum, json_ocean_current_h=data);
        temp.save()
    else:
        return 0;
    return 1;

def insertOne2OceanCurrentTAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data):
    if len(OceanCurrentTAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
                                                 end_longitude=endlong, end_latitude=endlat,
                                                 data_time=date, precision=precision, num_long=longnum,
                                                 num_lat=latnum)) == 0:
        temp = OceanCurrentTAttrs.objects.create(start_longitude=startlong, start_latitude=startlat,
                                                     end_longitude=endlong, end_latitude=endlat,
                                                     data_time=date, precision=precision, num_long=longnum,
                                                     num_lat=latnum, json_ocean_current_t=data);
        temp.save()
    else:
        return 0;
    return 1;

def insertOne2OceanCurrentUAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data):

    if len(OceanCurrentUAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
                                                 end_longitude=endlong, end_latitude=endlat,
                                                 data_time=date, precision=precision, num_long=longnum,
                                                 num_lat=latnum)) == 0:
        temp = OceanCurrentUAttrs.objects.create(start_longitude=startlong, start_latitude=startlat,
                                                     end_longitude=endlong, end_latitude=endlat,
                                                     data_time=date, precision=precision, num_long=longnum,
                                                     num_lat=latnum, json_ocean_current_u=data);
        temp.save()
    else:
        return 0;
    return 1;

def insertOne2OceanCurrentVAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data):
    if len(OceanCurrentVAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
                                                 end_longitude=endlong, end_latitude=endlat,
                                                 data_time=date, precision=precision, num_long=longnum,
                                                 num_lat=latnum)) == 0:
        temp = OceanCurrentVAttrs.objects.create(start_longitude=startlong, start_latitude=startlat,
                                                     end_longitude=endlong, end_latitude=endlat,
                                                     data_time=date, precision=precision, num_long=longnum,
                                                     num_lat=latnum, json_ocean_current_v=data);
        temp.save()
    else:
        return 0;
    return 1;

def insertOne2OceanCurrentWAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data):
    if len(OceanCurrentWAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
                                                 end_longitude=endlong, end_latitude=endlat,
                                                 data_time=date, precision=precision, num_long=longnum,
                                                 num_lat=latnum)) == 0:
        temp = OceanCurrentWAttrs.objects.create(start_longitude=startlong, start_latitude=startlat,
                                                     end_longitude=endlong, end_latitude=endlat,
                                                     data_time=date, precision=precision, num_long=longnum,
                                                     num_lat=latnum, json_ocean_current_w=data);
        temp.save()
    else:
        return 0;
    return 1;

def insertOne2WindSpeedAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data):
    if len(WindSpeedAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
                                                 end_longitude=endlong, end_latitude=endlat,
                                                 data_time=date, precision=precision, num_long=longnum,
                                                 num_lat=latnum)) == 0:
        temp = WindSpeedAttrs.objects.create(start_longitude=startlong, start_latitude=startlat,
                                                     end_longitude=endlong, end_latitude=endlat,
                                                     data_time=date, precision=precision, num_long=longnum,
                                                     num_lat=latnum, json_wind_speed=data);
        temp.save()
    else:
        return 0;
    return 1;

def insertOne2WindComponentAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data):
    if len(WindComponentAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
                                                 end_longitude=endlong, end_latitude=endlat,
                                                 data_time=date, precision=precision, num_long=longnum,
                                                 num_lat=latnum)) == 0:
        temp = WindComponentAttrs.objects.create(start_longitude=startlong, start_latitude=startlat,
                                                     end_longitude=endlong, end_latitude=endlat,
                                                     data_time=date, precision=precision, num_long=longnum,
                                                     num_lat=latnum, json_wind_component=data);
        temp.save()
    else:
        return 0;
    return 1;

def insertOne2VisibilityAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data):

    if len(VisibilityAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
                                                 end_longitude=endlong, end_latitude=endlat,
                                                 data_time=date, precision=precision, num_long=longnum,
                                                 num_lat=latnum)) == 0:
        temp = VisibilityAttrs.objects.create(start_longitude=startlong, start_latitude=startlat,
                                                     end_longitude=endlong, end_latitude=endlat,
                                                     data_time=date, precision=precision, num_long=longnum,
                                                     num_lat=latnum, json_visibility=data);
        temp.save()
    else:
        return 0;
    return 1;

def insertOne2PrecipitationAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data):
    if len(PrecipitationAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
                                                 end_longitude=endlong, end_latitude=endlat,
                                                 data_time=date, precision=precision, num_long=longnum,
                                                 num_lat=latnum)) == 0:
        temp = PrecipitationAttrs.objects.create(start_longitude=startlong, start_latitude=startlat,
                                                     end_longitude=endlong, end_latitude=endlat,
                                                     data_time=date, precision=precision, num_long=longnum,
                                                     num_lat=latnum, json_precipitation=data);
        temp.save()
    else:
        return 0;
    return 1;

def insertOne2HeightSwellAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data):

    if len(HeightSwellAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
                                                 end_longitude=endlong, end_latitude=endlat,
                                                 data_time=date, precision=precision, num_long=longnum,
                                                 num_lat=latnum)) == 0:
        temp = HeightSwellAttrs.objects.create(start_longitude=startlong, start_latitude=startlat,
                                                     end_longitude=endlong, end_latitude=endlat,
                                                     data_time=date, precision=precision, num_long=longnum,
                                                     num_lat=latnum, json_height_swell=data);
        temp.save()
    else:
        return 0;
    return 1;

def insertOne2SeaWaveAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data):
    if len(SeaWaveAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
                                                 end_longitude=endlong, end_latitude=endlat,
                                                 data_time=date, precision=precision, num_long=longnum,
                                                 num_lat=latnum)) == 0:
        temp = SeaWaveAttrs.objects.create(start_longitude=startlong, start_latitude=startlat,
                                                     end_longitude=endlong, end_latitude=endlat,
                                                     data_time=date, precision=precision, num_long=longnum,
                                                     num_lat=latnum, json_sea_wave=data);
        temp.save()
    else:
        return 0;
    return 1;

def insertOne2PressureAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data):
    if len(PressureAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
                                                 end_longitude=endlong, end_latitude=endlat,
                                                 data_time=date, precision=precision, num_long=longnum,
                                                 num_lat=latnum)) == 0:
        temp = PressureAttrs.objects.create(start_longitude=startlong, start_latitude=startlat,
                                                     end_longitude=endlong, end_latitude=endlat,
                                                     data_time=date, precision=precision, num_long=longnum,
                                                     num_lat=latnum, json_pressure=data);
        temp.save()
    else:
        return 0;
    return 1;

def insertOne2HumidityAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data):
    if len(HumidityAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
                                                 end_longitude=endlong, end_latitude=endlat,
                                                 data_time=date, precision=precision, num_long=longnum,
                                                 num_lat=latnum)) == 0:
        temp = HumidityAttrs.objects.create(start_longitude=startlong, start_latitude=startlat,
                                                     end_longitude=endlong, end_latitude=endlat,
                                                     data_time=date, precision=precision, num_long=longnum,
                                                     num_lat=latnum, json_humidity=data);
        temp.save()
    else:
        return 0;
    return 1;

def insertOne2PeriodSwellAttrs(startlong, startlat, endlong, endlat, date, precision, longnum, latnum, data):
    if len(PeriodSwellAttrs.objects.filter(start_longitude=startlong, start_latitude=startlat,
                                                 end_longitude=endlong, end_latitude=endlat,
                                                 data_time=date, precision=precision, num_long=longnum,
                                                 num_lat=latnum)) == 0:
        temp = PeriodSwellAttrs.objects.create(start_longitude=startlong, start_latitude=startlat,
                                                     end_longitude=endlong, end_latitude=endlat,
                                                     data_time=date, precision=precision, num_long=longnum,
                                                     num_lat=latnum, json_period_swell=data);
        temp.save()
    else:
        return 0;
    return 1;




def parseFile(file_dir, filename):
    file = open(file_dir+ "/" + filename, 'r')
    header = file.readline();
    timeinfo = file.readline();
    if timeinfo[0]=='1':
        dateinfo = "20" + timeinfo.strip().replace(' ','')[0:-2];
    else:
        dateinfo = timeinfo.strip().replace(' ', '')[0:-2];
    #print(filename);
    date = getFullTimeHour(dateinfo);
    slices = filename.split('_');
    attr = ""
    for i in range(len(slices)-2):
        attr += slices[i]
    #if date.strftime('%Y-%m-%d %H:%M:%S') != "2017-01-01 04:00:00":
    #   return 0

    #WeatherAttrs.objects.all().delete();
    type = slices[-2]

    posinfo = file.readline().split(' ');
    precision = float(posinfo[0])
    startlat = float(posinfo[4])
    endlat = float(posinfo[5])
    startlong = float(posinfo[2])
    endlong = float(posinfo[3])

    otherinfo = file.readline().split(' ');
    longnum = int(otherinfo[0])
    latnum = int(otherinfo[1])

    line_info = file.readline();
    count = 0;
    print(filename)
    num = 100
    if attr == "Temperatureheightaboveground":
        while line_info:
            datainfo = line_info.split(' ');
            for i in range(len(datainfo)):
                lat = startlat + round(precision * (count % latnum), 2);
                long = startlong + round(precision * (math.floor(count / latnum)), 2);
                count += 1;
                if len(WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                   precision=precision)) == 0:
                    WeatherAttrs.objects.create(longitude=long, latitude=lat, data_time=date,
                                                precision=precision,
                                                temperature=round(float(datainfo[i]), 2));
                else:
                    WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                precision=precision).update(temperature=round(float(datainfo[i]), 2));
                if count == num:
                    return 1;
            line_info = file.readline();
        WeatherAttrs.save()
    if attr == "directionswell":
        while line_info:
            datainfo = line_info.split(' ');
            for i in range(len(datainfo)):
                lat = startlat + round(precision * (count % latnum), 2);
                long = startlong + round(precision * (math.floor(count / latnum)), 2);
                count += 1;
                if len(WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                   precision=precision)) == 0:
                    WeatherAttrs.objects.create(longitude=long, latitude=lat, data_time=date,
                                                precision=precision,
                                                direction_swell=round(float(datainfo[i]), 2));
                else:
                    WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                precision=precision).update(direction_swell=round(float(datainfo[i]), 2));
                if count == num:
                    return 1;
            line_info = file.readline();
        WeatherAttrs.save()
    if attr == "oceancurrenth":
        while line_info:
            datainfo = line_info.split(' ');
            for i in range(len(datainfo)):
                lat = startlat + round(precision * (count % latnum), 2);
                long = startlong + round(precision * (math.floor(count / latnum)), 2);
                count += 1;
                if len(WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                   precision=precision)) == 0:
                    WeatherAttrs.objects.create(longitude=long, latitude=lat, data_time=date,
                                                precision=precision,
                                                ocean_current_h=round(float(datainfo[i]), 2));
                else:
                    WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                precision=precision).update(ocean_current_h=round(float(datainfo[i]), 2));
                if count == num:
                    return 1;
            line_info = file.readline();
        WeatherAttrs.save()
    if attr == "oceancurrentt":
        while line_info:
            datainfo = line_info.split(' ');
            for i in range(len(datainfo)):
                lat = startlat + round(precision * (count % latnum), 2);
                long = startlong + round(precision * (math.floor(count / latnum)), 2);
                count += 1;
                if len(WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                   precision=precision)) == 0:
                    WeatherAttrs.objects.create(longitude=long, latitude=lat, data_time=date,
                                                precision=precision,
                                                ocean_current_t=round(float(datainfo[i]), 2));
                else:
                    WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                precision=precision).update(ocean_current_t=round(float(datainfo[i]), 2));
                if count == num:
                    return 1;
            line_info = file.readline();
        WeatherAttrs.save()
    if attr == "oceancurrentu":
        while line_info:
            datainfo = line_info.split(' ');
            for i in range(len(datainfo)):
                lat = startlat + round(precision * (count % latnum), 2);
                long = startlong + round(precision * (math.floor(count / latnum)), 2);
                count += 1;
                if len(WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                   precision=precision)) == 0:
                    WeatherAttrs.objects.create(longitude=long, latitude=lat, data_time=date,
                                                precision=precision,
                                                ocean_current_u=round(float(datainfo[i]), 2));
                else:
                    WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                precision=precision).update(ocean_current_u=round(float(datainfo[i]), 2));
                if count == num:
                    return 1;
            line_info = file.readline();
        WeatherAttrs.save()
    if attr == "oceancurrentv":
        while line_info:
            datainfo = line_info.split(' ');
            for i in range(len(datainfo)):
                lat = startlat + round(precision * (count % latnum), 2);
                long = startlong + round(precision * (math.floor(count / latnum)), 2);
                count += 1;
                if len(WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                   precision=precision)) == 0:
                    WeatherAttrs.objects.create(longitude=long, latitude=lat, data_time=date,
                                                precision=precision,
                                                ocean_current_v=round(float(datainfo[i]), 2));
                else:
                    WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                precision=precision).update(ocean_current_v=round(float(datainfo[i]), 2));
                if count == num:
                    return 1;
            line_info = file.readline();
        WeatherAttrs.save()
    if attr == "oceancurrentw":
        while line_info:
            datainfo = line_info.split(' ');
            for i in range(len(datainfo)):
                lat = startlat + round(precision * (count % latnum), 2);
                long = startlong + round(precision * (math.floor(count / latnum)), 2);
                count += 1;
                if len(WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                   precision=precision)) == 0:
                    WeatherAttrs.objects.create(longitude=long, latitude=lat, data_time=date,
                                                precision=precision,
                                                ocean_current_w=round(float(datainfo[i]), 4));
                else:
                    WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                precision=precision).update(ocean_current_w=round(float(datainfo[i]), 4));
                if count == num:
                    return 1;
            line_info = file.readline();
        WeatherAttrs.save()
    if attr == "Windspeedheightaboveground":
        while line_info:
            datainfo = line_info.split(' ');
            for i in range(len(datainfo)):
                lat = startlat + round(precision * (count % latnum), 2);
                long = startlong + round(precision * (math.floor(count / latnum)), 2);
                count += 1;
                if len(WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                   precision=precision)) == 0:
                    WeatherAttrs.objects.create(longitude=long, latitude=lat, data_time=date,
                                                precision=precision,
                                                wind_speed=round(float(datainfo[i]), 2));
                else:
                    WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                precision=precision).update(wind_speed=round(float(datainfo[i]), 2));
                if count == num:
                    return 1;
            line_info = file.readline();
        WeatherAttrs.save()
    if attr == "Windcomponentheightaboveground":
        while line_info:
            datainfo = line_info.split(' ');
            for i in range(len(datainfo)):
                lat = startlat + round(precision * (count % latnum), 2);
                long = startlong + round(precision * (math.floor(count / latnum)), 2);
                count += 1;
                if len(WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                   precision=precision)) == 0:
                    WeatherAttrs.objects.create(longitude=long, latitude=lat, data_time=date,
                                                precision=precision,
                                                wind_component=round(float(datainfo[i]), 2));
                else:
                    WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                precision=precision).update(wind_component=round(float(datainfo[i]), 2));
                if count == num:
                    return 1;
            line_info = file.readline();
        WeatherAttrs.save()
    if attr == "Visibilitysurface":
        while line_info:
            datainfo = line_info.split(' ');
            for i in range(len(datainfo)):
                lat = startlat + round(precision * (count % latnum), 2);
                long = startlong + round(precision * (math.floor(count / latnum)), 2);
                count += 1;
                if len(WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                   precision=precision)) == 0:
                    WeatherAttrs.objects.create(longitude=long, latitude=lat, data_time=date,
                                                precision=precision,
                                                visibility=int(datainfo[i]));
                else:
                    WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                precision=precision).update(visibility=int(datainfo[i]));
                if count == num:
                    return 1;
            line_info = file.readline();
        WeatherAttrs.save()
    if attr == "Totalprecipitationsurface1HourAccumulation":
        while line_info:
            datainfo = line_info.split(' ');
            for i in range(len(datainfo)):
                lat = startlat + round(precision * (count % latnum), 2);
                long = startlong + round(precision * (math.floor(count / latnum)), 2);
                count += 1;
                if len(WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                   precision=precision)) == 0:
                    WeatherAttrs.objects.create(longitude=long, latitude=lat, data_time=date,
                                                precision=precision,
                                                precipitation=round(float(datainfo[i]), 2));
                else:
                    WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                precision=precision).update(precipitation=round(float(datainfo[i]), 2));
                if count == num:
                    return 1;
            line_info = file.readline();
        WeatherAttrs.save()
    if attr == "significantheightswell":
        while line_info:
            datainfo = line_info.split(' ');
            for i in range(len(datainfo)):
                lat = startlat + round(precision * (count % latnum), 2);
                long = startlong + round(precision * (math.floor(count / latnum)), 2);
                count += 1;
                if len(WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                   precision=precision)) == 0:
                    WeatherAttrs.objects.create(longitude=long, latitude=lat, data_time=date,
                                                precision=precision,
                                                height_swell=round(float(datainfo[i]), 2));
                else:
                    WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                precision=precision).update(height_swell=round(float(datainfo[i]), 2));
                if count == num:
                    return 1;
            line_info = file.readline();
        WeatherAttrs.save()
    if attr == "Seawavehigh":
        while line_info:
            datainfo = line_info.split(' ');
            for i in range(len(datainfo)):
                lat = startlat + round(precision * (count % latnum), 2);
                long = startlong + round(precision * (math.floor(count / latnum)), 2);
                count += 1;
                if len(WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                   precision=precision)) == 0:
                    WeatherAttrs.objects.create(longitude=long, latitude=lat, data_time=date,
                                                precision=precision,
                                                sea_wave=round(float(datainfo[i]), 2));
                else:
                    WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                precision=precision).update(sea_wave=round(float(datainfo[i]), 2));
                if count == num:
                    return 1;
            line_info = file.readline();
        WeatherAttrs.save()
    if attr == "Sealevelpressure":
        while line_info:
            datainfo = line_info.split(' ');
            for i in range(len(datainfo)):
                lat = startlat + round(precision * (count % latnum), 2);
                long = startlong + round(precision * (math.floor(count / latnum)), 2);
                count += 1;
                if len(WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                   precision=precision)) == 0:
                    WeatherAttrs.objects.create(longitude=long, latitude=lat, data_time=date,
                                                precision=precision,
                                                pressure=round(float(datainfo[i]), 2));
                else:
                    WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                precision=precision).update(pressure=round(float(datainfo[i]), 2));
                if count == num:
                    return 1;
            line_info = file.readline();
        WeatherAttrs.save()
    if attr == "Relativehumidityheightaboveground":
        while line_info:
            datainfo = line_info.split(' ');
            for i in range(len(datainfo)):
                lat = startlat + round(precision * (count % latnum), 2);
                long = startlong + round(precision * (math.floor(count / latnum)), 2);
                count += 1;
                if len(WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                   precision=precision)) == 0:
                    WeatherAttrs.objects.create(longitude=long, latitude=lat, data_time=date,
                                                precision=precision,
                                                humidity=round(float(datainfo[i]), 2));
                else:
                    WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                precision=precision).update(humidity=round(float(datainfo[i]), 2));
                if count == num:
                    return 1;
            line_info = file.readline();
        WeatherAttrs.save()
    if attr == "meanperiodswell":
        while line_info:
            datainfo = line_info.split(' ');
            for i in range(len(datainfo)):
                lat = startlat + round(precision * (count % latnum), 2);
                long = startlong + round(precision * (math.floor(count / latnum)), 2);
                count += 1;
                if len(WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                   precision=precision)) == 0:
                    WeatherAttrs.objects.create(longitude=long, latitude=lat, data_time=date,
                                                precision=precision,
                                                period_swell=round(float(datainfo[i]), 2));
                else:
                    WeatherAttrs.objects.filter(longitude=long, latitude=lat, data_time=date,
                                                precision=precision).update(period_swell=round(float(datainfo[i]), 2));
                if count == num:
                    return 1;
            line_info = file.readline();
        WeatherAttrs.save()
    return 1
'''
#获取目录下的文件
def file_name(file_dir):
    filesname = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            filesname.append(file)
    return filesname

#解析天气要素的文件
def getOneFileData(filename):
    file = open(filename)
    header = file.readline();
    timeinfo = file.readline();
    if timeinfo[0] == '1':
        dateinfo = "20" + timeinfo.strip().replace(' ', '')[0:-2];
    else:
        dateinfo = timeinfo.strip().replace(' ', '')[0:-2];
    print(filename);
    date = getFullTimeHour(dateinfo);
    slices = filename.split('_');
    attr = ""
    for i in range(len(slices) - 2):
        attr += slices[i]
    # if date.strftime('%Y-%m-%d %H:%M:%S') != "2017-01-01 04:00:00":
    #   return 0

    # WeatherAttrs.objects.all().delete();
    type = slices[-2]

    posinfo = file.readline().split(' ');
    precision = float(posinfo[0])
    startlat = float(posinfo[4])
    endlat = float(posinfo[5])
    startlong = float(posinfo[2])
    endlong = float(posinfo[3])

    otherinfo = file.readline().split(' ');
    longnum = int(otherinfo[0])
    latnum = int(otherinfo[1])

    line_info = file.readline().strip('\n');
    count = 0;
    all_datas = []

    while line_info:
        datainfo = line_info.split(' ');
        all_datas += datainfo;
        line_info = file.readline().strip('\n');
    return all_datas;

    '''lat=30;
    long=104;
    getIndex(lat, long, 0, 105, 0.1, 401);
    part_datas = []
    print(len(all_datas))
    for i in range(len(all_datas)):
        if (i%100!=0):
            continue;
        part_datas.append(all_datas[i]);

    print(len(part_datas));

    json_all_datas = json.dumps(all_datas);'''

# 获取距离目标点最近的feature
def getMinDistId(lon, lat, features_info):
    minDist = 0;
    minId = -1;
    for feature_info in features_info:
        dist = getDistance(lat, lon, feature_info[1][1], feature_info[1][0]);
        dist = abs(dist)
        if (dist < minDist):
            minDist = dist;
            minId = feature_info[0]
    return minId


# 获取首页每个区域的当天的天气属性情况
def getFeatureColor():
    return getFeatureColorWithDelay(0);

# 获取首页每个区域的今天或者明天的天气属性情况
def getFeatureColorWithDelay(delay):
    json_filepath = "/home/code/climateServices/climateServices/static/geojson/all.json"
    with open(json_filepath, 'r') as load_f:
        load_dict = json.load(load_f)
    features = load_dict["features"]
    feature_info = {}
    for feature in features:
        lon= (feature["properties"]["cp"][0] + 360) % 360;
        lat = (feature["properties"]["cp"][1] + 360) % 360;
        lon = int(lon/0.1)*0.1;
        lat = int(lat/0.1)*0.1;
        if lon > 135:
            lon = 135
        if lon < 105:
            lon = 105;
        if lat > 40:
            lat = 40;
        #debugOutputFile("start find one feature")


        #data_hz = getHashValue(lon, lat, 10, 20)
        #results = WeatherAttrs20170101.objects.filter(idx_b_hyqx_20170101_uk=data_hz);

        results = getWeatherAttrsWithDelay(lat, lon, 0.1, delay);
        #debugOutputFile(results["temperature"])
        feature_info[feature["properties"]["id"]] = {"wnd": results["temperature"],
                                                     "qy": results["pressure"],
                                                     "jyl": getPrecipitation(lat, lon, 0.3, delay),
                                                     "xdsd": results["humidity"],
                                                     "njd": results["visibility"]
                                                     }
        #debugOutputFile(str(lon) + " " + str(lat) + " " + " !!!!!  " + results["precipitation"])
        #debugOutputFile("end find one feature")

        '''for result in results:
            feature_info[feature["properties"]["id"]] = {"wnd":str(result.f_dl_wnd),
                                                     "qy":str(result.f_dl_qy),
                                                     "jyl":str(result.f_dl_jyl),
                                                     "xdsd":str(result.f_dl_xdsd),
                                                     "njd": str(result.f_it_njd)
                                                     }'''
    #debugOutputFile(load_dict)
    #debugOutputFile(feature_info)
    #debugOutputFile("end"):q

    return feature_info;

def getPrecipitation(lat, lon, precision, delay):
    #debugOutputFile("deal precipitation is zero %%%%%%%%%%%%%%%%%%%%")
    lats = [lat-3*precision, lat-precision, lat, lat+precision, lat+3*precision];
    lons = [lon-3*precision, lon-precision, lon, lon+precision,  lon+3*precision];
    precipitationSum = 0;
    count = 0;
    for onelat in lats:
        for onelon in lons:
            #debugOutputFile(str(onelon)+ " lon, " + str(onelat) + " lat %%%%%%%%%%%%%%%%%%%%");
            if onelon >= 105 and onelon <= 135 and onelat >= 0 and onelat <= 40:
                onePre = float(getWeatherAttrsWithDelay(onelat, onelon, precision, delay)["precipitation"])
                if onePre != 0.0:
                    count+=1;
                precipitationSum += onePre;
                #debugOutputFile("&&&&&&&&&&&&&&" + str(precipitationSum));
    if count == 0:
        return "0.0";
    else:
        return str(round(precipitationSum/count,2));



#获得风向
def getWindDirections():
    lons = np.linspace(105, 135, 16);
    lats = np.linspace(0, 40, 21);
    infos=[]

    for i in range(len(lons)):
        for j in range(len(lats)):
            data_hz = getHashValue(lons[i], lats[j], 10, 20)
            results = WeatherAttrs20170101.objects.filter(idx_b_hyqx_20170101_uk=data_hz);
            for result in results:
                infos.append([lons[i], lats[j], str(result.f_dl_fx)])

    return infos;

