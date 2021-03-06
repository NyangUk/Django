# blog/views.py
from django.shortcuts import render,get_object_or_404
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.utils import timezone
# Create your views here.
posts=Post.objects.all()
def post_list(request):
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request, 'blog/post_detail.html',{'post':post})

def post_new(request):
    if request.method == "POST":        # 데이터를 저장해야할때
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # 바로저장 X
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()                     # 바로저장 O
            return redirect('post_detail', pk=post.pk)
    else:                               # 입력 양식을 보여줘야 할때 
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})

def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def post_remove(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def post_edit(request,pk):
    post = get_object_or_404(Post, pk=pk)   # 이전 게시글 받아오기
    if request.method == "POST":        # 데이터를 저장해야할때
        form = PostForm(request.POST)
        if form.is_valid():
            edit = form.save(commit=False)  # 바로저장 X
            edit.author = request.user
            # post.published_date = timezone.now()
            post.save()                     # 바로저장 O
            return redirect('post_detail', pk=post.pk)
    else:                               # 입력 양식을 보여줘야 할때 
        form = PostForm(instance = post)
    return render(request, 'blog/post_edit.html', {'form': form})
