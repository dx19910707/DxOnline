import re

from django import forms

from operation.models import UserAsk
__author__ = 'duxi'
__date__ = '2017-9-5 14:21'


class UserAskForm(forms.ModelForm):

    class Meta:
        model = UserAsk
        fields = ['name','mobile','course_name']

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        regex = "^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\\d{8}$"
        p = re.compile(regex)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError('手机号非法',code='mobile_invalid')