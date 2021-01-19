from django.shortcuts import render
from .models import Post
# Create your views here.
posts=Post.objects.all()
def post_list(request):
    return render(request, 'blog/post_list.html', {'posts':posts})