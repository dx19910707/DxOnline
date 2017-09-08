__author__ = 'duxi'
__date__ = '2017-9-6 14:29'

from django.conf.urls import url, include

from .views import CourseListView, CourseDetailView, CourseVideoView


urlpatterns = [
    #课程列表页
    url(r'^list/$', CourseListView.as_view(), name='course-list'),
    #课程详情页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='course-detail'),
    #章节信息页
    url(r'^video/(?P<course_id>\d+)/$', CourseVideoView.as_view(), name='course-video'),
]