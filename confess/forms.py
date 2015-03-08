from .models import Post
from django import forms
from django.forms import ModelForm

class ConfessForm(ModelForm):

	class Meta:
		model = Post
		fields = ['title','text']