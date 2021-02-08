from django.shortcuts import render, get_object_or_404
from .models import Post ,Category
# Create your views here.
posts=Post.objects.all()
categorys =Category.objects.all()
def home(requset):
    post_category = []
    for category in categorys:
        post_category.append(Post.objects.filter(category = category))
    context = {
        'post_category' : post_category,
    }
    return render(requset ,'post/base.html', context)
# def post_list(request):
#     return render(request,'post')