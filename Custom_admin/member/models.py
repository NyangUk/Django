from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Member(AbstractUser):
    TYPE_PERMISSIONS =  (
        ('AD','관리자'),
        ('ET','에디터'),
        ('MB','일반'),
    )
    TYPE_MAJOR= (
        ('1','전자공학과'),
        ('2','컴퓨터공학과'),
        ('3','산업경영공학과'),

    )
    email = models.EmailField('이메일', max_length=255, unique =True)
    username = models.CharField('닉네임',max_length=30, unique =True)
    phone_number= models.CharField('전화번호', max_length=11,unique =True)
    student_id = models.CharField('학번', max_length=11,unique =True)
    major =  models.CharField('학과', max_length=1, choices = TYPE_MAJOR)
    permission = models.CharField('권한', max_length=2, choices = TYPE_PERMISSIONS, default= 'MB')
    certification_date = models.DateField('인증일', default=None, null =True, blank =True)
    is_certificated =models.BooleanField('인증상태',default=False)

