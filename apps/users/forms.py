import re

__author__ = 'duxi'
__date__ = '2017-9-1 16:09'
from django import forms
from captcha.fields import CaptchaField

from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6)
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=6)
    password2 = forms.CharField(required=True, min_length=6)


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nick_name', 'mobile', 'gender', 'birthday', 'address']
        # 验证手机号码是否正确（当不是必填项时不需要）
        # def clean_mobile(self):
        #     mobile = self.cleaned_data['mobile']
        #     regex = "^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\\d{8}$"
        #     p = re.compile(regex)
        #     if p.match(mobile):
        #         return mobile
        #     else:
        #         raise forms.ValidationError('手机号非法',code='mobile_invalid')
