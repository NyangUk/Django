from django.contrib import admin
from member.models import Member
from post.models import Post
from datetime import date

# action_1 사용자 인증하기
def certify_user(modeladmin, request ,queryset):
    queryset.update(is_certificated = True,certification_date =date.today())
certify_user.short_description = "선택된 사용자를 인증합니다."

class MemberAdmin(admin.ModelAdmin):
    actions = [certify_user]    # action 추가 
    list_per_page = 5
    list_display = (
        'id','email','username','permission',
        'is_certificated','certification_date','post_count',
    )
    list_editable = ('permission',)
    list_filter = ('permission', )
    search_fields = ('username', )
    ordering = ('-id', 'email', 'permission', )

    def post_count(self, obj):
        return Post.objects.filter(member=obj).count()
    
    post_count.short_description = '작성한 글 수'
# Register your models here.
admin.site.register(Member, MemberAdmin)

