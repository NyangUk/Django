# Custom_admin/post/admin.py
from django.contrib import admin
from post.models import Category, Post, Comment
from member.models import Member
from post.forms import MyPostAdminForm
from .filters import CreatedDateFilter
from django.urls import path
import datetime
from django.template.response import TemplateResponse
from django.shortcuts import  get_object_or_404
# Register your models here.
posts = Post.objects.all()
categotys =Category.objects.all()
class CategoryAdmin(admin.ModelAdmin):
    # form = 
    
    list_per_page =10
    list_display = (
        'id' ,'name' , 'post_count' , 'post_recent'
    )
    def post_count(self, obj):
        return Post.objects.filter(category=obj).count()
    def post_recent(self, obj):
        li =[]
        for i in Post.objects.filter(category=obj):
            li.append(i.created_at.ctime())
        return li
class PostAdmin(admin.ModelAdmin):
    form = MyPostAdminForm
    list_per_page = 10
    list_display = (
    'id', 'title', 'member','is_deleted', 'created_at', )
    list_editable = ('is_deleted', )
    list_filter = (
    'member__permission',
    'category__name', 'is_deleted',CreatedDateFilter )
    # fields = ('member','category','title',)
    fieldsets = (
        ('기본정보', {
            "fields": (('member','category')),
        }),
        ('제목 및 내용', {
            "fields": ('title','content',),
        }),
        ('삭제', {
            "fields": ('is_deleted',),
        })

    )

    def get_urls(self):
        urls = super().get_urls()
        post_urls = [
            path(r'status/', self.admin_site.admin_view(self.post_status_view))
        # url(r'^status/$', self.admin_site.admin_view(self.post_status_view))
        ]
        return post_urls + urls
    def post_status_view(self, request):
        context = dict(
        self.admin_site.each_context(request),
        posts=Post.objects.all(),
        # key = value,
        )
        return TemplateResponse(request, "admin/post_status.html", context)
    
admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Comment)
