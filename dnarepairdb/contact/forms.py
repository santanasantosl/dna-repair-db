# -*- coding: utf-8 -*-
from django import forms

class ContactFrom(forms.Form):

    name = forms.CharField(max_length=120, required=True)
    email = forms.EmailField(required=True)
    comment = forms.CharField(required=True, widget=forms.Textarea)