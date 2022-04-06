from django.shortcuts import render
from .forms import formModel
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import todolist
import datetime


# Create your views here.

@login_required
def home(request):
	return render(request, "todo/index.html")

class todoview(generic.CreateView):
	form_class=formModel
	template_name ='todo/todoform.html'


	def form_valid(self, form):
		form.instance.user=self.request.user
		#name=todolist.objects.get(name=self.request.POST.get('name'), time=self.request.POST.get('time'))
		#stipulate_time=todolist.objects.get(stipulate=self.request.POST.get('name'), time=self.request.POST.get('time'))
		return super().form_valid(form)





class analyseViews(generic.CreateView):
	model= todolist
	template_name= "todo/updateForm.html"
	fields=["accountability"]


	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		prompt_date=datetime.datetime.today()
		date_time=str(prompt_date).split()
		date=date_time[0]
		context['date']= todolist.objects.filter(date=date)
		
		return context



	
