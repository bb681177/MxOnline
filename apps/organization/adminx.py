# _*_ encoding:utf-8 _*_
__author__ = 'duanlian'
__date__ = '2017/2/28 6:44'

import xadmin

from.models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc',  'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'category', 'click_nums', 'address', 'city']
    search_fields = ['name', 'category', 'click_nums', 'address', 'city']
    list_filter = ['name', 'category', 'click_nums', 'address', 'city']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'points', 'click_nums', 'fav_nums', 'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'points', 'click_nums', 'fav_nums']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'points', 'click_nums', 'fav_nums', 'add_time']
    model_icon = 'fa fa-address-book-o'

xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)