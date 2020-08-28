from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login
from django.views.generic import CreateView
from .forms import CompanySignUpForm, EmployeeSignUpForm
from .models import CustomUser, Role, Company, Employee


def CompanySignUpView(request):
    if request.method == "POST":
        form = CompanySignUpForm(request.POST)
        if form.is_valid():
            signup = form.cleaned_data
            new_user = CustomUser.objects.create_user(
                username=''.join(signup.get('name').split()).capitalize(),
                role='COMPANY',
                password=signup.get('password')
            )
            company = Company.objects.create(
                user=new_user, 
                name=signup.get('name'),
                founded=signup.get('founded'),
                specialize_in=signup.get('specialize_in')
            )
            login(request, new_user)
            return HttpResponseRedirect(reverse('homepage'))
            # return HttpResponseRedirect(request.GET.get( 'next',reverse('homepage')))
    
    form = CompanySignUpForm()
    return render(request, 'registration/signup_form.html', {'form': form, 'user_type': 'Company'})

def EmployeeSignUpView(request):
    if request.method == "POST":
        form = EmployeeSignUpForm(request.POST)
        if form.is_valid():
            signup = form.cleaned_data
            new_user = CustomUser.objects.create_user(
                username=signup.get('firstname').capitalize() + signup.get('lastname').capitalize(),
                role='EMPLOYEE',
                password=signup.get('password')
            )
            employee = Employee.objects.create(
                user=new_user,
                firstname=signup.get('firstname'),
                lastname=signup.get('lastname'),
                company=signup.get('company')
            )
            login(request, new_user)
            return HttpResponseRedirect(reverse('homepage'))
            # return HttpResponseRedirect(request.GET.get( 'next',reverse('homepage')))
      
    form = EmployeeSignUpForm()
    return render(request, 'registration/signup_form.html', {'form': form, 'user_type': 'Employee'})

def SignUpView(request):
    return render(request,'registration/signup.html')