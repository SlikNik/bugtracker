from django import forms
from .models import Company, Employee, CustomUser, Role

class EmployeeSignUpForm(forms.Form):
    firstname = forms.CharField(max_length=120)
    lastname = forms.CharField(max_length=120)
    company = forms.ModelChoiceField(queryset=Company.objects.all())
    password = forms.CharField(widget=forms.PasswordInput)



class CompanySignUpForm(forms.Form):
    name = forms.CharField(max_length=120)
    founded = forms.IntegerField()
    specialize_in = forms.CharField(max_length=120)
    password = forms.CharField(widget=forms.PasswordInput)


