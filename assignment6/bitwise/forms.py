from django import forms

class NumberForm(forms.Form):
    a = forms.IntegerField(min_value=0, label="Número A")
    b = forms.IntegerField(min_value=0, label="Número B")
    c = forms.IntegerField(min_value=0, label="Número C")
    d = forms.IntegerField(min_value=0, label="Número D")
    e = forms.IntegerField(min_value=0, label="Número E")
