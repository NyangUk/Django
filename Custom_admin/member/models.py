from django.db import models

# Create your models here.
class Member(AbstractBaseUser):
    TYPE_PERMISSIONS =  (
        ('AD','관리자'),
        ('ET','에디터'),
        ('MB','일반'),
    )
    email = models.EmailField('이메일', max_length=255, unique =True)
    username = models.CharField('닉네임',max_length=30)
    permission = models.CharField('권한', max_length=2, choices = TYPE_PERMISSIONS, default= 'MB')
    certification_date = models.DateField('인증일', defualt=None, null =True, blank =True)
    is_certificated =models.BooleanField('인증상태',defualt=False)
    