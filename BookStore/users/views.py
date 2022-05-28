from django.shortcuts import render
from django.views.generic import DetailView, FormView
from django.db import models
from .models import Profile
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.http import HttpResponse

class CreateProfileView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        data = form.cleaned_data
        user = User.objects.create_user(
            username=data['username'],
            password=data['password'],
            first_name = data['first_name'],
            last_name = data['last_name'],
            email=data['email']
        )
        user.profile.location = data['location']
        user.save()

        return HttpResponse('Вы зарегистрированы. Теперь Вам доступен личный кабинет на главной странице магазинa')

class DisplayDetailView(DetailView):
    template_name = 'profile_detail.html'
    model = Profile
