from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .models import Candidate, VoteStatus,Position

# Create your views here.
def homepage(request):
	return render(request, "epoll/home.html")

def index(request):
	return HttpResponse('Hello world')