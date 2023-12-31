from django.shortcuts import render,redirect
from django.views import View
from django.urls import reverse
from accounts.models import User
from django.contrib.auth import authenticate,login,logout
from accounts.forms import SignUpForm,LoginForm
from profiles.models import UserProfile

# Create your views here.
class LoginView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'account/login.html')
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            user =authenticate(
                request,
                username=form.cleaned_data.get("email"),
                password=form.cleaned_data.get("password"),
            )
            if user:
                login(request,user)
                return redirect(reverse("post-list"))
            return render(
                request,"account/login.html",{"errors":"user Does not exsit."}
            )
        return render(request,"account/login.html",{"errors":form.errors})
    
class SignUpView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'account/signup.html')
    
    def post(self,request,*args,**kwargs):
        data=request.POST
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=User(
                email=form.cleaned_data.get("email"),
                username=form.cleaned_data.get("username"),
                )
            user.set_password(form.cleaned_data.get("password"))
            user.save()
            UserProfile.objects.create(user=user,
                                       firstname=data.get("firstname"),
                                       lastname=data.get("lastname"))
            return redirect(reverse("login"))  
        else:
            print("Errors",form.errors)  
        return render(request,"account/signup.html",{'errors':form.errors}
        )

class LogoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect(reverse('login'))    