from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect

from .models import Contact
from .forms import ContactForm
from django.contrib import messages

# Create your views here.

def contact_create(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		form = ContactForm()
		messages.success(request, 'Your message was sent successfully. We will contact you shortly.')
		return HttpResponseRedirect('/home')
	context = {
		"form": form,
	}
	
	return render(request, 'index.html', context)