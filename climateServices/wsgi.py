"""
WSGI config for climateServices project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import os

import sys
#该网页端程序使用的是Python的Django框架，实现之后需要通过Apache实现外部部署，Apache部署外部项目需要改wsgi组件

sys.path.append('/home/code/climateServices')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'climateServices.settings')

application = get_wsgi_application()
