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
from django.urls import path
from bugs import views 

urlpatterns = [
    path('', views.index, name='homepage'),
    path('login/', views.login_view, name='loginview'),
    path('logout/', views.logout_view, name='logoutview'),
    path('ticket/<int:id>/edit/', views.ticket_edit, name='ticketedit'),  
    path('ticket/<int:id>/', views.ticket_detail, name='ticketdetails'),
    path('complete/<int:id>/', views.ticket_complete, name='ticketcomplete'),
    path('claim/<int:id>/', views.ticket_claim, name='ticketclaim'),
    path('invalid/<int:id>/', views.ticket_invalid, name='ticketinvalid'),
    path('submit/<int:id>/', views.ticket_submit, name='ticketsubmit'),
    path('user/<str:username>/', views.users_detail, name='userdetails'),
    path('admin/', admin.site.urls),
]
