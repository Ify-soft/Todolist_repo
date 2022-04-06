from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

User= get_user_model()

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image=models.ImageField(upload_to='media/')

	def __str__(self):
		return self.user.username

class todolist(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	name= models.CharField(max_length=200)
	time=models.DateTimeField(auto_now_add=True)
	date=models.DateField(auto_now_add=True)
	stipulated_time=models.CharField(max_length=10)
	accountability=models.BooleanField(default=False)
	def __str__(self):
		return f'{self.user.username} | {self.name}'
		

	def get_absolute_url(self):
		return reverse('todo:home')