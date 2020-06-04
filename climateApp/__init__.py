import pymysql

from django.core import signals
from django.db import close_old_connections

pymysql.install_as_MySQLdb()
signals.request_finished.disconnect(close_old_connections)
