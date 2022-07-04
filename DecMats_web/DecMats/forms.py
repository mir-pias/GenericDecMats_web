from django import forms
from django.core.exceptions import ValidationError
import django.core.validators as val
from django.utils.translation import gettext_lazy as _
import re
# from .helper import Helper

class InputForm(forms.Form):

    type = forms.CharField(help_text='e.g. A, B', required=False)
    
    n = forms.CharField(help_text='e.g. 2,3 ', required=False, 
        validators=[val.int_list_validator(sep=',', message='enter whole number(s)', code='invalid', allow_negative=False)])
    
    d = forms.CharField(help_text='e.g. 2,4', required=False, 
        validators=[val.int_list_validator(sep=',', message='enter whole number(s)', code='invalid', allow_negative=False)])
