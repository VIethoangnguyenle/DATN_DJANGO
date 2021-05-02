from django.db import models

# Create your models here.
from django.db import models
import string,random
from django.utils import timezone
# Create your models here.
class control(models.Model):
    SIZE_A4 = '21'
    SIZE_A5 = '8'
    SIZE = [
        (SIZE_A4,'Size A4'),
        (SIZE_A5,'Size A5'),
    ]
    START = '1'
    STOP = '0'
    STATE = [
        (START,'Start'),
        (STOP,'Stop'),
    ]
    size = models.CharField(default=SIZE_A4,max_length=20, choices=SIZE)
    speed = models.CharField(max_length=5,default=0)
    state = models.CharField(max_length=2, choices=STATE,default=STOP)

class data_line(models.Model):
    data = models.DecimalField(max_digits=7,decimal_places=2)

class dut_net(models.Model):
    fail = models.CharField(max_length=10,default=0)

class data_avg(models.Model):
    avg_line = models.DecimalField(max_digits=7,decimal_places=2)

class pen_show(models.Model):
    DAT = '1'
    KHONG_DAT = '0'
    STATE=[
        (DAT,'Bút đạt chuẩn'),
        (KHONG_DAT,'Bút Không đạt chuẩn'),
    ]
    avg_pen = models.DecimalField(max_digits=7,decimal_places=2)
    dotted_lenght = models.DecimalField(max_digits=5,decimal_places=2)
    distance = models.DecimalField(max_digits=10,decimal_places=2)
    state = models.CharField(max_length=10,choices=STATE)
    time = models.DateField(default=timezone.now)
    
    @property
    def get_all_pen_error(self):
        return pen_show.objects.filter(state='0')

    @property
    def get_all_pen_good(self):
        return pen_show.objects.filter(state='1')

    @property
    def get_result_in_day(self):
        return pen_show.objects.filter(time=timezone.now)
    
    def __str__(self):
        return "{} {} {} {} {}".format(self.avg_pen,self.dotted_lenght,self.distance,self.state,self.time)

class test(models.Model):
    START = '1'
    STOP = '0'
    STATE = [
        (START,'Start'),
        (STOP,'Stop'),
    ]
    sizepaper = models.CharField(max_length=20,blank=False);
    speed = models.CharField(max_length=20,blank=False)
    error = models.CharField(max_length=20,blank=False)
    state = models.CharField(max_length=2, choices=STATE,default=STOP)

    def __str__(self):
        return "Size: {},speed: {},error:{}".format(self.sizepaper,self.speed,self.error)

class dut_net_length(models.Model):
    length = models.DecimalField(max_digits=7,decimal_places=2)

class threshold(models.Model):
    dut_net_error = models.IntegerField()
    mong_net_error = models.IntegerField()
    high_width = models.DecimalField(max_digits=8,decimal_places=3)
    low_width = models.DecimalField(max_digits=8,decimal_places=3)
    length = models.IntegerField()

class filterByDay(models.Model):
    date = models.CharField(max_length=100)
    
