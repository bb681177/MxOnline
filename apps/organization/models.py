# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from datetime import datetime

from django.db import models

# Create your models here.


class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"城市名")
    desc = models.TextField(max_length=200, verbose_name=u"城市描述")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"机构名称")
    desc = models.TextField(max_length=300, verbose_name=u"机构描述")
    category = models.CharField(max_length=20, choices=(('pxjg', "培训机构"), ('gr', "个人"), ('gx', "高校")), default=1, verbose_name=u"培训机构")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    course_nums = models.IntegerField(default=0, verbose_name=u"课程数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    image = models.ImageField(max_length=100, upload_to="org/%Y/%m",  verbose_name=u"封面图")
    address = models.CharField(max_length=100, verbose_name=u"机构地址")
    city = models.ForeignKey(CityDict, verbose_name=u"所在城市")

    class Meta:
        verbose_name = u"课程机构"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_teacher(self):
        # 获取课程机构的教师数
        return self.teacher_set.all().count()

    def get_course(self):
        # 获取课程机构的课程数
        return self.course_set.all().count()


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg,verbose_name=u"所属机构" )
    name = models.CharField(max_length=50, verbose_name=u"教师名")
    image = models.ImageField(max_length=100, default='', upload_to="teacher/%Y/%m",  verbose_name=u"头像")
    work_years = models.IntegerField(default=0, verbose_name=u"工作年限")
    work_company = models.CharField(max_length=50, verbose_name=u"就职公司")
    work_position = models.CharField(max_length=50, verbose_name=u"公司职位", null=True)
    points = models.CharField(max_length=50, verbose_name=u"教学特点")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"教师"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
