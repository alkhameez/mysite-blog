from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth import authenticate, login

from django.contrib import messages
from .models import *

def home(request):
	query = Post.objects.all().order_by('-published_date')
	context = {'query':query}
	return render(request, 'home1.html', context)

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			messages.success(request, 'Account created successfully')
			login(request, user)
			return redirect('/')
	else:
		form = UserCreationForm()

	return render(request, 'register_form.html', {'form':form})

def pass_change(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			return redirect('/password_change_done')
	else:
		form = PasswordChangeForm(user=request.user)
	context = {'form': form}

	return render(request, 'pass_change_form.html', context)

def password_change_done(request):
	return render(request, 'pass_change_done_form.html')


def password_reset(request):
	if request.method == 'POST':
		form = PasswordResetForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/passord_reset_confirm')
	else:
		form = PasswordResetForm()
	context = {'form': form}

	return render(request, 'pass_reset_form.html', context)



def password_reset_confirm(request):
	return render(request, 'pass_reset_confirm.html')