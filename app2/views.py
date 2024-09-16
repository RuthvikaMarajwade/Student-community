from django.shortcuts import render,redirect
from app2.forms import Usersignup
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from app2.models import Jobpost,Company
from django.db.models import Q
# Create your views here.
def home(request): 
    j=Jobpost.objects.all()[0:6]
    c=Company.objects.all()[0:6]
    jo=Jobpost.objects.all().order_by('-date')
    c={'j':j,'c':c,'jo':jo}
    if request.method=="POST":
        t=request.POST.get('job-title')
        l=request.POST.get('job-location')
        jo=Jobpost.objects.filter(job__icontains=t,location__icontains=l)
        c={'jo':jo}
        return render(request,'app2/job-listings.html',c)
    else:
        return render(request,'app2/home.html',c)
def search(request):
      if request.method=="POST":
        t=request.POST.get('job-title')
        l=request.POST.get('job-location')
        jo=Jobpost.objects.filter(job__contains=t,location__contains=l)
        c={'jo':jo}
        return render(request,'app2/job-listings.html',c)
      else:
           return render(request,'app2/home.html',c)
def details(request,slug):
    s=Jobpost.objects.get(slug=slug)
    c={'s':s}
    return render(request,'app2/job-details.html',c)
def listing(request):
    q='ALL JOBS'
    jo=Jobpost.objects.all().order_by('-date')
    c={'jo':jo}
    if request.method=="POST":
        t=request.POST.get('job-title')
        l=request.POST.get('job-location')
        q="Result For  "+t
        jo=Jobpost.objects.filter(job__icontains=t,location__icontains=l)
        c={'jo':jo,'q':q}
        return  render(request,'app2/job-listings.html',c)
    else:
        c={'jo':jo,'q':q}
        return render(request,'app2/job-listings.html',c)
def signup(request):
    ob=Usersignup()
    if request.method=="POST":
        ob=Usersignup(request.POST)
        if ob.is_valid(): 
            u=ob.save()
            login(request,u)
            return redirect("/")
    c={'ob':ob}
    return render(request,'app2/nsignup.html',c)
def login_req(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="app2/login.html", context={"login_form":form})
def logout_req(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/")


  