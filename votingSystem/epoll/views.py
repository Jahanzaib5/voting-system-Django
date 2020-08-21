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

@login_required
def position_view(request):
	position = Position.objects.all()
	return render(request, 'epoll/position.html', {"obj": position})

@login_required
def candidate_view(request, pos):
	obj=get_object_or_404(Position, pk=pos)
	if request.method == 'POST':
		temp = VoteStatus.objects.get_or_create(user=request.user, position=obj)[0]
		if temp.status == False:
			temp2=Candidate.objects.get(pk=request.POST.get(obj.title))
			temp2.no_votes+=1
			temp2.save()
			temp.status=True
			temp.save()
			return HttpResponseRedirect("/position/")
		else:
			messages.success(request, "You have already voted for this position!")
			return render(request, 'epoll/candidate.html', {'obj': obj})
	else:
		return render(request, 'epoll/candidate.html', {'obj': obj})


@login_required
def candidateDetail_view(request, id):
	obj=get_object_or_404(Candidate, pk=id)
	return render(request, 'epoll/c_detail.html', {'obj': obj})

@login_required
def result_view(request):
	obj = Candidate.objects.all().order_by('position', '-no_votes')
	return render(request, "epoll/results.html", {'obj': obj})	

@login_required
def changePassword_view(request):
	if request.method == "POST":
		form = PasswordChangeForm(user=request.user, data=request.POST)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('dashboard')
	else:
		form = PasswordChangeForm(user=request.user)

	return render(request, "epoll/password.html", {'form': form})		