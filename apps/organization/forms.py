# _*_ encoding:utf-8 _*_
__author__ = 'duanlian'
__date__ = '2017/3/5 16:56'

from django import forms
from operation.models import UserAsk


class UserAskForm(forms.ModelForm):

    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']
