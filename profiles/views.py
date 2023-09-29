from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import redirect, render
from profiles.forms import ProfileForm
from django.urls import reverse


# Create your views here.
class ProfileEditView(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
            form=ProfileForm(instance=request.user.profile)
            return render(request,"profile/profile.html",context={"form":form})
    def post(self,request,*args,**kwargs):
        form=ProfileForm(instance=request.user.profile,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("home"))
        return render(request,"profile/profile.html",context={"form":form})