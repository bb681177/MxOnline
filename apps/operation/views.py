# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.base import View
from .models import Course
# Create your views here.


class CourseListView(View):
    """
    课程例表页
    """
    def get(self, request):
        all_course = Course.objects.all().order_by("-add_time")
        hot_course = Course.objects.all().order_by("-click_nums")[:3]

        # 课程排序
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_course = all_course.order_by("-students")
            elif sort == "hot":
                all_course = all_course.order_by("-click_nums")

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_course, 9, request=request)
        course = p.page(page)
        course_nums = all_course.count()

        return render(request, "course-list.html", {
            "all_courses": course,
            "hot_course": hot_course,
            "course_nums": course_nums,
            "sort": sort
        })


class CourseDetaileView(View):
    """
    课程详情页
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        return render(request, "course-detail.html", {
            "course": course
        })




