"""BugTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from bugs import views 
from custom_users.views import SignUpView, CompanySignUpView, EmployeeSignUpView

urlpatterns = [
    path('', views.home, name='homepage'),
    path('signup/', SignUpView, name='signup'),
    path('company/signup/', CompanySignUpView, name='company_signup'),
    path('employee/signup/', EmployeeSignUpView, name='employee_signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('alltickets/', views.tickets, name='alltickets'),
    path('ticket/<int:id>/edit/', views.ticket_edit, name='ticketedit'),  
    path('ticket/<int:id>/', views.ticket_detail, name='ticketdetails'),
    path('ticket/complete/<int:id>/', views.ticket_complete, name='ticketcomplete'),
    path('ticket/claim/<int:id>/', views.ticket_claim, name='ticketclaim'),
    path('ticket/invalid/<int:id>/', views.ticket_invalid, name='ticketinvalid'),
    path('ticket/submit/', views.ticket_submit, name='ticketsubmit'),
    path('allprojects/', views.projects, name='allprojects'),
    path('project/<int:id>/edit/', views.project_edit, name='projectedit'),  
    path('project/<int:id>/', views.project_detail, name='projectdetails'),
    path('project/complete/<int:id>/', views.project_complete, name='projectcomplete'),
    path('project/claim/<int:id>/', views.project_claim, name='projectclaim'),
    path('project/invalid/<int:id>/', views.project_invalid, name='projectinvalid'),
    path('project/submit/', views.project_submit, name='projectsubmit'),
    path('allcompanies/', views.companies, name='allcompanies'),
    path('allemployees/', views.employees, name='allemployees'),
    path('employee/<str:username>/', views.employee_detail, name='employeedetails'),
    path('company/<str:username>/', views.company_detail, name='companydetails'),
    path('admin/', admin.site.urls),
]