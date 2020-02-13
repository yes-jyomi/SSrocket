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
        return self.user_id


class History(models.Model):
    history_num = models.AutoField(db_column='history_num',primary_key=True)
    history_place = models.CharField(db_column='history_place',max_length=200)
    user_id = models.CharField(db_column='user_id',max_length=200)
    r_btime = models.DateTimeField(db_column='r_btime')
    btime = models.DateTimeField(db_column='btime')
    r_rtime = models.DateTimeField(db_column='r_rtime')
    rtime = models.DateTimeField(db_column='rtime')

    class Meta:
        managed = False
        db_table = 'history'

    def publish(self):
        self.save()

    def __str__(self):
        return self.user_id

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
        return self.user_id
