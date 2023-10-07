from collections.abc import Mapping
import os
from typing import Any
from django import forms
from django.forms.utils import ErrorList


class GenForm(forms.Form):
    msg = forms.CharField(
        label='訊息', widget=forms.Textarea(attrs={'style': 'resize:none'}))
    font_size = forms.IntegerField(
        label='文字尺寸(12-120)', min_value=12, max_value=120)
    x = forms.IntegerField(label='X(0-200)', min_value=0, max_value=200)
    y = forms.IntegerField(label='Y(0-200)', min_value=0, max_value=200)

    def __init__(self, backfiles, *args, **kwargs):
        super(GenForm, self).__init__(*args, **kwargs)
        self.fields['backfile'] = forms.ChoiceField(
            choices=[(os.path.basename(bf), os.path.basename(bf))
                     for bf in backfiles]
        )


class CustomForm(forms.Form):
    msg = forms.CharField(
        label='訊息', widget=forms.Textarea(attrs={'style': 'resize:none'}))
    font_size = forms.IntegerField(
        label='文字尺寸(12-120)', min_value=12, max_value=120)
    x = forms.IntegerField(label='X(0-200)', min_value=0, max_value=200)
    y = forms.IntegerField(label='Y(0-200)', min_value=0, max_value=200)


class UploadForm(forms.Form):
    file = forms.FileField()
