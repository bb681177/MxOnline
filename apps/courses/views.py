# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.base import View
from .models import Course, CourseResource
from operation.models import UserFavorite, CourseComments
from django.http import HttpResponse
from organization.models import Teacher
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

        p = Paginator(all_course, 3, request=request)
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

        #增加课程点击数
        course.click_nums += 1
        course.save()

        # 判断课程与机构收藏
        has_fav_course = False
        has_fav_org = False

        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user,fav_id=course.id, fav_type=1):
                has_fav_course = True

            if UserFavorite.objects.filter(user=request.user,fav_id=course.course_org.id, fav_type=2):
                has_fav_org = True

        tag = course.tag
        if tag:
            relate_coures = Course.objects.filter(tag=tag)[:1]
        return render(request, "course-detail.html", {
            "course": course,
            "relate_coures": relate_coures,
            "has_fav_course": has_fav_course,
            "has_fav_org": has_fav_org
        })

class CourseInfoView(View):
    """
    课程章节信息
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        course_resources = CourseResource.objects.filter(Course_id=int(course.id))
        return render(request, "course-video.html", {
            "course": course,
            "course_resources": course_resources
        })


class CommentsView(View):
    """
    课程评论
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        course_resources = CourseResource.objects.filter(Course_id=int(course.id))
        all_comments = CourseComments.objects.all()
        return render(request, "course-comment.html", {
            "course": course,
            "course_resources": course_resources,
            "all_comments": all_comments
        })

class AddCommentsView(View):
    """
    添加评论
    """
    def post(self, request):
        if not request.user.is_authenticated():
            # 判断用户登录状态
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')

        course_id = request.POST.get("course_id", 0)
        comments = request.POST.get("comments","")
        if course_id > 0 and comments:
            course_comments = CourseComments()
            course = Course.objects.get(id=int(course_id))
            course_comments.course = course
            course_comments.comments = comments
            course_comments.user = request.user
            course_comments.save()
            return HttpResponse('{"status": "success", "添加成功":}}', content_type='application/json')
        else:
            return HttpResponse('{"status": "fail", "添加失败":}}', content_type='application/json')
