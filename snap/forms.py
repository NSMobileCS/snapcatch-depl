# -*- coding: utf-8 -*-
from django import forms
from . import models

class CatchForm(forms.ModelForm):
    # imgfile = forms.ImageField(label='Select image')
    class Meta(object):
        model = models.Catch
        fields = ('notes', 'pic')
