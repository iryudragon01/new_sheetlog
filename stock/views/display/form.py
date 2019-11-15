from django import forms


class loginform(forms.Form):
    name = forms.CharField(max_length=200,min_length=1)
    password = forms.CharField(max_length=120,widget=forms.PasswordInput)

