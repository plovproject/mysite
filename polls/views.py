from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth import forms, login, logout

def index(request):
    return render(request, 'polls/index.html')

def Get_users(request):
    u_list = User.objects
    u_l = []
    for u in u_list:
        if (u.is_authenticated()) and (u != request.user):
            # c = context(u.id:u.username)
            u_l.push(c)
    return u_l

def chat_room(request):
    u = Get_users(request)
    return render(request, 'polls/chat_room.html', u)

class RegisterFormView(FormView): # регистрация пользователя
    form_class = forms.UserCreationForm # подключили стандартную форму
    success_url = "/polls/login/" # страница входа для зареганных пользователей
    template_name = "polls/register.html" # шаблон для отображения представления
    def form_valid(self, form): # проверка на валидность
        form.save() # создаём пользователя, если данные корректны (корректность проверяется автоматом)
        return super(RegisterFormView, self).form_valid(form) # вызываем метод базового класса

class LoginFormView(FormView): # вход пользователя
    form_class = forms.AuthenticationForm # подключили стандартную форму
    success_url = "/polls/" # переадресация после удачного входа на сайт
    template_name = "polls/login.html" # шаблон для отображения представления
    def form_valid(self, form): #
        self.user = form.get_user() # берём данные пользователя из формы
        login(self.request, self.user) # функция логина юзера
        return super(LoginFormView, self).form_valid(form) # вызываем метод базового класса

class LogOutFormView(FormView): # выход пользователя
    def get(self, request): #
        logout(request) # функция выхода пользователя
        return HttpResponseRedirect("/polls/") #перенаправление на главную после "выхода"
