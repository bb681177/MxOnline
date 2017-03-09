# _*_ encoding:utf-8 _*_
__author__ = 'duanlian'
__date__ = '2017/3/7 21:03'

from django.conf.urls import url,include
from .views import CourseListView, CourseDetaileView

urlpatterns = [
    url(r'^list/$', CourseListView.as_view(), name="course_list"),
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetaileView.as_view(), name="course_detail"),
]