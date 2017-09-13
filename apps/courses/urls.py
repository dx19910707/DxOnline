__author__ = 'duxi'
__date__ = '2017-9-6 14:29'

from django.conf.urls import url, include

from .views import CourseListView, CourseDetailView, CourseVideoView, CourseCommentView, AddcommentView, VideoPlayView

urlpatterns = [
    # 课程列表页
    url(r'^list/$', CourseListView.as_view(), name='course-list'),
    # 课程详情页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='course-detail'),
    # 章节信息页
    url(r'^info/(?P<course_id>\d+)/$', CourseVideoView.as_view(), name='course-video'),
    # 课程评论页面
    url(r'^comments/(?P<course_id>\d+)/$', CourseCommentView.as_view(), name='course-comments'),
    # 添加课程评论
    url(r'^add_comment/$', AddcommentView.as_view(), name='add_comment'),
    # 添加课程评论
    url(r'^video/(?P<video_id>\d+)/$', VideoPlayView.as_view(), name='video_play'),
]
