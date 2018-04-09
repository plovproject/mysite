from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Ваше имя', max_length=10)
    your_pass = forms.CharField(label='Пароль', min_length=8)

class Form_login(forms.Form):
    login = forms.CharField(min_length=5)
    password = forms.PasswordInput()
