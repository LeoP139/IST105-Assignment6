from django import forms

class NumberForm(forms.Form):
    a = forms.IntegerField(min_value=0, label="Number A")
    b = forms.IntegerField(min_value=0, label="Number B")
    c = forms.IntegerField(min_value=0, label="Number C")
    d = forms.IntegerField(min_value=0, label="Number D")
    e = forms.IntegerField(min_value=0, label="Number E")
