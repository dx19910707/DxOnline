__author__ = 'duxi'
__date__ = '2017-9-6 14:29'

from django.conf.urls import url, include

from .views import CourseListView, CourseDetailView


urlpatterns = [
    url(r'^list/$', CourseListView.as_view(), name='course-list'),
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='course-detail'),
]