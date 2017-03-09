# _*_ encoding:utf-8 _*_
"""mx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.static import serve
import xadmin

from users.views import loginView, RegisterView, AciveUserView, ForgetWodView, ResetView, ModifyPwdView
from organization.views import OrgView
from MxOnline.settings import MEDIA_ROOT
urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    url('^$', TemplateView.as_view(template_name="index.html"),name="index"),
    url('^login/$', loginView.as_view(), name="login"),
    url('^register/$', RegisterView.as_view(), name="register"),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', AciveUserView.as_view(), name="user_acive"),
    url(r'^forget/$', ForgetWodView.as_view(), name="forget_pwd"),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name="rest_pwd"),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),
    # 机构配置
    url(r'^org/', include('organization.urls', namespace="org")),
    # 课程相关配置
    url(r'^course/', include('courses.urls', namespace="course")),

    # 配置上传文件的处理函数
    url(r'^media/(?P<path>.*)/$', serve,{"document_root": MEDIA_ROOT}),
]
