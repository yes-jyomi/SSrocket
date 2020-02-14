from django.conf import settings
from django.db import models
from django.utils import timezone


class User(models.Model):
    id = models.CharField(db_column='id',primary_key=True,max_length=200)
    name = models.CharField(db_column='name',max_length=200)
    pwd = models.CharField(db_column='pwd',max_length=200)
    info = models.IntegerField(db_column='info')

    class Meta:
        managed = False
        db_table = 'user'

    def publish(self):
        self.save()

    def __str__(self):
        return self.id


class History(models.Model):
    history_num = models.AutoField(db_column='history_num',primary_key=True)
    company_num = models.IntegerField(db_column='company_num')
    member_id = models.CharField(db_column='member_id',max_length=200)
    r_btime = models.DateTimeField(db_column='r_btime')
    btime = models.DateTimeField(db_column='btime')
    r_rtime = models.DateTimeField(db_column='r_rtime')
    rtime = models.DateTimeField(db_column='rtime')
    reserved_At = models.DateTimeField(db_column='reserved_At')

    class Meta:
        managed = False
        db_table = 'history'

    def publish(self):
        self.save()

    def __str__(self):
        return self.member_id

class Course(models.Model):
    c_num = models.AutoField(db_column='c_num',primary_key=True)
    c_name = models.CharField(db_column='c_name',max_length=200)
    c_info = models.TextField(db_column='c_info',max_length=1000)
    c_loc = models.CharField(db_column='c_loc',max_length=200)
    c_theme = models.CharField(db_column='c_theme',max_length=200)
    c_time = models.IntegerField(db_column='c_time')

    class Meta:
        managed = False
        db_table = 'course'

    def publish(self):
        self.save()

    def __str__(self):
        return self.c_name


class Company(models.Model):
    company_num = models.AutoField(db_column='company_num',primary_key=True)
    member_name = models.CharField(db_column='member_name',max_length=200)
    company_addr = models.CharField(db_column='company_addr',max_length=200)
    company_phone = models.CharField(db_column='company_phone',max_length=200)
    bicycle_num = models.IntegerField(db_column='bicycle_num')
    member_id = models.CharField(db_column='member_id',max_length=200)
    s_business = models.DateTimeField(db_column='s_business')
    e_business = models.DateTimeField(db_column='e_business')

    class Meta:
        managed = False
        db_table = 'company'

    def publish(self):
        self.save()

    def __str__(self):
        return self.member_name

