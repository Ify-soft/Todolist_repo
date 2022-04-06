from django import forms
from .models import todolist


class formModel(forms.ModelForm):

	class Meta:
		model= todolist
		fields=['name', 'stipulated_time']
		widgets={'name':forms.TextInput(attrs={"class":"form-control styleForm"}), \
		'stipulated_time':forms.TimeInput(attrs={"class":"form-control styleForm", "type":"time"})}
