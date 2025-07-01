from django import forms

class NumberInputForm(forms.Form):
    a = forms.FloatField(label='Value A', required=True)
    b = forms.FloatField(label='Value B', required=True)
    c = forms.FloatField(label='Value C', required=True)
    d = forms.FloatField(label='Value D', required=True)
    e = forms.FloatField(label='Value E', required=True)