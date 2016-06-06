from django import forms
from .models import Contact
from django.db import models
from captcha.fields import CaptchaField

class ContactForm(forms.ModelForm):
	captcha = CaptchaField(error_messages={'required': 'Please enter the characters from the picture below.'})
	class Meta:
		model = Contact
		fields = [
			'name',
			'email',
			'message',
		]


	#pomocu ovog dole moguce je primenjivati razlicite nacine za styling nasih polja odradjenih preko djanga
	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['name'].widget = forms.TextInput(attrs={
			'placeholder': 'Name', 
			'required': True,
			'class': "12u"})

		self.fields['email'].widget = forms.EmailInput(attrs={
			'placeholder': 'Email',
			'required': True,
			'class': "12u"})

		self.fields['message'].widget = forms.Textarea(attrs={
			'placeholder': 'Message',
			'rows': 6,
			'required': True,
			'class': "12u"})

