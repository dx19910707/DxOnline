__author__ = 'duxi'
__date__ = '2017-9-5 14:28'

from django.conf.urls import url, include

from organization.views import OrgListView, AddUserAskView ,OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView, AddFavView, TeacherListView


urlpatterns = [
    url(r'^list/$', OrgListView.as_view(), name='org-list'),
    url(r'^add_ask$', AddUserAskView.as_view(), name='add_ask'),
    url(r'^home/(?P<org_id>\d+)$', OrgHomeView.as_view(), name='org_home'),
    url(r'^course/(?P<org_id>\d+)$', OrgCourseView.as_view(), name='org_course'),
    url(r'^desc/(?P<org_id>\d+)$', OrgDescView.as_view(), name='org_desc'),
    url(r'^teacher/(?P<org_id>\d+)$', OrgTeacherView.as_view(), name='org_teacher'),
    url(r'^add_fav/$', AddFavView.as_view(), name='add_fav'),
    #配置讲师列表页
    url(r'^teacher/list/$', TeacherListView.as_view(), name='teacher_list'),
]