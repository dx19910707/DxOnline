import xadmin
from xadmin import views

from users.models import EmailVerifyRecord, Banner

__author__ = 'duxi'
__date__ = '2017-8-31 22:19'


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = "杜学后台管理系统"
    site_footer = '杜学在线网'
    menu_style = 'accordion'


class EmailVerifyRecordAdmin(object):
    list_display = ['code','email','send_time','send_type']
    search_fields = ['code','email','send_type']
    list_filter = ['code','email','send_time','send_type']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index','add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index','add_time']

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)