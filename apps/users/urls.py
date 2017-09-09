__author__ = 'duxi'
__date__ = '2017-9-5 14:28'

from django.conf.urls import url
from .views import UserInfoView

urlpatterns = [
    #用户信息
    url(r'^info/$', UserInfoView.as_view(), name='user_info'),
]