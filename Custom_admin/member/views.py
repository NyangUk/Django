from  django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Member
def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_member = Member.objects.create(**form.cleaned_data)
            login(requset, new_member)
        return redirect('home')
    else:
        form = RegisterForm()
    return render(request,'member/signup.html')
def login(requset):
        return render(request,'home.html')
def logout(requset):
        return render(request,'home.html')