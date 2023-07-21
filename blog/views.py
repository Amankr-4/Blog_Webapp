from django.shortcuts import render , HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm 
from .forms import Signupform ,  loginform ,postform
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from .models import post
from django.contrib.auth.models import Group

# Create your views here.

def home(request):
    posts =post.objects.all()
    return render(request,'blog/home.html',{'posts' : posts})

def about(request):
    return render(request,'blog/about.html')

def contact(request):
    return render(request,'blog/contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        posts = post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request,'blog/dashboard.html',{'posts' :posts,'full_name':full_name,'groups':gps})
    else:
        return HttpResponseRedirect('/login/')

def user_login(request):
    if not request.user.is_authenticated:  #to check that user is already logged in or not
        if request.method == 'POST':
            form = loginform(request=request ,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password = upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,"Logged In Successfully!!")
                    return HttpResponseRedirect('/dashboard/')
            
        form = loginform()
        return render(request,'blog/login.html',{'form' : form})
    else:
        return HttpResponseRedirect('/dashboard/')
    
    
def signup(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations, You became a Author :)')
            user=form.save()
            group = Group.objects.get(name='author')
            user.groups.add(group)
    else:
        form=Signupform()
    return render(request,'blog/signup.html',{'form':form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

# addpost
def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = postform(request.POST)
            if form.is_valid():
                form.save()
                form = postform()
        else:
            form = postform()       
        return render(request,'blog/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

# Updatepost
def update_post(request,id):
    if request.user.is_authenticated:
        if request.method== 'POST':
            pi = post.objects.get(pk=id)
            form = postform(request.POST,instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi = post.objects.get(pk=id)
            form= postform(instance=pi)    
        return render(request,'blog/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')
    
# Deletepost
def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method== 'POST':   # delete btn me click hoga to post request aayega qki delete form ke ander h ye safest tarika hota h element delete karne ke liye 
            pi = post.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/') 
