# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"呢称", default=u"")
    birday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    gender = models.CharField(max_length=6,choices=(("male",u"男"),("female","女")), default="male", verbose_name=u"性别")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u"手机")
    address = models.CharField(max_length=100, default=u"联系地址", verbose_name=u"联系地址")
    image = models.ImageField(upload_to="image/%Y/%m",default=u"image/default",verbose_name=u"头像" )

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural= verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50,verbose_name=u"邮箱")
    send_type = models.CharField(choices=(("register","注册"),("forget",u"找回密码")), max_length=10, verbose_name=u"验证码类型" )
    send_time = models.DateTimeField(default=datetime.now,verbose_name=u"发送时间")

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
         return self.code


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"图片名")
    image = models.ImageField(upload_to="image/%Y/%m",  verbose_name=u"轮播图", max_length=100)
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title