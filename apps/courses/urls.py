# _*_ encoding:utf-8 _*_
__author__ = 'duanlian'
__date__ = '2017/3/7 21:03'

from django.conf.urls import url,include
from .views import CourseListView, CourseDetaileView, CourseInfoView, CommentsView,AddCommentsView

urlpatterns = [
    # 课程列表
    url(r'^list/$', CourseListView.as_view(), name="course_list"),
    # 课程详情
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetaileView.as_view(), name="course_detail"),
    # 课程章节
    url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name="course_video"),
    # 课程评论
    url(r'^comment/(?P<course_id>\d+)/$', CommentsView.as_view(), name="course_comment"),
    # 课程评论
    url(r'^add_comment/$', AddCommentsView.as_view(), name="add_comment"),

]