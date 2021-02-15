from django import forms
from .models import Member

class RegisterForm(forms.ModelForm):
    class Meta: #2
        model = Member 
        fields =['email','username','student_id','major','phone_number']
    