# _*_ encoding:utf-8 _*_
__author__ = 'duanlian'
__date__ = '2017/2/28 6:44'
import xadmin
from.models import Course,lesson,Video,CourseResource


class CourseAdmin(object):
    list_display = ['name', 'desc', 'course_org', 'category', 'degree', 'learn_times', 'fav_nums', 'click_nums', 'add_time']
    search_fields = ['name', 'desc', 'course_org', 'category', 'degree', 'learn_times', 'fav_nums', 'click_nums']
    list_filter = ['name', 'desc', 'course_org', 'category', 'degree', 'learn_times', 'fav_nums', 'click_nums', 'add_time']


class lessonAdmin(object):

    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['Course', 'name', 'download', 'add_time']
    search_fields = ['Course', 'name', 'download']
    list_filter = ['Course', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(lesson, lessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)