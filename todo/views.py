from django.shortcuts import render
from .forms import formModel, imageModel, UserEditForm
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect	
from django.contrib.auth.decorators import login_required
from .models import todolist, Profile, User
from django.db.models import Count
import datetime
import matplotlib.pyplot as plt
from django.urls import reverse
from django.http import JsonResponse
from io import BytesIO	
import base64	




# Create your views here.

@login_required
def home(request):
	return render(request, "todo/index.html")

class todoview(generic.CreateView):
	form_class=formModel
	template_name ='todo/todoform.html'
	success_url= '/todolist/'


	def form_valid(self, form):
		form.instance.user=self.request.user
		#name=todolist.objects.get(name=self.request.POST.get('name'), time=self.request.POST.get('time'))
		#stipulate_time=todolist.objects.get(stipulate=self.request.POST.get('name'), time=self.request.POST.get('time'))
		return super().form_valid(form)





@login_required
def display_function(request):
	prompt_date=datetime.datetime.today()
	date_time=str(prompt_date).split()
	date=date_time[0]
	todo=todolist.objects.filter(date=date, user=request.user).order_by('time')

	return render(request,  "todo/updateForm.html", {"todo":todo})


@login_required
def process_function(request):
	prompt_date=datetime.datetime.today()
	date_time=str(prompt_date).split()
	date=date_time[0]
	filtered_list=todolist.objects.filter(date=date, user=request.user).order_by('time')
	if request.method == "POST":
		#print(request.POST)
		#print(list(dict(request.POST).keys()))
		for i in list(filtered_list):
			#print(i.id)
			if str(i.id) in list(dict(request.POST).keys()):
				
				#print(i.name)
				a=todolist.objects.get(pk=i.id)
				#print(a.accountability)
				#print(request.POST[str(i.id)])
		
				a.accountability=request.POST[str(i.id)]
				a.save()
			else:
				a=todolist.objects.get(pk=i.id)
				#print("no")
				a.accountability=False
				a.save()
				
		return HttpResponse("Your activities was graded successfully")

	else:
		return HttpResponse("Your activities was not graded successfully")



class profile_page(generic.CreateView):
	form_class=imageModel
	template_name="todo/profile_page.html"
	

	def form_valid(self, form):
		form.instance.user=self.request.user
		#a=Profile.objects.get(user=self.request.user)
		#a.image=request.POST[]
		#name=todolist.objects.get(name=self.request.POST.get('name'), time=self.request.POST.get('time'))
		#stipulate_time=todolist.objects.get(stipulate=self.request.POST.get('name'), time=self.request.POST.get('time'))
		return super().form_valid(form)

	
		
	def get_context_data(self, **kwargs):
		context= super().get_context_data(**kwargs)
		print(self.request.user)

		context["user_data"]=User.objects.get(username=self.request.user)
		context['user_pix']= Profile.objects.get(user=self.request.user)
		return context


def profileUpdateView(request, pk):
	userImage=Profile.objects.get(user=request.user)
	userProfile=User.objects.get(username=request.user)
	if request.method !="POST":
		imageForm=imageModel(instance=userImage)
		userForm=UserEditForm(instance=userProfile)

	else:
		print(request.POST)
		
		userForm=UserEditForm(instance=userProfile, data=request.POST)
		imageForm=imageModel(request.POST, request.FILES)
		if imageForm.is_valid() and userForm.is_valid():
			print(imageForm.cleaned_data)
			userImage.image=imageForm.cleaned_data['image']
			print(userImage.image)
			userImage.save()
			userForm.save()
				
			return HttpResponseRedirect('/profile/')

	context={"imageForm":imageForm, "userForm":userForm}
	return render(request, "todo/profileEdit.html", context)





@login_required
def get_todolist_by_date(request):
	dict_by_date={}
	# query the database to get the todolist for a day
	a=todolist.objects.values('date').filter(user=request.user).annotate(count_date=Count('date'))
		
	for todo in a:
		b=todolist.objects.filter(user=request.user, date=todo['date']).order_by('time')
	
		dict_by_date[todo['date']]=b
	return render(request, 'todo/allList.html', {'listPerDay':dict_by_date})


@login_required
def get_todolist_for_today(request):
	prompt_date=datetime.datetime.today()
	date_time=str(prompt_date).split()
	date=date_time[0]
	today_filtered_list=todolist.objects.filter(date=date, user=request.user).order_by("time")
	return render(request, 'todo/todayList.html', {"today_filtered_list":today_filtered_list})


def daily_score_graph(request):
	result=[]
	result_X=[]
	faithful_list =todolist.objects.values('date').filter(user=request.user, accountability=True).annotate(count_date=Count("date"))
	a=todolist.objects.values('date').filter(user=request.user).annotate(count_date=Count('date'))
	c_activities=0
	print(faithful_list,a)
	for i in faithful_list:
		print(i)
		for z in a:
			if i['date']==z['date']:
				fraction= (int(i['count_date']) / int(z['count_date'])) * 100
				percent="{0:.2f}".format(fraction) +"%"
				result.append(percent)
				c_activities+=z["count_date"]
				result_X.append(c_activities)
			else:
				continue
	plt.switch_backend("AGG")
	fig=plt.figure(figsize=(10,4))
	print(result, result_X)
	plt.plot(result_X, result)
	plt.title("Daily Stat", fontsize=24)
	
	plt.xlabel("days", fontsize=14)
	plt.ylabel("Performance %", fontsize=14)


	plt.tick_params(axis='both', labelsize=14)
	plt.tight_layout()
	# Create a bytes buffer for the image to save
	buffer=BytesIO()
	# create the plot with the use of ByteIO object as its 'file'
	plt.savefig(buffer, format='png')
	# set the cursor the beggining os the stream
	buffer.seek(0)
	#retrieve the entire bontent of the 'file'
	image_png = buffer.getvalue()
	graph = base64.b64encode(image_png)
	graph = graph.decode('utf-8')
	
	buffer.close()
	context	={'graph':graph}
	return render(request, "todo/statGraph.html", context)

	
