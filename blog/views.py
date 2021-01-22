# blog/views.py
from django.shortcuts import render,get_object_or_404
from .models import Post
from .forms import PostForm
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
            post.published_date = timezone.now()
            post.save()                     # 바로저장 O
            return redirect('post_detail', pk=post.pk)
    else:                               # 입력 양식을 보여줘야 할때 
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})