# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from datetime import datetime
from django.db import models

from users.models import UserProfile
from courses.models import Course
# Create your models here.


class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"姓名", default="")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u"手机", default="")
    course_name = models.CharField(max_length=50, verbose_name=u"课程名", default="")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户资源"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseComments(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    course = models.ForeignKey(Course, verbose_name=u"课程", default="")
    comments = models.CharField(max_length=200, verbose_name=u"评论", default="")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程评论"
        verbose_name_plural = verbose_name

    def __unicode__(self):
         return self.user.username


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户名")
    fav_id = models.IntegerField(default=0, verbose_name=u"数据ID")
    fav_type = models.IntegerField(choices=((1, "课程"),(2, "课程机构"),(3, "讲师")), default=1, verbose_name=u"收藏类型")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name

    def __unicode__(self):
         return self.user.username


class UserMessage(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    message = models.CharField(max_length=500, verbose_name=u"消息内容", default="")
    has_read = models.BooleanField(default=False, verbose_name=u"是否已读")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"发送时间")

    class Meta:
        verbose_name = u"用户消息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
         return self.user.username


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    course = models.ForeignKey(Course, verbose_name=u"课程", default="")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"学习时间")

    class Meta:
        verbose_name = u"用户课程"
        verbose_name_plural = verbose_name

    def __unicode__(self):
         return self.user.username

