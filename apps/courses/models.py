from datetime import datetime

from django.db import models

from organization.models import CourseOrg, Teacher

# Create your models here.


class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, verbose_name='机构名称',null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name='课程名称')
    teacher = models.ForeignKey(Teacher, verbose_name='授课讲师', null=True, blank=True)
    desc = models.CharField(max_length=300, verbose_name='课程描述')
    detail = models.TextField(verbose_name='课程详情')
    is_banner = models.BooleanField(default=0, verbose_name='是否轮播')
    degree = models.CharField(verbose_name='难度', choices=(('cj','初级'),('zj','中级'),('gj','高级')), max_length=2)
    learn_times = models.IntegerField(default=0, verbose_name='学习时长(分钟)')
    students = models.IntegerField(default=0, verbose_name='学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    image = models.ImageField(upload_to='course/%Y/%m', verbose_name='封面图', max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name='点击人数')
    category = models.CharField(max_length=30, verbose_name='课程类别',default='后端开发')
    tag = models.CharField(default='', verbose_name='课程标签', max_length=10)
    you_need_know = models.CharField(default='', verbose_name='课程须知', max_length=300)
    teacher_tell = models.CharField(default='', verbose_name='老师说', max_length=300)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '非轮播课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_zj_nums(self):
        #获取课程章节数
        return self.lesson_set.all().count()

    def get_learn_users(self):
        #获取学习本门课程的用户
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        #获取课程所有章节
        return self.lesson_set.all()


class BannerCourse(Course):
    class Meta:
        verbose_name = '轮播课程'
        verbose_name_plural = verbose_name
        proxy = True


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='章节名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_lesson_videos(self):
        #获取该章节下的所有视频
        return self.video_set.all()


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name='章节')
    name = models.CharField(max_length=100, verbose_name='视频名称')
    url = models.CharField(max_length=200, verbose_name='访问地址', default='')
    learn_times = models.IntegerField(default=0, verbose_name='学习时长(分钟)')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name

class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='课件名称')
    download = models.FileField(upload_to='courses/resource/%Y/%m', verbose_name='资源文件', max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name
