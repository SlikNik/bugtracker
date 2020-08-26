from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from custom_users.models import CustomUser
from bugs.models import Ticket
from bugs.forms import AddTicketForm, LoginForm
# Create your views here.

def index(request):
    new_tickets = Ticket.objects.filter(status='NEW')
    progress_tickets = Ticket.objects.filter(status='IN PROGRESS')
    done_tickets = Ticket.objects.filter(status='DONE')
    invalid_tickets = Ticket.objects.filter(status='INVALID')
    return render(request, 'index.html', {'new_tickets': new_tickets, 'progress_tickets': progress_tickets, 'done_tickets': done_tickets, 'invalid_tickets': invalid_tickets})

def users_detail(request, username):
    current_user = CustomUser.objects.filter(username=username).first()
    user_filed = Ticket.objects.filter(filedBy=current_user)
    user_assigned = Ticket.objects.filter(assignedTo=username)
    user_completed = Ticket.objects.filter(completedBy=username)
    return render(request, 'user_detail.html', {'current_user': current_user, 'filed_tickets': user_filed, 'assigned_tickets': user_assigned, 'completed_tickets': user_completed})

def ticket_detail(request, id):
    current_ticket = Ticket.objects.filter(id=id).first()
    return render(request, 'ticket_detail.html', {'ticket': current_ticket})


@login_required
def ticket_submit(request):
    if request.method == 'POST':
        form = AddTicketForm(request.POST)
        if form.is_valid():
            new_ticket = form.save(commit=False)
            new_ticket.filedBy = CustomUser.objects.filter(username=request.user.username).first()
            new_ticket.save()
            return HttpResponseRedirect(reverse('homepage'))
    form = AddTicketForm()
    return render(request, 'generic_form.html', {'form': form})

   

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            check_user = authenticate(request, username=data.get('username'), password=data.get('password'))
            if check_user:
                login(request, check_user)
                return HttpResponseRedirect(reverse('homepage'))
                # return HttpResponseRedirect(request.GET.get( 'next',reverse('homepage')))
      
    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))