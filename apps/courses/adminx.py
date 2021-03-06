import xadmin
from .models import Course, Lesson, Video, CourseResource, BannerCourse

__author__ = 'duxi'
__date__ = '2017-8-31 22:57'


class LessonInline(object):
    model = Lesson
    extra = 0


class CourseResourseInline(object):
    model = CourseResource
    extra = 0


class CourseAdmin(object):
    list_display = ['name','course_org', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image',
                    'click_nums', 'add_time', 'get_zj_nums']
    search_fields = ['name', 'course_org','desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums']
    list_filter = ['name','course_org', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image',
                   'click_nums', 'add_time']
    ordering = ('-click_nums',)
    readonly_fields = ['click_nums','students'] #只读
    list_editable = ['degree'] #可直接在xadmin桌面修改
    exclude = ['fav_nums'] #不在修改页面显示
    inlines = [LessonInline, CourseResourseInline]
    refresh_times = [3,5,10] #页面自动刷新时间
    style_fields = {"detail":"ueditor"}

    def queryset(self):
        qs = super(CourseAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs

    def save_models(self):
        #在保存课程的时候统计课程机构的课程数
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(course_org=course_org).all().count()
            course_org.save()


class BannerCourseAdmin(object):
    list_display = ['name','course_org', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image',
                    'click_nums', 'add_time', 'get_zj_nums']
    search_fields = ['name', 'course_org','desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums']
    list_filter = ['name','course_org', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image',
                   'click_nums', 'add_time']
    ordering = ('-click_nums',)
    readonly_fields = ['click_nums','students'] #只读
    list_editable = ['degree']#可直接在xadmin桌面修改
    exclude = ['fav_nums'] #不在修改页面显示
    inlines = [LessonInline, CourseResourseInline]

    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time', 'get_lesson_videos_nums']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson__name', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']

xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
