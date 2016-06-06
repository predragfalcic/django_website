from django.db import models
from django import forms
from django.core.validators import EmailValidator
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length = 50)
	email = models.EmailField(blank = False, max_length = 200)
	message = models.TextField(blank = False)
	time_message_sent = models.DateTimeField(auto_now = False, auto_now_add = True)

	#if true than the contact waits for me to contact him, else if false than the contact was contacted
	contacted = models.BooleanField(default = False)

	class Meta:
		#sorting the data in the database
		ordering = ['-time_message_sent', 'name']