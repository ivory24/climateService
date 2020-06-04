from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from climateApp.controllers.weather_attr.manage import *
from climateApp.controllers.typhoon.manage import *
from climateApp.controllers.ship.manage import *
from climateApp.controllers.seaway.manage import *
from climateApp.controllers.weather_attr.get_attr import *
from django.http import HttpResponse
import json
import datetime
from django.http import *
import decimal
from django.core.handlers.wsgi import WSGIRequest
# Create your views here.
from  decimal import Decimal
import numpy as np
import copy
import random

import base64



'''
def temperature_data():
    title = {
        'text': '出发地到目的地的气象要素-温度变化',
        'style': {
            "fontSize": "15px"
        }
    };

    subtitle = {
        'text': '温度'
    };
    xAxis = {
        'categories': ['出发地', '', '', '', '', '',
                       '', '', '', '', '', '目的地']
    };
    yAxis = {
        'tickInterval': 5,
        'title': ''
    };
    tooltip = {
        'valueSuffix': '\xB0C'
    }

    legend = {
        'layout': 'horizontal',
        'align': 'center',
        'verticalAlign': 'top',
        'borderWidth': 0
    };
    series = [
        {
            'name': 'T1',
            'data': [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2,
                     26.5, 23.3, 18.3, 13.9, 9.6],
            'color': '#FF0000'
        },
        {
            'name': 'T2',
            'data': [0, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8,
                     24.1, 20.1, 14.1, 8.6, 2.5],
            'color': '#003366'
        },
        {
            'name': 'T3',
            'data': [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0,
                     16.6, 14.2, 10.3, 6.6, 4.8],
            'color': '#0099CC'
        },
        {
            'name': 'T4',
            'data': [8.0, 5.9, 8.5, 12.5, 19.2, 24.5, 26.2,
                     24.5, 28.3, 19.3, 16.9, 10.6],
            'color': '#FF9933'
        },
        {
            'name': 'T5',
            'data': [1, 4, 3.7, 10.3, 14.0, 22.0, 26.8,
                     25.1, 22.1, 16.1, 9.6, 4.5],
            'color': '#99FFCC'
        },
        {
            'name': 'T6',
            'data': [3.0, 5.2, 6.7, 7.5, 10.9, 17.2, 16.0,
                     15.6, 15.2, 13.3, 10.6, 6.8],
            'color': '#00CC33'
        },
        {
            'name': 'T7',
            'data': [3.5, 5.2, 6.7, 3.5, 10.9, 12.2, 11.0,
                     15.6, 13.2, 11.3, 9.6, 8.8],
            'color': '#CC9900'
        }
    ];
    data = [{'title': title, 'xAxis': xAxis, 'yAxis': yAxis, 'tooltip': tooltip, 'legend': legend, 'series': series}]
    return data


def humidity_data():
    title = {
        'text': '出发地到目的地的气象要素-湿度变化',
        'style': {
            "fontSize": "15px"
        }
    };

    subtitle = {
        'text': '温度'
    };
    xAxis = {
        'categories': ['出发地', '', '', '', '', '',
                       '', '', '', '', '', '目的地']
    };
    yAxis = {
        'tickInterval': 5,
        'title': ''
    };
    tooltip = {
        'valueSuffix': '\xB0C'
    }

    legend = {
        'layout': 'horizontal',
        'align': 'center',
        'verticalAlign': 'top',
        'borderWidth': 0
    };
    series = [
        {
            'name': 'T1',
            'data': [90.00, 89.05, 92.01, 85.02, 82.20, 79.86, 78.00,
                     76.08, 71.84, 67.71, 65.44, 65.33],
            'color': '#FF0000'
        },
        {
            'name': 'T2',
            'data': [65.21, 63.52, 61.84, 60.94, 60.81, 60.68, 60.52,
                     60.35, 60.33, 60.59, 60.32, 62.04],
            'color': '#003366'
        },
        {
            'name': 'T3',
            'data': [90.10, 89.05, 88.01, 85.02, 82.20, 79.86, 78.00,
                     76.08, 71.84, 67.71, 65.44, 69.33],
            'color': '#0099CC'
        },
        {
            'name': 'T4',
            'data': [90.00, 89.05, 86.01, 85.02, 82.20, 79.86, 78.00,
                     76.08, 71.84, 67.71, 65.44, 75.33],
            'color': '#FF9933'
        },
        {
            'name': 'T5',
            'data': [90.00, 87.05, 88.01, 85.02, 82.20, 79.86, 78.00,
                     76.08, 71.84, 67.71, 65.44, 65.33],
            'color': '#99FFCC'
        },
        {
            'name': 'T6',
            'data': [70.00, 89.05, 88.01, 85.02, 82.20, 79.86, 75.00,
                     76.08, 71.84, 67.71, 65.44, 65.33],
            'color': '#00CC33'
        },
        {
            'name': 'T7',
            'data': [80.00, 89.05, 88.01, 86.02, 82.20, 79.86, 78.00,
                     76.08, 71.84, 67.71, 65.44, 65.33],
            'color': '#CC9900'
        }
    ];
    data = [{'title': title, 'xAxis': xAxis, 'yAxis': yAxis, 'tooltip': tooltip, 'legend': legend, 'series': series}]
    return data

def wind_speed_data(name):
    title = {
        'text': '出发地到目的地的气象要素-'+name + '变化',
        'style': {
            "fontSize": "15px"
        }
    };

    subtitle = {
        'text': '温度'
    };
    xAxis = {
        'categories': ['出发地', '', '', '', '', '',
                       '', '', '', '', '', '目的地']
    };
    yAxis = {
        'tickInterval': 5,
        'title': ''
    };
    tooltip = {
        'valueSuffix': '\xB0C'
    }

    legend = {
        'layout': 'horizontal',
        'align': 'center',
        'verticalAlign': 'top',
        'borderWidth': 0
    };
    series = [
        {
            'name': 'T1',
            'data': [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2,
                     26.5, 23.3, 18.3, 13.9, 9.6],
            'color': '#FF0000'
        },
        {
            'name': 'T2',
            'data': [0, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8,
                     24.1, 20.1, 14.1, 8.6, 2.5],
            'color': '#003366'
        },
        {
            'name': 'T3',
            'data': [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0,
                     16.6, 14.2, 10.3, 6.6, 4.8],
            'color': '#0099CC'
        },
        {
            'name': 'T4',
            'data': [8.0, 5.9, 8.5, 12.5, 19.2, 24.5, 26.2,
                     24.5, 28.3, 19.3, 16.9, 10.6],
            'color': '#FF9933'
        },
        {
            'name': 'T5',
            'data': [1, 4, 3.7, 10.3, 14.0, 22.0, 26.8,
                     25.1, 22.1, 16.1, 9.6, 4.5],
            'color': '#99FFCC'
        },
        {
            'name': 'T6',
            'data': [3.0, 5.2, 6.7, 7.5, 10.9, 17.2, 16.0,
                     15.6, 15.2, 13.3, 10.6, 6.8],
            'color': '#00CC33'
        },
        {
            'name': 'T7',
            'data': [3.5, 5.2, 6.7, 3.5, 10.9, 12.2, 11.0,
                     15.6, 13.2, 11.3, 9.6, 8.8],
            'color': '#CC9900'
        }
    ];
    data = [{'title': title, 'xAxis': xAxis, 'yAxis': yAxis, 'tooltip': tooltip, 'legend': legend, 'series': series}]
    return data;

'''
# 获取台风预警信息
def getTyphoon():
    #date_str = "20170720";
    now_time = datetime.datetime.now().strftime('%Y%m%d');
    now_time = now_time[:3] + '7' + now_time[4:];
    now_time = "20171220";

    data = search_data(now_time, 7);
    # 生成台风预警的具体文本信息
    warning = "中央气象台" + datetime.datetime.strftime(getFullTimeDate(now_time), '%Y年%m月%d日') + "发布未来7天的台风预警：<br>";
    strength = {0:"未达到热带低压", 1:"热带低压", 2:"热带风暴", 3:"强热带风暴", 4:"台风", 5:"强台风", 6:"超强台风", 9:"变性气旋"};
    for i in range(len(data["name"])):
        warning += "&nbsp&nbsp&nbsp&nbsp" + str(data["name"][i]) + "台风" + datetime.datetime.strftime(data["start_time"][i], '%Y年%m月%d日') + "开始，未来7天强度最大为";
        warning += str(strength[data["strength_grade_max"][i]]) + "强度，最低气压为" + str(data["pressure_min"][i]) + "hPa，最大风速为";
        warning += str(data["wind_speed_max"][i]) + "m/s。<br>";
    if len(data["name"]) == 0:
        warning = "&nbsp&nbsp&nbsp&nbsp未来7天无台风";
    data = [{'warning': warning}];
    return data;
# 获取一行台风预警信息
def getTyphoonOneLine():
    #date_str = "20170720";
    now_time = datetime.datetime.now().strftime('%Y%m%d');
    now_time = now_time[:3] + '7' + now_time[4:];
    now_time = "20171220";

    data = search_data(now_time, 7);
    # 生成台风预警的一行文本信息
    warning = "中央气象台" + datetime.datetime.strftime(getFullTimeDate(now_time), '%Y年%m月%d日') + "发布未来7天的台风预警：";
    strength = {0:"未达到热带低压", 1:"热带低压", 2:"热带风暴", 3:"强热带风暴", 4:"台风", 5:"强台风", 6:"超强台风", 9:"变性气旋"};
    for i in range(len(data["name"])):
        warning += "&nbsp&nbsp&nbsp&nbsp" + str(data["name"][i]) + "台风" + datetime.datetime.strftime(data["start_time"][i], '%Y年%m月%d日') + "开始，未来7天强度最大为";
        warning += str(strength[data["strength_grade_max"][i]]) + "强度，最低气压为" + str(data["pressure_min"][i]) + "hPa，最大风速为";
        warning += str(data["wind_speed_max"][i]) + "m/s。";
    if len(data["name"]) == 0:
        warning = "&nbsp&nbsp&nbsp&nbsp未来7天无台风";
    data = [{'warning': warning}];
    return data;
# 封装的一个函数，获取台风的所有信息
def init():
    #insertWeather_attr();
    #insertFileInfo();
    getTyphoon();
    #insertAttrFileData("/Users/qingwang/Desktop/code/2dData");
    #insertAttrFileData("/home/data/2dData_unrar");

    #lat, long, precision, date
    #getTemperature(0.05, 105.05, 0.05, "2017-01-02 00:00:00");

# rgb颜色对应的十六进制表示法
p_colors=['#500006', '#74000c', '#b80000', '#fb3800', '#ff6e00',
          '#ff9400', '#ffcb24', '#ffe664', '#faf296', '#feffc0',
          '#b7e7fb', '#8bcff8', '#4eb9f9', '#0091fc', '#0069df',
          '#0b3ecc', '#13209b', '#13036d', '#560094', '#350059']

colors=[[80,0,6],[116,0,12],[184,0,0],[251,56,0],[255,110,0],
        [255,148,0], [255,203,36], [255,230,100], [250,242,150], [254,255,192],
        [183,231,251], [139,207,248], [78,185,249], [0,145,252], [0,105,223],
        [11,62,204], [19,32,155], [19,3,109], [86,0,148], [53,0,89]]
# 将rgb颜色转换为十六进制字符串的函数
def getColorByTemp(temp):
    #print(temp)
    start=45
    end=50
    for i in range(20):
        if (temp >= start and temp <= end):
            return p_colors[i]
        start -= 5;
        end -= 5;
    return '#ffffff'

# 返回主页界面
def home(request):
    #insertAreaShipInfo();
    #getPortByName("香港");
    '''lons = np.linspace(105, 135, 31);
    lats = np.linspace(0, 40, 41);

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    temperature_data = getOneFileData(BASE_DIR + "/climateServices/static/Temperature_height_above_ground_10km_2017010118.000");

    show_colors={}
    for i in range(len(lons)):
        for j in range(len(lats)):
            temp = temperature_data[getIndex(lats[j], lons[i], 0.0, 105.00, 0.1, 401) - 1];
            color = getColorByTemp(float(temp));
            if color not in show_colors.keys():
                show_colors[color]=[];
            show_colors[color].append([str(lons[i]),str(lats[j])])'''

    features_info = getFeatureColor();
    wind_directions_info = getWindDirections();


    return render(request, 'home.html', {'features_info': json.dumps(features_info),
                                         'wind_directions_info': json.dumps(wind_directions_info)});

# 获取主界面的天气信息，今天或者明天的
@csrf_exempt
def get_home_weather_info(request):
    re = request.POST
    date_delay = int(re["date_delay"]);
    features_info = getFeatureColorWithDelay(date_delay);
    return HttpResponse(json.dumps(features_info, ensure_ascii=False), content_type='application/json');

# 返回航线界面
def seaway(request):
    return render(request, 'seaway.html', {'typhoon_warning': json.dumps(getTyphoon())});

# 返回台风界面
def typhoon(request):
    allships = getAreaShipInfo();
    now_time = datetime.datetime.now().strftime('%Y%m%d');
    now_time = now_time[:3] + '7' + now_time[4:];
    #print(now_time)
    now_time = "20171220";
    # 获取该时间之后的台风信息
    current_typhoon = search_typhoon_info(now_time, 1);
    all_typhoon= search_all_typhoon_info();
    #getShipInfo();

    #print(current_typhoon);
    return render(request, 'typhoon.html', {'current_typhoon': json.dumps(current_typhoon['name']),
                                            'typhoon_warning': json.dumps(getTyphoonOneLine()),
                                            'all_typhoon': json.dumps(all_typhoon['name']),
                                            'all_ships': json.dumps(allships)
                                            });
# 获取某个台风信息
@csrf_exempt
def get_typhoon_info(request):
    re = request.body
    re = re.decode("utf-8")
    re = eval(re)
    keywords = re['typhoon_name'];
    limit = re['pageSize'];
    offset = re['offset'];

    now_time = datetime.datetime.now().strftime('%Y%m%d');
    now_time = now_time[:3] + '7' + now_time[4:];
    now_time = "20171220";

    current_typhoon = search_typhoon_info(now_time, 1);
    res = current_typhoon["typhoons_infos"][keywords];
    length = len(res);
    # 根据分页情况返回表格信息
    data = {"total":length, "rows":res[offset:offset+limit]};
    return HttpResponse(json.dumps(data,ensure_ascii=False), content_type='application/json');

# 获取所有台风信息
@csrf_exempt
def get_typhoon_all_info(request):
    re = request.body
    re = re.decode("utf-8")
    re = eval(re)
    keywords = re['typhoon_name'];
    limit = re['pageSize'];
    offset = re['offset'];

    current_typhoon = search_all_typhoon_info();
    res = current_typhoon["typhoons_infos"][keywords];
    length = len(res);
    data = {"total":length, "rows":res[offset:offset+limit]};
    return HttpResponse(json.dumps(data,ensure_ascii=False), content_type='application/json');

# 根据台风名称获取当前时间以后的台风路径信息
@csrf_exempt
def get_path_info(request):
    re = request.POST
    name = re["typhoon_name"]
    now_time = datetime.datetime.now().strftime('%Y%m%d');
    now_time = now_time[:3] + '7' + now_time[4:] + '00';
    now_time = "2017122000";
    data = search_typhoon_path_info(now_time, name);
    return HttpResponse(json.dumps(data,ensure_ascii=False), content_type='application/json');

# 根据台风名称获取台风路径信息
@csrf_exempt
def get_history_path_info(request):
    re = request.POST
    name = re["typhoon_name"]
    data = search_histoty_typhoon_path_info(name);
    return HttpResponse(json.dumps(data,ensure_ascii=False), content_type='application/json');

# 根据表格分页情况，获取某一个表格页中心点某半径圆区域内的船只信息
@csrf_exempt
def get_ship_info(request):
    re = request.body
    re = re.decode("utf-8")
    re = eval(re)
    limit = re['pageSize'];
    offset = re['offset'];
    pos = re['centerPos'];
    radius = re['radius']
    #print(pos);

    res = getCirclesShips(float(pos[1]),float(pos[0]),int(radius));
    length = len(res);
    data = {"total":length, "rows":res[offset:offset+limit]};
    return HttpResponse(json.dumps(data,ensure_ascii=False), content_type='application/json');

# 获取中心点某半径圆区域内的船只信息
@csrf_exempt
def get_circle_ship_info(request):
    re = request.POST
    pos = [re['lon'], re['lat']];
    radius = re['radius']
    res = getCirclesShipsWithPos(float(pos[1]),float(pos[0]),int(radius));
    return HttpResponse(json.dumps(res,ensure_ascii=False), content_type='application/json');


# 船只界面左栏图表格式信息，输入图表曲线数据
def ship_temperature_data(data):
    chart = {
        'zoomType': 'x'
    }
    #图表标题
    title = {
        'text': '未来2天温度变化',
        'style': {
            "fontSize": "15px"
        }
    };
   #图表x轴设置
    xAxis = {
        'type':'datetime',
        'maxZoom': 24*3600*1000
    };
    #图表y轴设置
    yAxis = {
        'title': ''
    };
    #图表显示单位
    tooltip = {
        'valueSuffix': '\xB0C'
    }
    #图表显示设置
    legend = {
        'layout': 'horizontal',
        'align': 'center',
        'verticalAlign': 'top',
        'borderWidth': 0
    };
    # 图表数据信息
    series = [
        {
            'name':"温度",
            'data': data,
            'pointInterval':1*3600*1000,
            'color': '#FF0000'
        },
    ];
    data = [{'title':title, 'chart':chart,  'xAxis': xAxis, 'yAxis':yAxis, 'tooltip':tooltip, 'legend':legend,'series': series}]
    return data
    
# 船只界面左栏图表格式信息，输入图表曲线数据、表头、以及图数据点的间隔
def ship_chart_data(data, title_info, point_interval):
    chart = {
        'zoomType': 'x'
    }
    title = {
        'text': title_info,
        'style': {
            "fontSize": "15px"
        }
    };

    xAxis = {
        'type':'datetime',
        'maxZoom': 24*3600*1000
    };
    yAxis = {
        'title': ''
    };
    tooltip = {
        'valueSuffix': '%'
    }

    legend = {
        'layout': 'horizontal',
        'align': 'center',
        'verticalAlign': 'top',
        'borderWidth': 0
    };

    series = [
        {
            'type': 'area',
            'data': data,
            'pointInterval':point_interval,
            #'color': '#FF0000'
        },
    ];
    data = [{'title':title, 'chart':chart,  'xAxis': xAxis, 'yAxis':yAxis, 'tooltip':tooltip, 'legend':legend,'series': series}]
    return data


# 航线界面图表格式，输入图表表头、数据、以及数据值的单位
def seaway_chart_data(title_info, data, unit):
    categories =[];
    categories.append('')
    for i in range(8):
        categories.append(str(data[i]['timev']))
    chart = {
        #'zoomType': 'x'
        'type': 'spline'
    }
    title = {
        'text': title_info,
        'style': {
            "fontSize": "15px"
        }
    };

    xAxis = {
        'title': {
            'text': '出发地-目的地'
        },
        'categories': categories
    };
    scrollbar = {
        'enabled': 'true'
    },
    yAxis = {
        'title': '',
        'labels': {
            'format': '{value}'+unit
        }
    };
    tooltip = {
        'headerFormat': '距离出发时间{point.x}<br>',
        'pointFormat': '经纬度坐标[{point.lon}, {point.lat}]<br>预测值{point.y}'+unit
    }

    legend = {
        'layout': 'horizontal',
        'align': 'center',
        'verticalAlign': 'top',
        'borderWidth': 0,
        'enabled': False
    };
    series = [
        {
            'type':'area',
            'data':data,
            'pointStart':1,
        },
    ];
    chart_data = [{'scrollbar':scrollbar,'title':title, 'chart':chart,  'xAxis': xAxis, 'yAxis':yAxis, 'tooltip':tooltip, 'legend':legend,'series': series}]
    return chart_data

# 航线界面，风向显示图表格式，输入数据、表头、数据单位  
def seaway_wind_direction_chart_data(data, title_info, unit):
    categories = [];
    categories.append('')
    for i in range(8):
        categories.append(str(data[i]['timev']))
    chart = {
        'type':'spline'
    }
    title = {
        'useHTML': True,
        'text': '<div>'+ title_info +'<img src="/static/img/wind_direction_img/D.png" style="transform:scale(0.5); vertical-align:middle"/></div>',
        'style': {
            "fontSize": "15px"
        }
    };

    xAxis = {
        'title': {
            'text': '出发地-目的地'
        },
        'categories': categories
    };
    scrollbar = {
                    'enabled': 'true'
    },
    yAxis = {
        'title': '',
        'labels': {
            'format': '{value}'+unit
        }
    };
    tooltip = {
        'headerFormat': '距离出发时间{point.x}<br>',
        'pointFormat': '经纬度坐标[{point.lon},{point.lat}]<br>预测{point.direction}方向'
    }
    plotOptions = {
        'spline': {
            'marker': {
                'radius': 4,
                'lineColor': '#666666',
                'lineWidth': 0
            }
        }
    };

    legend = {
        'layout': 'horizontal',
        'align': 'center',
        'verticalAlign': 'top',
        'borderWidth': 0,
        'enabled': False
    };
    
    # 风向显示数据
    dataList = []
    for i  in range(0,len(data)):
        dataList.append({
            'y': data[i]['y'],
            'timev':data[i]['timev'],
            'lon':data[i]['lon'],
            'lat':data[i]['lat'],
            'direction': getChineseDirectFromAngle(data[i]['y']),
            'desc': getDirectFlagFromAngle(data[i]['y']),
            'marker': {
                'symbol': 'url(static/img/wind_direction_img/' + getDirectFlagFromAngle(data[i]['y']) + '.png)'
                #'symbol': 'url(static/img/wind_direction_img/N.png)'
            }
        })
    series = [
        {
            'pointStart': 1,
            'data': dataList,
            'color': '#FF0000',
            'marker': {
                'symbol': 'circle'
            },
            "colorByPoint": True
        },
    ];
    credits = {
        "enabled": False
    }
    data = [{'scrollbar':scrollbar, 'title': title, 'chart': chart, 'xAxis': xAxis, 'yAxis': yAxis, 'tooltip': tooltip, 'legend': legend,
             'series': series, 'plotOptions':plotOptions, 'credits':credits}]
    return data

# 船只界面风向图表单位，输入数据、图表表头、数据点间隔
def ship_wind_direction_chart_data(data, title_info, point_interval):
    chart = {
        'type':'spline'
    }
    title = {
        'useHTML': True,
        'text': '<div>'+ title_info +'<img src="/static/img/wind_direction_img/D.png" style="transform:scale(0.5); vertical-align:middle"/></div>',
        'style': {
            "fontSize": "15px"
        }
    };

    xAxis = {
        'type': 'datetime',
        'maxZoom': 24 * 3600 * 1000
    };
    yAxis = {
        'title': ''
    };
    tooltip = {
        'valueSuffix': '%'
    }
    plotOptions = {
        'spline': {
            'marker': {
                'radius': 4,
                'lineColor': '#666666',
                'lineWidth': 0
            }
        }
    };

    legend = {
        'layout': 'horizontal',
        'align': 'center',
        'verticalAlign': 'top',
        'borderWidth': 0
    };
    # 风向显示数据
    dataList = []
    for i  in range(0,len(data)):
        dataList.append({
            'y': data[i],
            'direction': getDirectFlagFromAngle(data[i]),
            'desc': getDirectFlagFromAngle(data[i]),
            'marker': {
                'symbol': 'url(static/img/wind_direction_img/' + getDirectFlagFromAngle(data[i]) + '.png)'
                #'symbol': 'url(static/img/wind_direction_img/N.png)'
            }
        })
    series = [
        {
            'data': dataList,
            'pointInterval': point_interval,
            'color': '#FF0000',
            'marker': {
                'symbol': 'circle'
            },
            "colorByPoint": True
        },
    ];
    credits = {
        "enabled": False
    }
    data = [{'title': title, 'chart': chart, 'xAxis': xAxis, 'yAxis': yAxis, 'tooltip': tooltip, 'legend': legend,
             'series': series, 'plotOptions':plotOptions, 'credits':credits}]
    return data

# 将角度转换成具体的方向，用字符串表示具体的方向NEN
def getDirectFlagFromAngle(angle_str):
    angle_float = float(angle_str);
    direct_list = ['N','NEN','EN','EEN',
                            'E','EES','ES','SES',
                            'S','SWS','WS','WWS',
                            'W','WWN','WN','NWN'];
    for i in range(0, 12):
        if (angle_float > (348.75 + i*22.5)%360 and angle_float <= (11.25 + i*22.5)):
            return direct_list[i];
    return 'N';
# 将角度转换成中文方向，如“北”
def getChineseDirectFromAngle(angle_str):
    angle_float = float(angle_str);
    direct_list = ['北', '北东北', '东北', '东东北',
                   '东', '东东南', '东南', '南东南',
                   '南', '南西南', '西南', '西西南',
                   '西', '西西北', '西北', '北西北'];
    for i in range(0, 12):
        if (angle_float > (348.75 + i*22.5)%360 and angle_float <= (11.25 + i*22.5)):
            return direct_list[i];
    return '北';

# 模拟数据库的船只数据，后期已经替换成数据库的数据
def getShipNames():
    names = [];
    '''html = urllib.request.urlopen(
        #r'http://fleet.shiplinker.com/transMethod.do?cmd=0x0109&param=eyJtbXNpIjoiNDEzMDQwMDIwIn0=');
    r'http://218.205.125.142:10080/transMethod.do?cmd=0x0109&param=eyJtbXNpIjoiNDEzMDQwMDIwIn0=');
    content = html.read();
    if content != b'':
        hjson = json.loads(content.decode('utf-8'))
        names.append(hjson['name']);'''
    names.append("XIN HAI HU")
    names.append('ship1');
    names.append('ship2');
    return names

'''
@csrf_exempt
def set_area(request):
    re = request.POST
    number = re["number"]
    start_lon = re['start_lon']
    start_lat = re['start_lat']
    end_lon = re['end_lon']
    end_lat = re['end_lat']
    start_lon = round(float(start_lon),2)
    start_lat = round(float(start_lat),2)
    end_lon = round(float(end_lon),2)
    end_lat = round(float(end_lat),2)

    if len(TargetArea.objects.filter(number=number)) !=0:
        return HttpResponse(json.dumps({'status':'请选择其他编号，该编号已经被使用过了。'}, ensure_ascii=False), content_type='application/json');
    if len(TargetArea.objects.filter(start_lon=start_lon, start_lat=start_lat,
                                          end_lon=end_lon, end_lat=end_lat)) == 0:
        temp = TargetArea.objects.create(start_lon=start_lon, start_lat=start_lat,
                                          end_lon=end_lon, end_lat=end_lat, number=number);
        temp.save()
        data={'status':'设置成功。'}
    else:
        database_res = TargetArea.objects.filter(start_lon=start_lon, start_lat=start_lat,
                                          end_lon=end_lon, end_lat=end_lat);
        data = {'status': '该目标区域已经设置过编号，编号为' + database_res[0].number}

    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json');
'''
# 获取data中的num个数据
def getPartData(data, num):
    interval = int(math.floor((len(data)/num)));
    res = []
    for i in range(0, num):
        res.append(data[interval*i])
    return res;


# 获取船只界面目标船只的气象信息，包含温度、湿度、风速、风向、降雨量等
@csrf_exempt
def getShipWeather(request):
    re = request.POST
    precision= int(re.get('precision'))/100
    mmsi = re["mmsi"]
    weatherinfo = {};
    weatherinfo['mmsi_ship'] = getShipInfoBymmsi(mmsi);
    ori_long = float(weatherinfo['mmsi_ship']['lon']);
    ori_lat = float(weatherinfo['mmsi_ship']['lat']);

    long = int(ori_long/precision)*precision;
    lat = int(ori_lat/precision)*precision;
    '''if name == "XIN HAI HU":
        long = 114.97;
        lat = 14.05;
    else:
        long = 400;
        lat = 400;
    date = "2017-01-01 00:00:00";
    #weather_attrs = getWeatherAttrs(lat, long, precision, date);'''
    weather_attrs = getWeatherAttrs(lat, long, precision);
    #debugOutputFile(len(weather_attrs));

    #print(weather_attrs);
    if len(weather_attrs) == 0:
        weatherinfo['flag'] = 0;
        return HttpResponse(json.dumps(weatherinfo, ensure_ascii=False), content_type='application/json');
    
    # 获取未来天气情况
    weather_attrs_week = getWeatherAttrsForWeek(lat, long, precision);
    weather_attrs_week["wind_component"] = getPartData(weather_attrs_week["wind_component"], 8);

    temperature_data = ship_chart_data(weather_attrs_week['temperature'], '未来两天温度变化',1*3600*1000);
    humidity_data = ship_chart_data(weather_attrs_week["humidity"], '未来2天湿度变化', 1*3600*1000);
    wind_speed_data = ship_chart_data(weather_attrs_week["wind_speed"], '未来2天风速变化', 1*3600*1000);
    wind_component_data = ship_wind_direction_chart_data(weather_attrs_week["wind_component"], "未来2天风向变化", 6*3600*1000);
    precipitation_data = ship_chart_data(weather_attrs_week["precipitation"], "未来2天降雨量变化",1*3600*1000);
    visibility_data = ship_chart_data(weather_attrs_week["visibility"], "未来2天能见度变化",1*3600*1000);
    sea_wave_data = ship_chart_data(weather_attrs_week["sea_wave"], "未来2天海浪变化",1*3600*1000);
    height_swell_data = ship_chart_data(weather_attrs_week["height_swell"], "未来2天涌流高度变化",1*3600*1000);
    ocean_current_h_data = ship_chart_data(weather_attrs_week["ocean_current_h"], "未来2天海流水位变化",1*3600*1000);


    weatherinfo['flag'] = 1;
    weatherinfo['detail'] = weather_attrs;
    weatherinfo['detail']['long'] = ori_long;
    weatherinfo['detail']['lat'] = ori_lat;


    weatherinfo['chart'] = {};
    weatherinfo['chart']['temperature_chart'] = temperature_data;
    weatherinfo['chart']['humidity_chart'] = humidity_data;
    weatherinfo['chart']['wind_speed_chart'] = wind_speed_data;
    weatherinfo['chart']['wind_component_chart'] = wind_component_data;
    weatherinfo['chart']['precipitation_chart'] = precipitation_data;
    weatherinfo['chart']['visibility_chart'] = visibility_data;
    weatherinfo['chart']['sea_wave_chart'] = sea_wave_data;
    weatherinfo['chart']['height_swell_chart'] = height_swell_data;
    weatherinfo['chart']['ocean_current_h_chart'] = ocean_current_h_data;

    '''html = urllib.request.urlopen(
        #r'http://fleet.shiplinker.com/transMethod.do?cmd=0x010b&param=eyJpZCI6IlM5MzY3MDYxIn0=');
        r'http://218.205.125.142:10080/transMethod.do?cmd=0x0109&param=eyJtbXNpIjoiNDEzMDQwMDIwIn0='); 
    content = html.read();
    if content!=b'':
        data = json.loads(content.decode('utf-8'));'''
    # 根据船只信息查询接口获取船只信息
    url = 'http://218.205.125.144:9600/RTData/AisInfo?mmsi=' + str(mmsi)
    # print(url)
    try:
        html = urllib.request.urlopen(url);
        htmldata = json.loads(html.read().decode('utf-8'));
        weatherinfo['ship_show_info'] = htmldata
    except Exception as e:
        weatherinfo['ship_show_info'] = []

    data={}
    #data['name']="XIN HAI HU";
    data['location'] = [ori_long, ori_lat];
    weatherinfo['ship'] = data;

    return HttpResponse(json.dumps(weatherinfo, ensure_ascii=False), content_type='application/json');



# 根据精度，获取某个经纬度的气象信息
@csrf_exempt
def get_path_pos_weather(request):
    re = request.POST
    precision = 0.05
    long = int(float(re['lon'])/ precision) * precision;
    lat = int(float(re['lat']) / precision) * precision;

    weather_attrs = getWeatherAttrs(lat, long, precision);
    weatherinfo = {};
    if len(weather_attrs) == 0:
        weatherinfo['flag'] = 0;
        return HttpResponse(json.dumps(weatherinfo, ensure_ascii=False), content_type='application/json');

    weatherinfo['flag'] = 1;
    weatherinfo['climate'] = weather_attrs;
    return HttpResponse(json.dumps(weatherinfo, ensure_ascii=False), content_type='application/json');


# 根据精度，获取某个经纬度的气象信息
@csrf_exempt
def get_pos_weather(request):
    re = request.POST
    precision = int(re.get('precision'))/100
    long = int(float(re['lon'])/ precision) * precision;
    lat = int(float(re['lat']) / precision) * precision;

    weather_attrs = getWeatherAttrs(lat, long, precision);
    weatherinfo = {};
    if len(weather_attrs) == 0:
        weatherinfo['flag'] = 0;
        return HttpResponse(json.dumps(weatherinfo, ensure_ascii=False), content_type='application/json');

    weather_attrs_week = getWeatherAttrsForWeek(lat, long, precision);
    weather_attrs_week["wind_component"] = getPartData(weather_attrs_week["wind_component"], 8);

    temperature_data = ship_chart_data(weather_attrs_week['temperature'], '未来两天温度变化',1*3600*1000);
    humidity_data = ship_chart_data(weather_attrs_week["humidity"], '未来2天湿度变化',1*3600*1000);
    wind_speed_data = ship_chart_data(weather_attrs_week["wind_speed"], '未来2天风速变化',1*3600*1000);
    wind_component_data = ship_wind_direction_chart_data(weather_attrs_week["wind_component"], "未来2天风向变化",6*3600*1000);
    precipitation_data = ship_chart_data(weather_attrs_week["precipitation"], "未来2天降雨量变化",1*3600*1000);
    visibility_data = ship_chart_data(weather_attrs_week["visibility"], "未来2天能见度变化",1*3600*1000);
    sea_wave_data = ship_chart_data(weather_attrs_week["sea_wave"], "未来2天海浪变化",1*3600*1000);
    height_swell_data = ship_chart_data(weather_attrs_week["height_swell"], "未来2天涌流高度变化",1*3600*1000);
    ocean_current_h_data = ship_chart_data(weather_attrs_week["ocean_current_h"], "未来2天海流水位变化",1*3600*1000);

    weatherinfo['flag'] = 1;

    weatherinfo['chart'] = {};
    weatherinfo['chart']['temperature_chart'] = temperature_data;
    weatherinfo['chart']['humidity_chart'] = humidity_data;
    weatherinfo['chart']['wind_speed_chart'] = wind_speed_data;
    weatherinfo['chart']['wind_component_chart'] = wind_component_data;
    weatherinfo['chart']['precipitation_chart'] = precipitation_data;
    weatherinfo['chart']['visibility_chart'] = visibility_data;
    weatherinfo['chart']['sea_wave_chart'] = sea_wave_data;
    weatherinfo['chart']['height_swell_chart'] = height_swell_data;
    weatherinfo['chart']['ocean_current_h_chart'] = ocean_current_h_data;
    weatherinfo['climate'] = weather_attrs;
    return HttpResponse(json.dumps(weatherinfo, ensure_ascii=False), content_type='application/json');

# 已知航线的两个端口，输出该航线的所有信息，将航线分成7段，获取8个节点，并将这8个节点的气象属性获取出来，用于航线页面的图表显示
@csrf_exempt
def getSeawayInfo(request):

    re = request.POST
    port1_name =re["ports_id1"]
    port2_name =re["ports_id2"]
    ports =[];
    ports.append(getPortByName(port1_name));
    ports.append(getPortByName(port2_name));
    data={}

    if len(ports) <2 or ports[0]==-1 or ports[1]==-1:
        data["flag"]=0
        return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json');
    '''
    #{"rp_id":"","orig_rp_id":"","leg":-1,"rp_group":"","pointList":"40440#40438"}
    #http://fleet.shiplinker.com/transMethod.do?cmd=0x0501&param=
    url = 'http://fleet.shiplinker.com/transMethod.do?cmd=0x0501&param='
    s = '{"rp_id":"","orig_rp_id":"","leg":-1,"rp_group":"","pointList":"'+str(ports[0])+'#'+str(ports[1])+'"}'
    #print(s)
    url += str(base64.b64encode(s.encode('utf-8')))[2:-2]
    #print(url)
    try:
        html = urllib.request.urlopen(url);
        #print(html)
        debugOutputFile(html);
        htmldata = json.loads(html.read().decode('utf-8'));
        debugOutputFile(htmldata)
        #print(htmldata)
        routes = htmldata[1]['routes']
        paths=[]
        for route in routes:
            pointsets = route['pointset'].split('|')
            for pointset  in pointsets :
                pointset = pointset.split(',')
                if pointset not in paths:
                    paths.append(pointset)
        #print(paths)
        data['flag'] = 1;
        data['paths_info']=divideHangxian(paths,7);
        data['distance']=htmldata[1]['distance'];
        #print(data['paths_info'])
    except Exception as e:
        print(e)
        if (port1_name=="新加坡" and port2_name=="舟山"):
            data['flag'] = 1;
            hangxian = [["103.8333", "1.2667"], ["103.8505", "1.232672"], ["103.9239", "1.224042"], ["104.3222", "1.3364"],
                        ["105.6994", "3.1375"], ["109.3397", "9.9742"], ["114.3397", "17.65315"], ["118.8328", "23.9483"],
                        ["119.8733", "25.2958"], ["120.93", "26.375"], ["122.3539", "28.8831"], ["122.425", "29.7617"],
                        ["122.14", "29.925"], ["122.0969", "29.9297"]]
            data['paths_info'] = divideHangxian(hangxian, 7);
            data['distance'] = data['paths_info'][3];
        elif(port2_name=="新加坡" and port1_name=="舟山"):
            data['flag'] = 1;
            hangxian = [["122.0969", "29.9297"],["122.14", "29.925"],["122.425", "29.7617"],["122.3539", "28.8831"],
                          ["120.93", "26.375"],["119.8733", "25.2958"],["118.8328", "23.9483"],["114.3397", "17.65315"],
                          ["109.3397", "9.9742"],["105.6994", "3.1375"],["104.3222", "1.3364"],["103.9239", "1.224042"],
                          ["103.8505", "1.232672"],["103.8333", "1.2667"]]
            data['paths_info'] = divideHangxian(hangxian, 7);
            data['distance'] = data['paths_info'][3];
        else:
            data["flag"] = 0
            return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json');
    '''
    seaway_paths = getSeawayFastly(ports[0], ports[1]);
    debugOutputFile("@@@@@@@@@@@@@@@@@2")
    if (len(seaway_paths) ==0):
        data["flag"] = 0
        return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json');
    data['flag'] = 1;
    data['paths_info'] = divideHangxian(seaway_paths, 7);
    debugOutputFile("&&&&&&&&&&&&&&&&&&&&")
    debugOutputFile(data['paths_info'])

    position = port1_name + "到" + port2_name;
    # show 5km 2017010100
    # init();
    # pos_attr = WeatherAttrs.objects.filter(longitude=105, latitude=0, data_time="2017-01-01 00:00:00", precision=0.05);

    debugOutputFile("nice**************")
    res = {};
    res['temperature'] = []
    res['date_info'] = []
    res['humidity'] = []
    res["wind_speed"] = []
    res["wind_component"] = []
    res["precipitation"] = []
    res["visibility"] = []
    res["sea_wave"] = []
    res["height_swell"] = []
    res["ocean_current_h"] = []

    now_date = datetime.datetime.now()
    debugOutputFile(len(data['paths_info'][2]))
    debugOutputFile(len(data['paths_info'][1]))
    if (len(data['paths_info'][2]) !=8 or len(data['paths_info'][1])!=8):
        data["flag"] = 0
        return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json');
    
    # 查询路径点的天气情况
    for i in range(len(data['paths_info'][2])):
        #debugOutputFile("get in **************")
        #debugOutputFile(round(data['paths_info'][2][i]))

        cur_date = now_date + datetime.timedelta(hours=round(data['paths_info'][2][i]));
        cur_month = str(cur_date.month)
        cur_day = str(cur_date.day)
        cur_hour = cur_date.hour

        precision = 0.1
        long = round(int(data['paths_info'][1][i][0] / precision) * precision,2);
        lat = round(int(data['paths_info'][1][i][1] / precision) * precision,2);

        # debugOutputFile(precision)
        # debugOutputFile(lat)
        # debugOutputFile(long)
        # debugOutputFile(cur_month)
        # debugOutputFile(cur_day)
        # debugOutputFile(cur_hour)

        pos_info = getWeatherAttrsByTime(lat, long, 0.1, cur_month, cur_day, cur_hour);
        #debugOutputFile(pos_info)
        res['temperature'].append(pos_info["temperature"]);
        res['humidity'].append(pos_info["humidity"]);
        res['wind_speed'].append(pos_info["wind_speed"]);
        res['wind_component'].append(pos_info["wind_component"]);
        res['precipitation'].append(pos_info["precipitation"]);
        res['visibility'].append(pos_info["visibility"]);
        res['sea_wave'].append(pos_info["sea_wave"]);
        res['height_swell'].append(pos_info["height_swell"]);
        res['ocean_current_h'].append(pos_info["ocean_current_h"])

    chart_data = [{'lon': "103.83", 'lat': "1.27", 'timev': "0h", 'y': 25.12},
            {'lon': "107.14", 'lat': "5.84", 'timev': "10h", 'y': 27.25},
            {'lon': "110.27", 'lat': "11.41", 'timev': "20h", 'y': 28.19},
            {'lon': "113.40", 'lat': "16.21", 'timev': "30h", 'y': 24.98},
            {'lon': "116.48", 'lat': "20.65", 'timev': "40h", 'y': 27.95},
            {'lon': "119.52", 'lat': "24.84", 'timev': "50h", 'y': 30.02},
            {'lon': "122.36", 'lat': "28.98", 'timev': "60h", 'y': 27.45},
            {'lon': "122.10", 'lat': "29.92", 'timev': "62h", 'y': 27.37}]
    for index in range(len(data['paths_info'][1])):
        chart_data[index]['lon'] = str(round(data['paths_info'][1][index][0],2));
        chart_data[index]['lat'] = str(round(data['paths_info'][1][index][1],2));
        chart_data[index]['timev'] = str(round(data['paths_info'][2][index],1)) + 'h';
        chart_data[index]['y'] = float(res['temperature'][index]);
    temperature_chart_info = seaway_chart_data(position + "的温度变化曲线图", chart_data, "\xB0C");

    humidity = [90, 87.5, 85.23, 86.45, 80.82, 78.93, 79.65, 80.32]
    humidity_data = copy.deepcopy(chart_data);
    for i in range(len(humidity_data)):
        humidity_data[i]['y'] = float(res['humidity'][i]);
    humidity_chart_info = seaway_chart_data(position + "的湿度变化曲线图", humidity_data, "%")

    wind_speed = [11.29, 11.48, 11.35, 11.41, 11.34, 11.26, 11.31, 11.46]
    wind_speed_data = copy.deepcopy(chart_data);
    for i in range(len(wind_speed)):
        wind_speed_data[i]['y'] = float(res['wind_speed'][i]);
    wind_speed_chart_info = seaway_chart_data(position + "的风速变化曲线图", wind_speed_data, "m/s");

    wind_component = [212.46, 203.36, 194.71, 187.60, 183.87, 185.25, 189.25, 192.62]
    wind_component_info = copy.deepcopy(chart_data);
    for i in range(len(wind_component_info)):
        wind_component_info[i]['y'] = float(res['wind_component'][i]);
    wind_component_chart_info = seaway_wind_direction_chart_data(wind_component_info, position + "的风速变化曲线图", "度");

    precipitation = [2, 0, 8, 3, 0, 0, 0, 4]
    precipitation_info = copy.deepcopy(chart_data);
    for i in range(len(precipitation_info)):
        precipitation_info[i]['y'] = float(res['precipitation'][i]);
    precipitation_chart_info = seaway_chart_data(position + "的降雨量变化曲线图", precipitation_info, "mm");

    visibility = [5660, 5890, 6009, 5893, 6735, 5894, 6003, 6415]
    visibility_info = copy.deepcopy(chart_data);
    for i in range(len(visibility_info)):
        visibility_info[i]['y'] = float(res['visibility'][i]);
    visibility_chart_info = seaway_chart_data(position + "的能见度变化曲线图", visibility_info, "m");

    sea_wave_height = [1.44, 1.35, 1.50, 1.45, 1.37, 1.43, 1.50, 1.38]
    sea_wave_height_info = copy.deepcopy(chart_data);
    for i in range(len(sea_wave_height_info)):
        sea_wave_height_info[i]['y'] = float(res['sea_wave'][i]);
    sea_wave_height_chart_info = seaway_chart_data(position + "的海浪高度变化曲线图", sea_wave_height_info, "m");

    height_swell = [2.77, 2.62, 2.48, 2.33, 2.19, 2.15, 2.12, 2.08]
    height_swell_info = copy.deepcopy(chart_data);
    for i in range(len(height_swell_info)):
        height_swell_info[i]['y'] = float(res['height_swell'][i]);
    height_swell_chart_info = seaway_chart_data(position + "的涌流高度变化曲线图", height_swell_info, "m");

    ocean_current_h = [1.03, 1.02, 1.04, 0.94, 1.01, 1.03, 1.03, 1.00]
    ocean_current_h_info = copy.deepcopy(chart_data);
    for i in range(len(ocean_current_h_info)):
        ocean_current_h_info[i]['y'] = float(res['ocean_current_h'][i]);
    ocean_current_h_chart_info = seaway_chart_data(position + "的海流水位变化曲线图", ocean_current_h_info, "m");

    data['chart'] = {};
    data['chart']['temperature_chart'] = temperature_chart_info;
    data['chart']['humidity_chart'] = humidity_chart_info;
    data['chart']['wind_speed_chart'] = wind_speed_chart_info;
    data['chart']['wind_component_chart'] = wind_component_chart_info;
    data['chart']['precipitation_chart'] = precipitation_chart_info;
    data['chart']['visibility_chart'] = visibility_chart_info;
    data['chart']['sea_wave_chart'] = sea_wave_height_chart_info;
    data['chart']['height_swell_chart'] = height_swell_chart_info;
    data['chart']['ocean_current_h_chart'] = ocean_current_h_chart_info;

    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json');

# 获取所有的船只信息，返回船只界面
def shipinfo(request):
    allships = getAreaShipInfo();
    return render(request, 'ship_meteorology.html', {'typhoon_warning': json.dumps(getTyphoon()),
                                                     'ship_names': json.dumps(getShipNames()),
                                                     'all_ships': json.dumps(allships)});
    '''long=122.20;
    lat=30.00;
    precision=0.05;
    date="2017-01-01 00:00:00";
    weather_attrs = getWeatherAttrs20170101(lat, long, precision, 0);
    weather_attrs_week = getWeatherAttrsForWeek(lat, long, precision, 0);

    debugOutputFile(len(weather_attrs))
    debugOutputFile(len(weather_attrs_week))

    weather_attrs_week["wind_component"] = getPartData(weather_attrs_week["wind_component"], 8);

    temperature_data = ship_chart_data(weather_attrs_week['temperature'], '未来两天温度变化', 1 * 3600 * 1000);
    humidity_data = ship_chart_data(weather_attrs_week["humidity"], '未来2天湿度变化', 1 * 3600 * 1000);
    wind_speed_data = ship_chart_data(weather_attrs_week["wind_speed"], '未来2天风速变化', 1 * 3600 * 1000);
    wind_component_data = ship_wind_direction_chart_data(weather_attrs_week["wind_component"], "未来2天风向变化", 6 * 3600 * 1000);
    precipitation_data = ship_chart_data(weather_attrs_week["precipitation"], "未来2天降雨量变化", 1 * 3600 * 1000);
    visibility_data = ship_chart_data(weather_attrs_week["visibility"], "未来2天能见度变化", 1 * 3600 * 1000);
    sea_wave_data = ship_chart_data(weather_attrs_week["sea_wave"], "未来2天海浪变化", 1 * 3600 * 1000);
    height_swell_data = ship_chart_data(weather_attrs_week["height_swell"], "未来2天涌流高度变化", 1 * 3600 * 1000);
    ocean_current_h_data = ship_chart_data(weather_attrs_week["ocean_current_h"], "未来2天海流水位变化", 1 * 3600 * 1000);

    allships=getAreaShipInfo();

    return render(request, 'ship_meteorology.html', {'weather_attrs': json.dumps(weather_attrs),
                                                     'typhoon_warning': json.dumps(getTyphoon()),
                                                     'ship_temperature_chart': json.dumps(temperature_data),
                                                     'ship_humidity_chart':json.dumps(humidity_data),
                                                     'ship_wind_speed_chart':json.dumps(wind_speed_data),
                                                     'ship_wind_component_chart':json.dumps(wind_component_data),
                                                     'ship_precipitation_chart':json.dumps(precipitation_data),
                                                     'ship_visibility_chart':json.dumps(visibility_data),
                                                     'ship_sea_wave_chart':json.dumps(sea_wave_data),
                                                     'ship_height_swell_chart':json.dumps(height_swell_data),
                                                     'ship_ocean_current_h_chart':json.dumps(ocean_current_h_data),
                                                     'ship_names':json.dumps(getShipNames()),
                                                     'all_ships':json.dumps(allships)})
                                                     '''
# 返回目标区域界面  
def areainfo(request):
    return render(request, 'target_area.html', {'typhoon_warning': json.dumps(getTyphoon())});

# 获取目标区域的天气情况，因为要显示对比网格的信息，所以会返回两个精度的天气属性
@csrf_exempt
def get_area_weather_type(request):
    #debugOutputFile("input get area weather type")
    re = request.POST
    precision = re["precision"]
    precision = int(precision) * 1.0/100
    area = re["area"]
    type = int(re["type"])
    twomeshflag = int(re["twomeshflag"])
    area = json.loads(area)
    coors=[]
    for one_area in area:
        onelon = one_area[0]
        onelat = one_area[1]
        twolon = one_area[2]
        twolat = one_area[3]
        lonnum = int((twolon - onelon)/precision);
        latnum = int((twolat - onelat)/precision);
        #debugOutputFile(lonnum)
        #debugOutputFile(latnum)
        for i in range(lonnum):
            for j in range(-latnum):
                curlon = onelon + i*precision + precision/2;
                curlat = onelat - j*precision - precision/2;
                long = int(curlon / precision) * precision;
                lat = int(curlat / precision) * precision;
                data_hz = getHashValue(long, lat, int(precision*100), 0)
                res = AreaWeatherType.objects.filter(idx_b_hyqx_tqlx_uk=data_hz);
                for oneres in res:
                    #debugOutputFile(oneres)
                    if (oneres.f_it_tqlx == type):
                        coors.append([curlon, curlat]);
        if twomeshflag == 0:
            continue;
        if precision == 0.1:
            other_precision = 0.05;
        else:
            other_precision = 0.1;
        # 更新目标区域的左上角和右下角坐标
        onelon = one_area[0]-(one_area[2]-one_area[0])-0.1;
        onelat = one_area[1]
        twolon = one_area[2]-(one_area[2]-one_area[0])-0.1;
        twolat = one_area[3]
        lonnum = int((twolon - onelon) / other_precision);
        latnum = int((twolat - onelat) / other_precision);
        # debugOutputFile(lonnum)
        # debugOutputFile(latnum)
        for i in range(lonnum):
            for j in range(-latnum):
                curlon = onelon + i * other_precision + other_precision / 2;
                curlat = onelat - j * other_precision - other_precision / 2;
                long = int(curlon / other_precision) * other_precision;
                lat = int(curlat / other_precision) * other_precision;
                data_hz = getHashValue(long, lat, int(other_precision * 100), 0)
                res = AreaWeatherType.objects.filter(idx_b_hyqx_tqlx_uk=data_hz);
                for oneres in res:
                    if (oneres.f_it_tqlx == type):
                        coors.append([curlon, curlat]);

    #debugOutputFile(precision)
    #debugOutputFile(area)
    #debugOutputFile(type)
    #debugOutputFile(coors)
    return HttpResponse(json.dumps(coors, ensure_ascii=False), content_type='application/json');


# 获取区域的天气情况
@csrf_exempt
def get_offshore_weather_type(request):
    #debugOutputFile("input get area weather type")
    re = request.POST
    precision = re["precision"]
    precision = int(precision) * 1.0/100
    area = re["area"]
    area = json.loads(area)
    coors={}
    for one_area in area:
        onelon = one_area[0]
        onelat = one_area[1]
        twolon = one_area[2]
        twolat = one_area[3]
        # 数据库查询数据
        res = AreaWeatherType.objects.filter(f_dl_jd__gte=onelon, f_dl_jd__lte=twolon, f_dl_wd__gte=onelat, f_dl_wd__lte=twolat);
        for oneres in res:
            if (oneres.f_it_tqlx in coors.keys()):
                coors[oneres.f_it_tqlx].append([str(oneres.f_dl_jd), str(oneres.f_dl_wd)])
            else:
                coors[oneres.f_it_tqlx]=[]
                coors[oneres.f_it_tqlx].append([str(oneres.f_dl_jd), str(oneres.f_dl_wd)])
    for i in coors.keys():
        coors[i] = random.sample(coors[i], 5)
    return HttpResponse(json.dumps(coors, ensure_ascii=False), content_type='application/json');


# 首页添加标记
@csrf_exempt
def add_tag(request):
    re = request.POST
    name = re["name"]
    comment = re["comment"]
    img_src = re["img_src"]
    lon = re["lon"]
    lat = re["lat"]

    '''
    class TagInfo(models.Model):
    idx_b_hyqx_dtbj_pk = models.IntegerField(primary_key=True)
    f_vc_yhm = models.CharField(max_length=50)
    f_vc_mc = models.CharField(max_length=50)
    f_vc_bz = models.CharField(max_length=400, null=True)
    f_vc_tb = models.CharField(max_length=50)
    class Meta:
        db_table = 'b_hyqx_dtbj'
        '''
    # 处理首页添加标记情况，如果成功将标记数据写入数据库
    if (len(name) > 50):
        return HttpResponse(json.dumps({'status': 10, 'info': "标记名称超过50个字符，添加标记失败"}, ensure_ascii=False),
                            content_type='application/json');
    if (len(comment) > 400):
        tag = TagInfo.objects.filter(f_vc_mc=name);
        if (len(tag) > 0):
            return HttpResponse(json.dumps({'status': 11, 'info': "标记名称已存在，标记备注超过400个字符，更新标记失败"}, ensure_ascii=False),
                            content_type='application/json');
        else:
            return HttpResponse(json.dumps({'status': 12, 'info': "标记名称已存在，标记备注超过400个字符，添加标记失败"}, ensure_ascii=False),
                                content_type='application/json');
    tag = TagInfo.objects.filter(f_vc_mc=name);
    if (len(tag) > 0):
        TagInfo.objects.filter(f_vc_mc=name).update(f_vc_mc=name, f_vc_bz=comment, f_vc_tb=img_src, f_dl_jd=lon, f_dl_wd=lat)
        return HttpResponse(json.dumps({'status': 13, 'info': "该标记名称已存在，数据库更新标记成功"}, ensure_ascii=False),
                            content_type='application/json');
    else:
        TagInfo.objects.create(f_vc_yhm="admin",f_vc_mc=name, f_vc_bz=comment, f_vc_tb=img_src,f_dl_jd=lon, f_dl_wd=lat)
        return HttpResponse(json.dumps({'status': 14, 'info': "数据库添加标记成功"}, ensure_ascii=False),
                            content_type='application/json');
# 首页删除标记
@csrf_exempt
def delete_tag(request):
    re = request.POST
    name = re["name"]
    tag = TagInfo.objects.filter(f_vc_mc=name);
    if (len(tag) > 0):
        TagInfo.objects.filter(f_vc_mc=name).delete();
        return HttpResponse(json.dumps({'status': 1, 'info': "数据库删除标记成功"}, ensure_ascii=False),
                        content_type='application/json');
    else:
        return HttpResponse(json.dumps({'status': 0, 'info': "数据库不存在该标记名称的标记"}, ensure_ascii=False),
                            content_type='application/json');
# 首页更新标记
@csrf_exempt
def update_tag(request):
    re = request.POST
    ori_name = re["ori_name"]
    tag = TagInfo.objects.filter(f_vc_mc=ori_name);
    #更新成功，则写入数据库
    if (len(tag) > 0):
        TagInfo.objects.filter(f_vc_mc=ori_name).update(f_vc_mc=re["name"], f_vc_bz=re["comment"],
                                                        f_vc_tb=re["img_src"], f_dl_jd=re["lon"], f_dl_wd=re["lat"]);
        return HttpResponse(json.dumps({'status': 1, 'info': "数据库修改标记成功"}, ensure_ascii=False),
                        content_type='application/json');
    else:
        return HttpResponse(json.dumps({'status': 0, 'info': "数据库不存在该标记名称，修改失败"}, ensure_ascii=False),
                            content_type='application/json');

# 首页获取所有的标记
@csrf_exempt
def get_all_tags(request):
    re = request.POST
    yhm = re["yhm"]
    tags = TagInfo.objects.filter(f_vc_yhm=yhm);
    all_tags={}
    for one in tags:
        all_tags[one.f_vc_mc] = [str(one.f_dl_jd), str(one.f_dl_wd),one.f_vc_tb];
    return HttpResponse(json.dumps(all_tags, ensure_ascii=False), content_type='application/json');


# 首页，根据名称获取标记信息
@csrf_exempt
def get_one_tag(request):
    re = request.POST
    name = re["name"]
    tags = TagInfo.objects.filter(f_vc_mc=name);
    one_tag={}
    for one in tags:
        one_tag["name"] = one.f_vc_mc
        one_tag["comment"] = one.f_vc_bz
        one_tag["img_src"] = one.f_vc_tb;
        one_tag["lon"] = str(one.f_dl_jd);
        one_tag["lat"] = str(one.f_dl_wd);
        break;
    return HttpResponse(json.dumps(one_tag, ensure_ascii=False), content_type='application/json');


