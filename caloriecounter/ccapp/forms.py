
from django import forms
from ccapp.models import AppUser
class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        #field = " -all-"
        fields = ('email','password')
        model = AppUser

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields = ('first_name','middle_name','last_name','contact','email',\
            'gender','dob','blood_group','password','address','major_health_issue')
        model = AppUser

