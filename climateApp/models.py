from django.db import models

# Create your models here. wq

# 数据库所有数据表的信息，台风信息表
class Typhoon(models.Model):
    idx_b_hyqx_tf_pk = models.IntegerField(primary_key=True)
    f_dl_zlfl = models.DecimalField(max_digits=5,decimal_places=0);
    f_dl_gjbh = models.DecimalField(max_digits=4,decimal_places=0);
    f_dl_ljhs = models.DecimalField(max_digits=3,decimal_places=0);
    f_dl_xh = models.DecimalField(max_digits=4,decimal_places=0);
    f_dl_bh = models.DecimalField(max_digits=4,decimal_places=0);
    f_dl_zjjl = models.DecimalField(max_digits=1,decimal_places=0);
    f_dl_sjjg = models.DecimalField(max_digits=1,decimal_places=0);
    f_vc_mz = models.CharField(max_length=20);
    f_dt_jlsj = models.DateTimeField();
    f_dt_tfsj = models.DateTimeField();
    f_dl_qd = models.DecimalField(max_digits=1,decimal_places=0);
    f_dl_wd = models.DecimalField(max_digits=4,decimal_places=0);
    f_dl_jd = models.DecimalField(max_digits=4,decimal_places=0);
    f_dl_zdqy = models.DecimalField(max_digits=5,decimal_places=0);
    f_dl_zdfs = models.DecimalField(max_digits=3,decimal_places=0);

    class Meta:
        db_table = "b_hyqx_tf"
# 船只信息表
class ShipInfo(models.Model):
    idx_b_hyqx_cz_pk = models.IntegerField(primary_key=True)
    f_it_hjx = models.IntegerField();
    f_vc_mmsi = models.CharField(max_length=9)
    f_dt_sj = models.DateTimeField()
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_czlx = models.IntegerField();
    class Meta:
        db_table = 'b_hyqx_cz'

# 航线端口信息表
class PortInfo(models.Model):
    idx_b_hyqx_gk_pk = models.IntegerField(primary_key=True)
    f_it_gkh = models.IntegerField();
    f_it_iso3 = models.IntegerField();
    f_vc_mz = models.CharField(max_length=255);
    f_vc_zwm = models.CharField(max_length=255);
    f_dl_wd = models.DecimalField(max_digits=7, decimal_places=4);
    f_dl_jd = models.DecimalField(max_digits=7, decimal_places=4);
    class Meta:
        db_table = 'b_hyqx_gk'
# 航线信息表
class SeawayInfo(models.Model):
    idx_b_hyqx_hx_pk = models.IntegerField(primary_key=True)
    f_it_gkhx = models.IntegerField();
    f_it_gkhd = models.IntegerField();
    f_tf_hx = models.TextField(max_length=None);  # 航线
    class Meta:
        db_table = 'b_hyqx_hx'

# 台风界面船只信息表
class TyphoonShipInfo(models.Model):
    idx_b_hyqx_tfcz_pk = models.IntegerField(primary_key=True)
    f_vc_mmsi = models.CharField(max_length=9)
    f_dt_sj = models.DateTimeField()
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_vc_mz = models.CharField(max_length=50)
    f_it_czlx = models.IntegerField();
    f_vc_hh = models.CharField(max_length=50)
    class Meta:
        db_table = 'b_hyqx_tfcz'

# 目标区域天气属性信息表
class AreaWeatherType(models.Model):
    idx_b_hyqx_tqlx_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_tqlx = models.IntegerField();  # 天气类型
    idx_b_hyqx_tqlx_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True);
    f_it_jnd = models.IntegerField();
    class Meta:
        db_table = 'b_hyqx_tqlx'
# 首页标签信息表
class TagInfo(models.Model):
    idx_b_hyqx_dtbj_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=15, decimal_places=12);  # 180.00
    f_dl_wd = models.DecimalField(max_digits=15, decimal_places=12);
    f_vc_yhm = models.CharField(max_length=50)
    f_vc_mc = models.CharField(max_length=50)
    f_vc_bz = models.CharField(max_length=400, null=True)
    f_vc_tb = models.CharField(max_length=50)
    class Meta:
        db_table = 'b_hyqx_dtbj'

# 天气属性信息表，包含精度、经纬度、温度、湿度、能见度等
class WeatherAttrs20170101(models.Model):
    idx_b_hyqx_20170101_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170101_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170101'


class WeatherAttrs20170102(models.Model):
    idx_b_hyqx_20170102_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170102_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170102'

class WeatherAttrs20170103(models.Model):
    idx_b_hyqx_20170103_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170103_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170103'

class WeatherAttrs20170104(models.Model):
    idx_b_hyqx_20170104_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170104_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170104'

class WeatherAttrs20170105(models.Model):
    idx_b_hyqx_20170105_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170105_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170105'

class WeatherAttrs20170106(models.Model):
    idx_b_hyqx_20170106_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170106_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170106'



class WeatherAttrs20170107(models.Model):
    idx_b_hyqx_20170107_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170107_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170107'

class WeatherAttrs20170108(models.Model):
    idx_b_hyqx_20170108_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170108_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170108'

class WeatherAttrs20170109(models.Model):
    idx_b_hyqx_20170109_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170109_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170109'

class WeatherAttrs20170110(models.Model):
    idx_b_hyqx_20170110_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170110_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170110'

class WeatherAttrs20170111(models.Model):
    idx_b_hyqx_20170111_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170111_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170111'

class WeatherAttrs20170112(models.Model):
    idx_b_hyqx_20170112_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170112_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170112'


class WeatherAttrs20170113(models.Model):
    idx_b_hyqx_20170113_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170113_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170113'

class WeatherAttrs20170114(models.Model):
    idx_b_hyqx_20170114_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170114_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170114'

class WeatherAttrs20170115(models.Model):
    idx_b_hyqx_20170115_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170115_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170115'

class WeatherAttrs20170116(models.Model):
    idx_b_hyqx_20170116_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170116_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170116'

class WeatherAttrs20170117(models.Model):
    idx_b_hyqx_20170117_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170117_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170117'

class WeatherAttrs20170118(models.Model):
    idx_b_hyqx_20170118_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170118_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170118'

class WeatherAttrs20170119(models.Model):
    idx_b_hyqx_20170119_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170119_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170119'

class WeatherAttrs20170120(models.Model):
    idx_b_hyqx_20170120_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170120_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170120'

class WeatherAttrs20170121(models.Model):
    idx_b_hyqx_20170121_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170121_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170121'

class WeatherAttrs20170122(models.Model):
    idx_b_hyqx_20170122_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170122_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170122'

class WeatherAttrs20170123(models.Model):
    idx_b_hyqx_20170123_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170123_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170123'

class WeatherAttrs20170124(models.Model):
    idx_b_hyqx_20170124_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170124_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170124'

class WeatherAttrs20170125(models.Model):
    idx_b_hyqx_20170125_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170125_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170125'

class WeatherAttrs20170126(models.Model):
    idx_b_hyqx_20170126_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170126_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170126'

class WeatherAttrs20170127(models.Model):
    idx_b_hyqx_20170127_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170127_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170127'

class WeatherAttrs20170128(models.Model):
    idx_b_hyqx_20170128_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170128_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170128'


class WeatherAttrs20170129(models.Model):
    idx_b_hyqx_20170129_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170129_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170129'


class WeatherAttrs20170130(models.Model):
    idx_b_hyqx_20170130_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170130_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170130'

class WeatherAttrs20170131(models.Model):
    idx_b_hyqx_20170131_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170131_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170131'

class WeatherAttrs20171201(models.Model):
    idx_b_hyqx_20171201_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171201_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171201'


class WeatherAttrs20171202(models.Model):
    idx_b_hyqx_20171202_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171202_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171202'


class WeatherAttrs20171203(models.Model):
    idx_b_hyqx_20171203_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171203_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171203'

class WeatherAttrs20171204(models.Model):
    idx_b_hyqx_20171204_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171204_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171204'


class WeatherAttrs20171205(models.Model):
    idx_b_hyqx_20171205_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171205_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171205'


class WeatherAttrs20171206(models.Model):
    idx_b_hyqx_20171206_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171206_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171206'


class WeatherAttrs20171207(models.Model):
    idx_b_hyqx_20171207_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171207_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171207'


class WeatherAttrs20171208(models.Model):
    idx_b_hyqx_20171208_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171208_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171208'

class WeatherAttrs20171209(models.Model):
    idx_b_hyqx_20171209_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171209_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171209'


class WeatherAttrs20171210(models.Model):
    idx_b_hyqx_20171210_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171210_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171210'

class WeatherAttrs20171211(models.Model):
    idx_b_hyqx_20171211_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171211_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171211'


class WeatherAttrs20171212(models.Model):
    idx_b_hyqx_20171212_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171212_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171212'

class WeatherAttrs20171213(models.Model):
    idx_b_hyqx_20171213_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171213_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171213'

class WeatherAttrs20171214(models.Model):
    idx_b_hyqx_20171214_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171214_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171214'

class WeatherAttrs20171215(models.Model):
    idx_b_hyqx_20171215_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171215_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171215'

class WeatherAttrs20171216(models.Model):
    idx_b_hyqx_20171216_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171216_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171216'

class WeatherAttrs20171217(models.Model):
    idx_b_hyqx_20171217_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171217_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171217'

class WeatherAttrs20171218(models.Model):
    idx_b_hyqx_20171218_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171218_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171218'


class WeatherAttrs20171219(models.Model):
    idx_b_hyqx_20171219_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171219_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171219'

class WeatherAttrs20171220(models.Model):
    idx_b_hyqx_20171220_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171220_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171220'

class WeatherAttrs20171221(models.Model):
    idx_b_hyqx_20171221_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171221_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171221'

class WeatherAttrs20171222(models.Model):
    idx_b_hyqx_20171222_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171222_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171222'


class WeatherAttrs20171223(models.Model):
    idx_b_hyqx_20171223_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171223_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171223'


class WeatherAttrs20171224(models.Model):
    idx_b_hyqx_20171224_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171224_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171224'


class WeatherAttrs20171225(models.Model):
    idx_b_hyqx_20171225_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171225_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171225'

class WeatherAttrs20171226(models.Model):
    idx_b_hyqx_20171226_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171226_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171226'


class WeatherAttrs20171227(models.Model):
    idx_b_hyqx_20171227_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171227_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171227'

class WeatherAttrs20171228(models.Model):
    idx_b_hyqx_20171228_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171228_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171228'


class WeatherAttrs20171229(models.Model):
    idx_b_hyqx_20171229_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171229_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171229'

class WeatherAttrs20171230(models.Model):
    idx_b_hyqx_20171230_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时


    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171230_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171230'

class WeatherAttrs20171231(models.Model):
    idx_b_hyqx_20171231_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2); #180.00
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时

    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪

    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向

    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动

    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171231_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值

    class Meta:
        db_table = 'b_hyqx_20171231'

class WeatherAttrs20170201(models.Model):
    idx_b_hyqx_20170201_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170201_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170201'
class WeatherAttrs20170202(models.Model):
    idx_b_hyqx_20170202_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170202_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170202'
class WeatherAttrs20170203(models.Model):
    idx_b_hyqx_20170203_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170203_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170203'
class WeatherAttrs20170204(models.Model):
    idx_b_hyqx_20170204_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170204_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170204'
class WeatherAttrs20170205(models.Model):
    idx_b_hyqx_20170205_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170205_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170205'
class WeatherAttrs20170206(models.Model):
    idx_b_hyqx_20170206_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170206_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170206'
class WeatherAttrs20170207(models.Model):
    idx_b_hyqx_20170207_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170207_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170207'
class WeatherAttrs20170208(models.Model):
    idx_b_hyqx_20170208_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170208_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170208'
class WeatherAttrs20170209(models.Model):
    idx_b_hyqx_20170209_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170209_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170209'
class WeatherAttrs20170210(models.Model):
    idx_b_hyqx_20170210_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170210_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170210'
class WeatherAttrs20170211(models.Model):
    idx_b_hyqx_20170211_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170211_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170211'
class WeatherAttrs20170212(models.Model):
    idx_b_hyqx_20170212_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170212_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170212'
class WeatherAttrs20170213(models.Model):
    idx_b_hyqx_20170213_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170213_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170213'
class WeatherAttrs20170214(models.Model):
    idx_b_hyqx_20170214_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170214_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170214'
class WeatherAttrs20170215(models.Model):
    idx_b_hyqx_20170215_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170215_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170215'
class WeatherAttrs20170216(models.Model):
    idx_b_hyqx_20170216_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170216_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170216'
class WeatherAttrs20170217(models.Model):
    idx_b_hyqx_20170217_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170217_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170217'
class WeatherAttrs20170218(models.Model):
    idx_b_hyqx_20170218_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170218_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170218'
class WeatherAttrs20170219(models.Model):
    idx_b_hyqx_20170219_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170219_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170219'
class WeatherAttrs20170220(models.Model):
    idx_b_hyqx_20170220_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170220_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170220'
class WeatherAttrs20170221(models.Model):
    idx_b_hyqx_20170221_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170221_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170221'
class WeatherAttrs20170222(models.Model):
    idx_b_hyqx_20170222_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170222_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170222'
class WeatherAttrs20170223(models.Model):
    idx_b_hyqx_20170223_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170223_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170223'
class WeatherAttrs20170224(models.Model):
    idx_b_hyqx_20170224_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170224_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170224'
class WeatherAttrs20170225(models.Model):
    idx_b_hyqx_20170225_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170225_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170225'
class WeatherAttrs20170226(models.Model):
    idx_b_hyqx_20170226_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170226_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170226'
class WeatherAttrs20170227(models.Model):
    idx_b_hyqx_20170227_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170227_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170227'
class WeatherAttrs20170228(models.Model):
    idx_b_hyqx_20170228_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170228_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170228'
class WeatherAttrs20170301(models.Model):
    idx_b_hyqx_20170301_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170301_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170301'
class WeatherAttrs20170302(models.Model):
    idx_b_hyqx_20170302_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170302_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170302'
class WeatherAttrs20170303(models.Model):
    idx_b_hyqx_20170303_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170303_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170303'
class WeatherAttrs20170304(models.Model):
    idx_b_hyqx_20170304_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170304_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170304'
class WeatherAttrs20170305(models.Model):
    idx_b_hyqx_20170305_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170305_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170305'
class WeatherAttrs20170306(models.Model):
    idx_b_hyqx_20170306_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170306_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170306'
class WeatherAttrs20170307(models.Model):
    idx_b_hyqx_20170307_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170307_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170307'
class WeatherAttrs20170308(models.Model):
    idx_b_hyqx_20170308_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170308_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170308'
class WeatherAttrs20170309(models.Model):
    idx_b_hyqx_20170309_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170309_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170309'
class WeatherAttrs20170310(models.Model):
    idx_b_hyqx_20170310_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170310_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170310'
class WeatherAttrs20170311(models.Model):
    idx_b_hyqx_20170311_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170311_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170311'
class WeatherAttrs20170312(models.Model):
    idx_b_hyqx_20170312_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170312_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170312'
class WeatherAttrs20170313(models.Model):
    idx_b_hyqx_20170313_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170313_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170313'
class WeatherAttrs20170314(models.Model):
    idx_b_hyqx_20170314_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170314_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170314'
class WeatherAttrs20170315(models.Model):
    idx_b_hyqx_20170315_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170315_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170315'
class WeatherAttrs20170316(models.Model):
    idx_b_hyqx_20170316_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170316_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170316'
class WeatherAttrs20170317(models.Model):
    idx_b_hyqx_20170317_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170317_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170317'
class WeatherAttrs20170318(models.Model):
    idx_b_hyqx_20170318_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170318_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170318'
class WeatherAttrs20170319(models.Model):
    idx_b_hyqx_20170319_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170319_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170319'
class WeatherAttrs20170320(models.Model):
    idx_b_hyqx_20170320_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170320_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170320'
class WeatherAttrs20170321(models.Model):
    idx_b_hyqx_20170321_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170321_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170321'
class WeatherAttrs20170322(models.Model):
    idx_b_hyqx_20170322_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170322_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170322'
class WeatherAttrs20170323(models.Model):
    idx_b_hyqx_20170323_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170323_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170323'
class WeatherAttrs20170324(models.Model):
    idx_b_hyqx_20170324_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170324_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170324'
class WeatherAttrs20170325(models.Model):
    idx_b_hyqx_20170325_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170325_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170325'
class WeatherAttrs20170326(models.Model):
    idx_b_hyqx_20170326_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170326_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170326'
class WeatherAttrs20170327(models.Model):
    idx_b_hyqx_20170327_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170327_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170327'
class WeatherAttrs20170328(models.Model):
    idx_b_hyqx_20170328_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170328_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170328'
class WeatherAttrs20170329(models.Model):
    idx_b_hyqx_20170329_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170329_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170329'
class WeatherAttrs20170330(models.Model):
    idx_b_hyqx_20170330_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170330_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170330'
class WeatherAttrs20170331(models.Model):
    idx_b_hyqx_20170331_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170331_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170331'
class WeatherAttrs20170401(models.Model):
    idx_b_hyqx_20170401_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170401_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170401'
class WeatherAttrs20170402(models.Model):
    idx_b_hyqx_20170402_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170402_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170402'
class WeatherAttrs20170403(models.Model):
    idx_b_hyqx_20170403_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170403_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170403'
class WeatherAttrs20170404(models.Model):
    idx_b_hyqx_20170404_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170404_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170404'
class WeatherAttrs20170405(models.Model):
    idx_b_hyqx_20170405_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170405_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170405'
class WeatherAttrs20170406(models.Model):
    idx_b_hyqx_20170406_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170406_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170406'
class WeatherAttrs20170407(models.Model):
    idx_b_hyqx_20170407_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170407_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170407'
class WeatherAttrs20170408(models.Model):
    idx_b_hyqx_20170408_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170408_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170408'
class WeatherAttrs20170409(models.Model):
    idx_b_hyqx_20170409_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170409_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170409'
class WeatherAttrs20170410(models.Model):
    idx_b_hyqx_20170410_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170410_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170410'
class WeatherAttrs20170411(models.Model):
    idx_b_hyqx_20170411_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170411_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170411'
class WeatherAttrs20170412(models.Model):
    idx_b_hyqx_20170412_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170412_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170412'
class WeatherAttrs20170413(models.Model):
    idx_b_hyqx_20170413_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170413_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170413'
class WeatherAttrs20170414(models.Model):
    idx_b_hyqx_20170414_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170414_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170414'
class WeatherAttrs20170415(models.Model):
    idx_b_hyqx_20170415_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170415_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170415'
class WeatherAttrs20170416(models.Model):
    idx_b_hyqx_20170416_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170416_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170416'
class WeatherAttrs20170417(models.Model):
    idx_b_hyqx_20170417_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170417_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170417'
class WeatherAttrs20170418(models.Model):
    idx_b_hyqx_20170418_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170418_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170418'
class WeatherAttrs20170419(models.Model):
    idx_b_hyqx_20170419_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170419_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170419'
class WeatherAttrs20170420(models.Model):
    idx_b_hyqx_20170420_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170420_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170420'
class WeatherAttrs20170421(models.Model):
    idx_b_hyqx_20170421_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170421_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170421'
class WeatherAttrs20170422(models.Model):
    idx_b_hyqx_20170422_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170422_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170422'
class WeatherAttrs20170423(models.Model):
    idx_b_hyqx_20170423_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170423_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170423'
class WeatherAttrs20170424(models.Model):
    idx_b_hyqx_20170424_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170424_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170424'
class WeatherAttrs20170425(models.Model):
    idx_b_hyqx_20170425_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170425_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170425'
class WeatherAttrs20170426(models.Model):
    idx_b_hyqx_20170426_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170426_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170426'
class WeatherAttrs20170427(models.Model):
    idx_b_hyqx_20170427_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170427_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170427'
class WeatherAttrs20170428(models.Model):
    idx_b_hyqx_20170428_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170428_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170428'
class WeatherAttrs20170429(models.Model):
    idx_b_hyqx_20170429_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170429_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170429'
class WeatherAttrs20170430(models.Model):
    idx_b_hyqx_20170430_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170430_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170430'
class WeatherAttrs20170501(models.Model):
    idx_b_hyqx_20170501_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170501_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170501'
class WeatherAttrs20170502(models.Model):
    idx_b_hyqx_20170502_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170502_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170502'
class WeatherAttrs20170503(models.Model):
    idx_b_hyqx_20170503_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170503_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170503'
class WeatherAttrs20170504(models.Model):
    idx_b_hyqx_20170504_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170504_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170504'
class WeatherAttrs20170505(models.Model):
    idx_b_hyqx_20170505_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170505_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170505'
class WeatherAttrs20170506(models.Model):
    idx_b_hyqx_20170506_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170506_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170506'
class WeatherAttrs20170507(models.Model):
    idx_b_hyqx_20170507_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170507_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170507'
class WeatherAttrs20170508(models.Model):
    idx_b_hyqx_20170508_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170508_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170508'
class WeatherAttrs20170509(models.Model):
    idx_b_hyqx_20170509_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170509_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170509'
class WeatherAttrs20170510(models.Model):
    idx_b_hyqx_20170510_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170510_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170510'
class WeatherAttrs20170511(models.Model):
    idx_b_hyqx_20170511_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170511_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170511'
class WeatherAttrs20170512(models.Model):
    idx_b_hyqx_20170512_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170512_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170512'
class WeatherAttrs20170513(models.Model):
    idx_b_hyqx_20170513_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170513_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170513'
class WeatherAttrs20170514(models.Model):
    idx_b_hyqx_20170514_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170514_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170514'
class WeatherAttrs20170515(models.Model):
    idx_b_hyqx_20170515_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170515_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170515'
class WeatherAttrs20170516(models.Model):
    idx_b_hyqx_20170516_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170516_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170516'
class WeatherAttrs20170517(models.Model):
    idx_b_hyqx_20170517_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170517_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170517'
class WeatherAttrs20170518(models.Model):
    idx_b_hyqx_20170518_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170518_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170518'
class WeatherAttrs20170519(models.Model):
    idx_b_hyqx_20170519_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170519_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170519'
class WeatherAttrs20170520(models.Model):
    idx_b_hyqx_20170520_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170520_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170520'
class WeatherAttrs20170521(models.Model):
    idx_b_hyqx_20170521_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170521_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170521'
class WeatherAttrs20170522(models.Model):
    idx_b_hyqx_20170522_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170522_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170522'
class WeatherAttrs20170523(models.Model):
    idx_b_hyqx_20170523_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170523_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170523'
class WeatherAttrs20170524(models.Model):
    idx_b_hyqx_20170524_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170524_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170524'
class WeatherAttrs20170525(models.Model):
    idx_b_hyqx_20170525_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170525_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170525'
class WeatherAttrs20170526(models.Model):
    idx_b_hyqx_20170526_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170526_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170526'
class WeatherAttrs20170527(models.Model):
    idx_b_hyqx_20170527_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170527_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170527'
class WeatherAttrs20170528(models.Model):
    idx_b_hyqx_20170528_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170528_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170528'
class WeatherAttrs20170529(models.Model):
    idx_b_hyqx_20170529_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170529_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170529'
class WeatherAttrs20170530(models.Model):
    idx_b_hyqx_20170530_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170530_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170530'
class WeatherAttrs20170531(models.Model):
    idx_b_hyqx_20170531_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170531_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170531'
class WeatherAttrs20170601(models.Model):
    idx_b_hyqx_20170601_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170601_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170601'
class WeatherAttrs20170602(models.Model):
    idx_b_hyqx_20170602_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170602_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170602'
class WeatherAttrs20170603(models.Model):
    idx_b_hyqx_20170603_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170603_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170603'
class WeatherAttrs20170604(models.Model):
    idx_b_hyqx_20170604_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170604_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170604'
class WeatherAttrs20170605(models.Model):
    idx_b_hyqx_20170605_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170605_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170605'
class WeatherAttrs20170606(models.Model):
    idx_b_hyqx_20170606_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170606_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170606'
class WeatherAttrs20170607(models.Model):
    idx_b_hyqx_20170607_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170607_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170607'
class WeatherAttrs20170608(models.Model):
    idx_b_hyqx_20170608_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170608_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170608'
class WeatherAttrs20170609(models.Model):
    idx_b_hyqx_20170609_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170609_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170609'
class WeatherAttrs20170610(models.Model):
    idx_b_hyqx_20170610_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170610_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170610'
class WeatherAttrs20170611(models.Model):
    idx_b_hyqx_20170611_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170611_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170611'
class WeatherAttrs20170612(models.Model):
    idx_b_hyqx_20170612_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170612_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170612'
class WeatherAttrs20170613(models.Model):
    idx_b_hyqx_20170613_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170613_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170613'
class WeatherAttrs20170614(models.Model):
    idx_b_hyqx_20170614_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170614_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170614'
class WeatherAttrs20170615(models.Model):
    idx_b_hyqx_20170615_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170615_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170615'
class WeatherAttrs20170616(models.Model):
    idx_b_hyqx_20170616_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170616_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170616'
class WeatherAttrs20170617(models.Model):
    idx_b_hyqx_20170617_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170617_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170617'
class WeatherAttrs20170618(models.Model):
    idx_b_hyqx_20170618_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170618_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170618'
class WeatherAttrs20170619(models.Model):
    idx_b_hyqx_20170619_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170619_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170619'
class WeatherAttrs20170620(models.Model):
    idx_b_hyqx_20170620_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170620_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170620'
class WeatherAttrs20170621(models.Model):
    idx_b_hyqx_20170621_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170621_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170621'
class WeatherAttrs20170622(models.Model):
    idx_b_hyqx_20170622_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170622_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170622'
class WeatherAttrs20170623(models.Model):
    idx_b_hyqx_20170623_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170623_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170623'
class WeatherAttrs20170624(models.Model):
    idx_b_hyqx_20170624_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170624_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170624'
class WeatherAttrs20170625(models.Model):
    idx_b_hyqx_20170625_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170625_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170625'
class WeatherAttrs20170626(models.Model):
    idx_b_hyqx_20170626_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170626_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170626'
class WeatherAttrs20170627(models.Model):
    idx_b_hyqx_20170627_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170627_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170627'
class WeatherAttrs20170628(models.Model):
    idx_b_hyqx_20170628_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170628_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170628'
class WeatherAttrs20170629(models.Model):
    idx_b_hyqx_20170629_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170629_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170629'
class WeatherAttrs20170630(models.Model):
    idx_b_hyqx_20170630_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170630_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170630'
class WeatherAttrs20170701(models.Model):
    idx_b_hyqx_20170701_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170701_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170701'
class WeatherAttrs20170702(models.Model):
    idx_b_hyqx_20170702_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170702_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170702'
class WeatherAttrs20170703(models.Model):
    idx_b_hyqx_20170703_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170703_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170703'
class WeatherAttrs20170704(models.Model):
    idx_b_hyqx_20170704_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170704_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170704'
class WeatherAttrs20170705(models.Model):
    idx_b_hyqx_20170705_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170705_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170705'
class WeatherAttrs20170706(models.Model):
    idx_b_hyqx_20170706_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170706_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170706'
class WeatherAttrs20170707(models.Model):
    idx_b_hyqx_20170707_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170707_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170707'
class WeatherAttrs20170708(models.Model):
    idx_b_hyqx_20170708_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170708_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170708'
class WeatherAttrs20170709(models.Model):
    idx_b_hyqx_20170709_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170709_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170709'
class WeatherAttrs20170710(models.Model):
    idx_b_hyqx_20170710_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170710_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170710'
class WeatherAttrs20170711(models.Model):
    idx_b_hyqx_20170711_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170711_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170711'
class WeatherAttrs20170712(models.Model):
    idx_b_hyqx_20170712_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170712_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170712'
class WeatherAttrs20170713(models.Model):
    idx_b_hyqx_20170713_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170713_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170713'
class WeatherAttrs20170714(models.Model):
    idx_b_hyqx_20170714_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170714_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170714'
class WeatherAttrs20170715(models.Model):
    idx_b_hyqx_20170715_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170715_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170715'
class WeatherAttrs20170716(models.Model):
    idx_b_hyqx_20170716_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170716_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170716'
class WeatherAttrs20170717(models.Model):
    idx_b_hyqx_20170717_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170717_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170717'
class WeatherAttrs20170718(models.Model):
    idx_b_hyqx_20170718_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170718_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170718'
class WeatherAttrs20170719(models.Model):
    idx_b_hyqx_20170719_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170719_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170719'
class WeatherAttrs20170720(models.Model):
    idx_b_hyqx_20170720_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170720_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170720'
class WeatherAttrs20170721(models.Model):
    idx_b_hyqx_20170721_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170721_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170721'
class WeatherAttrs20170722(models.Model):
    idx_b_hyqx_20170722_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170722_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170722'
class WeatherAttrs20170723(models.Model):
    idx_b_hyqx_20170723_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170723_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170723'
class WeatherAttrs20170724(models.Model):
    idx_b_hyqx_20170724_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170724_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170724'
class WeatherAttrs20170725(models.Model):
    idx_b_hyqx_20170725_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170725_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170725'
class WeatherAttrs20170726(models.Model):
    idx_b_hyqx_20170726_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170726_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170726'
class WeatherAttrs20170727(models.Model):
    idx_b_hyqx_20170727_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170727_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170727'
class WeatherAttrs20170728(models.Model):
    idx_b_hyqx_20170728_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170728_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170728'
class WeatherAttrs20170729(models.Model):
    idx_b_hyqx_20170729_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170729_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170729'
class WeatherAttrs20170730(models.Model):
    idx_b_hyqx_20170730_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170730_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170730'
class WeatherAttrs20170731(models.Model):
    idx_b_hyqx_20170731_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170731_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170731'
class WeatherAttrs20170801(models.Model):
    idx_b_hyqx_20170801_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170801_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170801'
class WeatherAttrs20170802(models.Model):
    idx_b_hyqx_20170802_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170802_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170802'
class WeatherAttrs20170803(models.Model):
    idx_b_hyqx_20170803_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170803_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170803'
class WeatherAttrs20170804(models.Model):
    idx_b_hyqx_20170804_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170804_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170804'
class WeatherAttrs20170805(models.Model):
    idx_b_hyqx_20170805_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170805_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170805'
class WeatherAttrs20170806(models.Model):
    idx_b_hyqx_20170806_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170806_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170806'
class WeatherAttrs20170807(models.Model):
    idx_b_hyqx_20170807_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170807_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170807'
class WeatherAttrs20170808(models.Model):
    idx_b_hyqx_20170808_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170808_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170808'
class WeatherAttrs20170809(models.Model):
    idx_b_hyqx_20170809_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170809_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170809'
class WeatherAttrs20170810(models.Model):
    idx_b_hyqx_20170810_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170810_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170810'
class WeatherAttrs20170811(models.Model):
    idx_b_hyqx_20170811_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170811_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170811'
class WeatherAttrs20170812(models.Model):
    idx_b_hyqx_20170812_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170812_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170812'
class WeatherAttrs20170813(models.Model):
    idx_b_hyqx_20170813_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170813_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170813'
class WeatherAttrs20170814(models.Model):
    idx_b_hyqx_20170814_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170814_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170814'
class WeatherAttrs20170815(models.Model):
    idx_b_hyqx_20170815_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170815_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170815'
class WeatherAttrs20170816(models.Model):
    idx_b_hyqx_20170816_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170816_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170816'
class WeatherAttrs20170817(models.Model):
    idx_b_hyqx_20170817_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170817_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170817'
class WeatherAttrs20170818(models.Model):
    idx_b_hyqx_20170818_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170818_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170818'
class WeatherAttrs20170819(models.Model):
    idx_b_hyqx_20170819_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170819_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170819'
class WeatherAttrs20170820(models.Model):
    idx_b_hyqx_20170820_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170820_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170820'
class WeatherAttrs20170821(models.Model):
    idx_b_hyqx_20170821_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170821_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170821'
class WeatherAttrs20170822(models.Model):
    idx_b_hyqx_20170822_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170822_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170822'
class WeatherAttrs20170823(models.Model):
    idx_b_hyqx_20170823_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170823_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170823'
class WeatherAttrs20170824(models.Model):
    idx_b_hyqx_20170824_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170824_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170824'
class WeatherAttrs20170825(models.Model):
    idx_b_hyqx_20170825_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170825_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170825'
class WeatherAttrs20170826(models.Model):
    idx_b_hyqx_20170826_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170826_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170826'
class WeatherAttrs20170827(models.Model):
    idx_b_hyqx_20170827_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170827_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170827'
class WeatherAttrs20170828(models.Model):
    idx_b_hyqx_20170828_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170828_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170828'
class WeatherAttrs20170829(models.Model):
    idx_b_hyqx_20170829_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170829_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170829'
class WeatherAttrs20170830(models.Model):
    idx_b_hyqx_20170830_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170830_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170830'
class WeatherAttrs20170831(models.Model):
    idx_b_hyqx_20170831_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170831_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170831'
class WeatherAttrs20170901(models.Model):
    idx_b_hyqx_20170901_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170901_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170901'
class WeatherAttrs20170902(models.Model):
    idx_b_hyqx_20170902_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170902_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170902'
class WeatherAttrs20170903(models.Model):
    idx_b_hyqx_20170903_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170903_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170903'
class WeatherAttrs20170904(models.Model):
    idx_b_hyqx_20170904_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170904_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170904'
class WeatherAttrs20170905(models.Model):
    idx_b_hyqx_20170905_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170905_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170905'
class WeatherAttrs20170906(models.Model):
    idx_b_hyqx_20170906_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170906_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170906'
class WeatherAttrs20170907(models.Model):
    idx_b_hyqx_20170907_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170907_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170907'
class WeatherAttrs20170908(models.Model):
    idx_b_hyqx_20170908_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170908_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170908'
class WeatherAttrs20170909(models.Model):
    idx_b_hyqx_20170909_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170909_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170909'
class WeatherAttrs20170910(models.Model):
    idx_b_hyqx_20170910_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170910_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170910'
class WeatherAttrs20170911(models.Model):
    idx_b_hyqx_20170911_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170911_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170911'
class WeatherAttrs20170912(models.Model):
    idx_b_hyqx_20170912_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170912_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170912'
class WeatherAttrs20170913(models.Model):
    idx_b_hyqx_20170913_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170913_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170913'
class WeatherAttrs20170914(models.Model):
    idx_b_hyqx_20170914_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170914_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170914'
class WeatherAttrs20170915(models.Model):
    idx_b_hyqx_20170915_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170915_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170915'
class WeatherAttrs20170916(models.Model):
    idx_b_hyqx_20170916_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170916_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170916'
class WeatherAttrs20170917(models.Model):
    idx_b_hyqx_20170917_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170917_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170917'
class WeatherAttrs20170918(models.Model):
    idx_b_hyqx_20170918_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170918_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170918'
class WeatherAttrs20170919(models.Model):
    idx_b_hyqx_20170919_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170919_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170919'
class WeatherAttrs20170920(models.Model):
    idx_b_hyqx_20170920_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170920_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170920'
class WeatherAttrs20170921(models.Model):
    idx_b_hyqx_20170921_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170921_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170921'
class WeatherAttrs20170922(models.Model):
    idx_b_hyqx_20170922_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170922_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170922'
class WeatherAttrs20170923(models.Model):
    idx_b_hyqx_20170923_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170923_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170923'
class WeatherAttrs20170924(models.Model):
    idx_b_hyqx_20170924_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170924_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170924'
class WeatherAttrs20170925(models.Model):
    idx_b_hyqx_20170925_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170925_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170925'
class WeatherAttrs20170926(models.Model):
    idx_b_hyqx_20170926_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170926_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170926'
class WeatherAttrs20170927(models.Model):
    idx_b_hyqx_20170927_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170927_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170927'
class WeatherAttrs20170928(models.Model):
    idx_b_hyqx_20170928_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170928_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170928'
class WeatherAttrs20170929(models.Model):
    idx_b_hyqx_20170929_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170929_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170929'
class WeatherAttrs20170930(models.Model):
    idx_b_hyqx_20170930_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20170930_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20170930'
class WeatherAttrs20171001(models.Model):
    idx_b_hyqx_20171001_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171001_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171001'
class WeatherAttrs20171002(models.Model):
    idx_b_hyqx_20171002_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171002_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171002'
class WeatherAttrs20171003(models.Model):
    idx_b_hyqx_20171003_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171003_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171003'
class WeatherAttrs20171004(models.Model):
    idx_b_hyqx_20171004_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171004_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171004'
class WeatherAttrs20171005(models.Model):
    idx_b_hyqx_20171005_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171005_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171005'
class WeatherAttrs20171006(models.Model):
    idx_b_hyqx_20171006_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171006_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171006'
class WeatherAttrs20171007(models.Model):
    idx_b_hyqx_20171007_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171007_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171007'
class WeatherAttrs20171008(models.Model):
    idx_b_hyqx_20171008_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171008_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171008'
class WeatherAttrs20171009(models.Model):
    idx_b_hyqx_20171009_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171009_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171009'
class WeatherAttrs20171010(models.Model):
    idx_b_hyqx_20171010_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171010_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171010'
class WeatherAttrs20171011(models.Model):
    idx_b_hyqx_20171011_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171011_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171011'
class WeatherAttrs20171012(models.Model):
    idx_b_hyqx_20171012_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171012_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171012'
class WeatherAttrs20171013(models.Model):
    idx_b_hyqx_20171013_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171013_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171013'
class WeatherAttrs20171014(models.Model):
    idx_b_hyqx_20171014_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171014_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171014'
class WeatherAttrs20171015(models.Model):
    idx_b_hyqx_20171015_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171015_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171015'
class WeatherAttrs20171016(models.Model):
    idx_b_hyqx_20171016_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171016_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171016'
class WeatherAttrs20171017(models.Model):
    idx_b_hyqx_20171017_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171017_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171017'
class WeatherAttrs20171018(models.Model):
    idx_b_hyqx_20171018_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171018_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171018'
class WeatherAttrs20171019(models.Model):
    idx_b_hyqx_20171019_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171019_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171019'
class WeatherAttrs20171020(models.Model):
    idx_b_hyqx_20171020_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171020_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171020'
class WeatherAttrs20171021(models.Model):
    idx_b_hyqx_20171021_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171021_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171021'
class WeatherAttrs20171022(models.Model):
    idx_b_hyqx_20171022_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171022_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171022'
class WeatherAttrs20171023(models.Model):
    idx_b_hyqx_20171023_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171023_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171023'
class WeatherAttrs20171024(models.Model):
    idx_b_hyqx_20171024_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171024_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171024'
class WeatherAttrs20171025(models.Model):
    idx_b_hyqx_20171025_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171025_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171025'
class WeatherAttrs20171026(models.Model):
    idx_b_hyqx_20171026_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171026_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171026'
class WeatherAttrs20171027(models.Model):
    idx_b_hyqx_20171027_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171027_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171027'
class WeatherAttrs20171028(models.Model):
    idx_b_hyqx_20171028_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171028_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171028'
class WeatherAttrs20171029(models.Model):
    idx_b_hyqx_20171029_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171029_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171029'
class WeatherAttrs20171030(models.Model):
    idx_b_hyqx_20171030_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171030_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171030'
class WeatherAttrs20171031(models.Model):
    idx_b_hyqx_20171031_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171031_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171031'
class WeatherAttrs20171101(models.Model):
    idx_b_hyqx_20171101_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171101_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171101'
class WeatherAttrs20171102(models.Model):
    idx_b_hyqx_20171102_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171102_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171102'
class WeatherAttrs20171103(models.Model):
    idx_b_hyqx_20171103_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171103_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171103'
class WeatherAttrs20171104(models.Model):
    idx_b_hyqx_20171104_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171104_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171104'
class WeatherAttrs20171105(models.Model):
    idx_b_hyqx_20171105_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171105_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171105'
class WeatherAttrs20171106(models.Model):
    idx_b_hyqx_20171106_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171106_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171106'
class WeatherAttrs20171107(models.Model):
    idx_b_hyqx_20171107_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171107_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171107'
class WeatherAttrs20171108(models.Model):
    idx_b_hyqx_20171108_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171108_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171108'
class WeatherAttrs20171109(models.Model):
    idx_b_hyqx_20171109_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171109_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171109'
class WeatherAttrs20171110(models.Model):
    idx_b_hyqx_20171110_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171110_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171110'
class WeatherAttrs20171111(models.Model):
    idx_b_hyqx_20171111_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171111_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171111'
class WeatherAttrs20171112(models.Model):
    idx_b_hyqx_20171112_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171112_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171112'
class WeatherAttrs20171113(models.Model):
    idx_b_hyqx_20171113_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171113_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171113'
class WeatherAttrs20171114(models.Model):
    idx_b_hyqx_20171114_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171114_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171114'
class WeatherAttrs20171115(models.Model):
    idx_b_hyqx_20171115_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171115_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171115'
class WeatherAttrs20171116(models.Model):
    idx_b_hyqx_20171116_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171116_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171116'
class WeatherAttrs20171117(models.Model):
    idx_b_hyqx_20171117_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171117_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171117'
class WeatherAttrs20171118(models.Model):
    idx_b_hyqx_20171118_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171118_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171118'
class WeatherAttrs20171119(models.Model):
    idx_b_hyqx_20171119_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171119_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171119'
class WeatherAttrs20171120(models.Model):
    idx_b_hyqx_20171120_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171120_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171120'
class WeatherAttrs20171121(models.Model):
    idx_b_hyqx_20171121_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171121_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171121'
class WeatherAttrs20171122(models.Model):
    idx_b_hyqx_20171122_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171122_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171122'
class WeatherAttrs20171123(models.Model):
    idx_b_hyqx_20171123_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171123_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171123'
class WeatherAttrs20171124(models.Model):
    idx_b_hyqx_20171124_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171124_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171124'
class WeatherAttrs20171125(models.Model):
    idx_b_hyqx_20171125_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171125_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171125'
class WeatherAttrs20171126(models.Model):
    idx_b_hyqx_20171126_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171126_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171126'
class WeatherAttrs20171127(models.Model):
    idx_b_hyqx_20171127_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171127_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171127'
class WeatherAttrs20171128(models.Model):
    idx_b_hyqx_20171128_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171128_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171128'
class WeatherAttrs20171129(models.Model):
    idx_b_hyqx_20171129_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171129_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171129'
class WeatherAttrs20171130(models.Model):
    idx_b_hyqx_20171130_pk = models.IntegerField(primary_key=True)
    f_dl_jd = models.DecimalField(max_digits=5, decimal_places=2);
    f_dl_wd = models.DecimalField(max_digits=5, decimal_places=2);
    f_it_jnd = models.IntegerField();  # 5 或者10
    f_it_sj = models.IntegerField();  #精确到年月日小时
    f_dl_wnd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #温度
    f_dl_qy = models.DecimalField(max_digits=10, decimal_places=2, null=True);    #气压
    f_dl_jyl = models.DecimalField(max_digits=10, decimal_places=2, null=True); #降雨量
    f_dl_fs = models.DecimalField(max_digits=5, decimal_places=2, null=True);    #风速
    f_dl_fx = models.DecimalField(max_digits=10, decimal_places=2, null=True); #风向
    f_it_njd = models.IntegerField(null=True); #能见度
    f_dl_hl = models.DecimalField(max_digits=5, decimal_places=2, null=True);   #海浪
    f_dl_ylgd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流高度
    f_dl_ylzq = models.DecimalField(max_digits=5, decimal_places=2, null=True); #涌流周期
    f_dl_ylfx = models.DecimalField(max_digits=10, decimal_places=2, null=True); # 涌流方向
    f_dl_hlsw = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流水位
    f_dl_hlwd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #海流温度
    f_dl_xl = models.DecimalField(max_digits=5, decimal_places=2, null=True); #x方向的流
    f_dl_yl =  models.DecimalField(max_digits=5, decimal_places=2, null=True); #y方向的流
    f_dl_zl = models.DecimalField(max_digits=10, decimal_places=4, null=True); #垂直运动
    f_dl_xdsd = models.DecimalField(max_digits=5, decimal_places=2, null=True); #相对湿度
    idx_b_hyqx_20171130_uk = models.DecimalField(max_digits=12, decimal_places=0, unique=True); #number，经纬度+精度+时间的hash值
    class Meta:
        db_table = 'b_hyqx_20171130'