from django.shortcuts import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from climateApp.controllers.weather_attr.get_attr import *

# 实现单点登录，需要的中间件
def auth_token(request, token_v):
    try:
        html = urllib.request.urlopen("http://218.205.125.100/jfinal_sso/member/loged?token=" + token_v);
        htmldata = json.loads(html.read().decode('utf-8'));
        debugOutputFile(htmldata)
        # print(htmldata)
        auth_code = htmldata['code']
        if auth_code == '0':
            debugOutputFile("error open auth url 0")
            return None
        elif auth_code == '1':
            debugOutputFile("error open auth url 1")
        else:
            return HttpResponseRedirect('http://218.205.125.100/jfinal_sso/member/logout');
    except Exception as e:
        debugOutputFile("error open auth url")

# 自定义中间件类
class UsersAuthMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        debugOutputFile("nice")
        debugOutputFile(request.get_full_path())
        # 获取session内用户的登录标识
        if 'token' not in request.GET:
            debugOutputFile("not in get")
            debugOutputFile(request.COOKIES)
            if 'token' not in request.COOKIES:
                debugOutputFile("not in COOKIES")
                return HttpResponseRedirect('http://218.205.125.100/jfinal_sso/member/logout');
            else:
                debugOutputFile("in COOKIES")
                return auth_token(request, request.COOKIES.get('token'))
        else:
            debugOutputFile(request.GET)
            token = request.GET["token"];
            return auth_token(request, token)



