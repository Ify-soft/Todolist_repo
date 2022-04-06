from django import forms
from django.contrib.auth.forms import UserCreationForm
from todo.models import User

class UserRegisterForm(UserCreationForm):
	email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control styleForm'}))
	first_name=forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class":"form-control styleForm"}))
	last_name=forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class":"form-control styleForm"}))

	class Meta:
		model=User
		fields=('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(UserRegisterForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class']="form-control styleForm"
		self.fields['password1'].widget.attrs['class']="form-control styleForm"
		self.fields['password2'].widget.attrs['class']="form-control styleForm"
		
	
		