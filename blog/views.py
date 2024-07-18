from django.shortcuts import render,HttpResponseRedirect
from .forms import signUp,LoginUp,Postform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Post
from django.contrib.auth.models import Group
# Create your views here.
def home(request):
    posts=Post.objects.all()
    return render(request,'blog/home.html',{'posts':posts})
def about(request):
    return render(request,'blog/about.html')
def contact(request):
    return render(request,'blog/contact.html')
def dashboard(request):
    if request.user.is_authenticated:
     posts=Post.objects.all()
     return render(request,'blog/dashboard.html',{'posts':posts})
    else:
     return HttpResponseRedirect('/login/')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
def user_signup(request):
    if request.method=='POST':
        form=signUp(request.POST)
        if form.is_valid():
            messages.success(request,'congratulation!! now you become an author')
            user=form.save()
            group=Group.objects.get(name='Author')
            user.groups.add(group)
    else:
     form=signUp()
    return render(request,'blog/signup.html',{'form':form})
def login(request):
 if not request.user.is_authenticated: 
    if request.method=='POST':
        form=LoginUp(request=request,data=request)
        if form.is_valid():
            usname=form.cleaned_data['username']
            psword=form.cleaned_data['password']
            user=authenticate(username=usname,password=psword)
            if user is not None:
                login(request,user)
                messages.success(request,'you have successfully login')
                return HttpResponseRedirect('/dashboard/')
    else:        
     form=LoginUp()
    return render(request,'blog/login.html',{'form':form})
 else:
    return HttpResponseRedirect('/dashboard/')

def add_post(request):
   if request.user.is_authenticated:
      if request.method=='POST':
         form=Postform(request.POST)
         if form.is_valid():
            title=form.cleaned_data['title']
            desc=form.cleaned_data['desc']
            pst=Post(title=title,desc=desc)
            pst.save()
            form=Postform()
      else:
        form=Postform()     
      return render(request,'blog/addpost.html',{'form':form})
   else:   
    return HttpResponseRedirect('/login/')
   

def update_post(request,id):
   if request.user.is_authenticated:
      if request.method=="POST":
         pi=Post.objects.get(pk=id)
         form=Postform(request.POST,instance=pi)
         if form.is_valid():
            form.save()
      else:
         pi=Post.objects.get(pk=id)
         form=Postform(instance=pi)      
      return render(request,'blog/updatepost.html',{'form':form})
   else:   
    return HttpResponseRedirect('/login/')
   

def delete_post(request,id):
   if request.user.is_authenticated:
      if request.method=='POST':
         pi=Post.objects.get(pk=id)
         pi.delete()
         return HttpResponseRedirect('/dashboard/')
   else:  
    return HttpResponseRedirect('/login/')