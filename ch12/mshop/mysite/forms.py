from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.utils import ErrorList
from mysite import models

class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ['full_name', 'address', 'phone']

    def __init__(self, *args, **kwargs) -> None:
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].label = "收件人姓名"
        self.fields['address'].label = "郵件地址"
        self.fields['phone'].label = "連絡電話"