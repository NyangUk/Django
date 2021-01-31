# Custom_admin/post/forms.py
from django import forms
class MyPostAdminForm(forms.ModelForm):
    def clean_content(self):
        content = self.cleaned_data["content"]
        words = ['금지어','욕설','관리자']
        error_msg = '{0} {1} 같은 단어는 쓸 수 없습니다.'.format(', '.join(words),'와')

        if any(word in content for word in words):
            raise forms.ValidationError(error_msg)
            
        return content
        