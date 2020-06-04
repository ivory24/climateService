"""climateServices URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from climateApp import views
from django.conf.urls import url

from climateApp.views import *

urlpatterns = [
    path(r'home', views.home, name='home'),
    path(r'seaway', views.seaway, name='seaway'),
    path(r'typhoon', views.typhoon, name='typhoon'),
    path(r'ship', views.shipinfo, name='ship'),
    path(r'area', views.areainfo, name='area'),

]


urlpatterns += [
    url(r'^home/get_home_weather_info$', views.get_home_weather_info),
    url(r'^typhoon/get_typhoon_info$', views.get_typhoon_info),
    url(r'^typhoon/get_typhoon_all_info$', views.get_typhoon_all_info),
    url(r'^typhoon/get_ship_table_info$', views.get_ship_info),
    url(r'^typhoon/get_path_info$', views.get_path_info),
    url(r'^typhoon/get_history_path_info$', views.get_history_path_info),
    url(r'^typhoon/get_circle_ship_info$', views.get_circle_ship_info),
    url(r'^ship/get_ship_weather$', views.getShipWeather),
    #url(r'^target_area/set_area$', views.set_area),
    url(r'^target_area/get_pos_weather$', views.get_pos_weather),
    url(r'^seaway/get_seaway_info$', views.getSeawayInfo),
    url(r'^seaway/get_path_pos_weather$', views.get_path_pos_weather),
    url(r'^target_area/get_area_weather_type$', views.get_area_weather_type),
    url(r'^target_area/get_offshore_weather_type$', views.get_offshore_weather_type),
    url(r'^home/add_tag$', views.add_tag),
    url(r'^home/delete_tag$', views.delete_tag),
    url(r'^home/update_tag$', views.update_tag),
    url(r'^home/get_all_tags$', views.get_all_tags),
    url(r'^home/get_one_tag$', views.get_one_tag)
]