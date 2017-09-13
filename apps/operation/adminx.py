import xadmin
from .models import UserAsk, CourseComments, UserFavorite, UserMassage, UserCourse

__author__ = 'duxi'
__date__ = '2017-8-31 23:57'


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course', ]
    list_filter = ['user', 'course', 'add_time']


class UserMassageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']


class CourseCommentsAdmin(object):
    list_display = ['user', 'course', 'comments', 'add_time']
    search_fields = ['user', 'course', 'comments']
    list_filter = ['user__username', 'course__name', 'comments', 'add_time']


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user__username', 'fav_id', 'fav_type']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMassage, UserMassageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
