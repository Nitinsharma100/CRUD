from django import forms
from .models import user

class curd(forms.ModelForm):
    class Meta:
        model=user
        fields=['name','email','password']
        widgets={
            'password':forms.PasswordInput
        }
