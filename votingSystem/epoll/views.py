from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .models import Candidate, VoteStatus, Position
from .forms import RegisterForm, ChangeForm 


# Create your views here.
def home_view(request):
	return render(request, "epoll/home.html")

def login_view(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect("dashboard")
		else:
			return render(request, "epoll/login.html", {"message": "Invalid credentials."})
	else:
		return render(request, "epoll/login.html")

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['password'] == cd['confirm_password']:
                obj = form.save(commit=False)
                obj.set_password(obj.password)
                obj.save()
                messages.success(request, 'You have been registered.')
                return redirect('home')
            else:
                return render(request, "epoll/register.html", {'form':form,'note':'password must match'})
    else:
        form = RegisterForm()

    return render(request, "epoll/register.html", {'form':form})



@login_required
def dashboard_view(request):
	return render(request, "epoll/dashboard.html")

@login_required
def logout_view(request):
	logout(request)
	return redirect("home")