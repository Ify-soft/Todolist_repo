from django.shortcuts import render

from django.views import generic
from .forms import UserRegisterForm
from django.urls import reverse_lazy

class UserRegisterView(generic.CreateView):
	form_class = UserRegisterForm
	template_name = 'member/register.html'
	success_url = reverse_lazy('login')
# Create your views here.
