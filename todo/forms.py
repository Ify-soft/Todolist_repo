from django import forms
from .models import todolist, Profile, User



class formModel(forms.ModelForm):

	class Meta:
		model= todolist
		fields=['name', 'stipulated_time']
		widgets={'name':forms.TextInput(attrs={"class":"form-control styleForm"}), \
		'stipulated_time':forms.TimeInput(attrs={"class":"form-control styleForm", "type":"time"})}

class imageModel(forms.ModelForm):

	class Meta:
		model=Profile
		fields = ['image']
		

class UserEditForm(forms.ModelForm):

	class Meta:
		model=User
		fields=['email','first_name','last_name']



class multipleForm():
	form_classes = {
		'user':UserEditForm,
		'profile': imageModel
	}