from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.models.CharField('카테고리이름', max_length=20)

class Post(models.Model):
    member = models.ForeignKey(Member,verbose_name='작성자')
    category = models.ForeignKey(Category,verbose_name='카테고리')
    title = models.CharField('제목', max_length=255)
    content = models.TextField('내용')
    is_deleted = models.BooleanField('삭제된글', default=False)
    created_at = models.DateTimeField('작성일', auto_now_add=True) 

class Comment(models.Model):
    member = models.ForeignKey(Member, verbose_name='작성자')
    post = models.ForeignKey(Post, verbose_name='원본글')
    content = models.TextField()
    is_blocked = models.BooleanField('노출제한', default=False)