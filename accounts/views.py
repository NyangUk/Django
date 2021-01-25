from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
import blog.views
import blog.urls
# Create your views here.

# 회원 가입
def signup(request):
    if request.method == 'POST':
        if request.POST['userPw'] == request.POST['confirm']:
            user = User.objects.create_user(username=request.POST['userId'], password=request.POST['userPw'])
            auth.login(request, user)
            return redirect('post_list')
    return render(request, 'accounts/signup.html')

# 로그인
def login(request):
    if request.method == 'POST':
        userId = request.POST['userId']
        userPw = request.POST['userPw']
        user = auth.authenticate(request, username=userId, password=userPw)
        
        if user is not None:
            auth.login(request, user)
            return redirect('post_list')
        else:
            return render(request, 'login.html', {'error' : 'userId or userPw is incorrect.'})
    else:
        return render(request, 'accounts/login.html')

# 로그 아웃
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('post_list')
    return render(request, 'accounts/login.html')
