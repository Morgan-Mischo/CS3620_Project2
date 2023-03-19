from django import forms

class InputForm(forms.Form):
    noun1 = forms.CharField(max_length=200)
    pluralNoun = forms.CharField(max_length=200)
    noun2 = forms.CharField(max_length=200)
    place = forms.CharField(max_length=200)
    adjective = forms.CharField(max_length=200)
    noun3 = forms.CharField(max_length=200)