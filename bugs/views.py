from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from custom_users.models import CustomUser, Company, Employee, Role
from custom_users.decorators import company_required, employee_required
from bugs.models import Ticket, Project
from bugs.forms import AddTicketForm, AddProjectForm, LoginForm
# Create your views here.

now = timezone.now()

def home(request):
    return render(request, 'home.html')

@login_required
def employees(request):
    all_employees = Employee.objects.order_by('lastname')
    return render(request, 'employees.html', {'employees': all_employees})

@login_required
def companies(request):
    all_companies = Company.objects.order_by('name')
    return render(request, 'companies.html', {'companies': all_companies})

@login_required
def tickets(request):
    new_tickets = Ticket.objects.filter(status='NEW')
    progress_tickets = Ticket.objects.filter(status='IN PROGRESS')
    done_tickets = Ticket.objects.filter(status='DONE')
    invalid_tickets = Ticket.objects.filter(status='INVALID')
    return render(request, 'tickets.html', {'new_tickets': new_tickets, 'progress_tickets': progress_tickets, 'done_tickets': done_tickets, 'invalid_tickets': invalid_tickets, 'now': now})

@login_required
def projects(request):
    new_projects = Project.objects.filter(status='NEW')
    progress_projects = Project.objects.filter(status='IN PROGRESS')
    done_projects = Project.objects.filter(status='DONE')
    invalid_projects = Project.objects.filter(status='INVALID')
    return render(request, 'projects.html', {'new_projects': new_projects, 'progress_projects': progress_projects, 'done_projects': done_projects, 'invalid_projects': invalid_projects, 'now': now})

def company_detail(request, username):
    current_user = CustomUser.objects.filter(username=username).first()
    current_company = Company.objects.filter(user=current_user).first()
    new_projects = Project.objects.filter(company=current_company).filter(status='NEW')
    progress_projects = Project.objects.filter(company=current_company).filter(status='IN PROGRESS')
    done_projects = Project.objects.filter(company=current_company).filter(status='DONE')
    invalid_projects = Project.objects.filter(company=current_company).filter(status='INVALID')
    return render(request, 'company_detail.html', {'current_company': current_company, 'new_projects': new_projects, 'progress_projects': progress_projects, 'done_projects': done_projects, 'invalid_projects': invalid_projects, 'now':now})

def employee_detail(request, username):
    current_user = CustomUser.objects.filter(username=username).first()
    current_employee = Employee.objects.filter(user=current_user).first()
    user_filed = Ticket.objects.filter(filedBy=current_employee)
    user_assigned = Ticket.objects.filter(assignedTo=username)
    user_completed = Ticket.objects.filter(completedBy=username)
    return render(request, 'employee_detail.html', {'current_employee': current_employee, 'filed_tickets': user_filed, 'assigned_tickets': user_assigned, 'completed_tickets': user_completed})

def project_detail(request, id):
    current_project = Project.objects.filter(id=id).first()
    return render(request, 'project_detail.html', {'project': current_project})

def ticket_detail(request, id):
    current_ticket = Ticket.objects.filter(id=id).first()
    return render(request, 'ticket_detail.html', {'ticket': current_ticket})


@login_required
@company_required
def project_submit(request):
    current= CustomUser.objects.filter(username=request.user.username).first()
    if request.method == 'POST':
        form = AddProjectForm(request.POST)
        if form.is_valid():
            new_project = form.save(commit=False)
            new_project.company = Company.objects.filter(user=current.id).first()
            new_project.save()
            return HttpResponseRedirect(reverse('homepage'))
    form = AddProjectForm()
    return render(request, 'generic_form.html', {'form': form})

@login_required
@company_required
def project_edit(request, id):
    current_project = Project.objects.get(id=id)
    if request.method == 'POST':
        form = AddProjectForm(request.POST)
        if form.is_valid():
            new_project = form.cleaned_data
            current_project.title = new_project['title']
            current_project.description = new_project['description']
            current_project.save()
        return HttpResponseRedirect(reverse('projectdetails', args=[current_project.id]))
    form = AddProjectForm(initial={'title' : current_project.title, 'description': current_project.description})
    return render(request, 'generic_form.html', {'form': form})

@login_required
@company_required
def project_claim(request, id):
    current_project = Project.objects.filter(id=id).first()
    current_project.status = "IN PROGRESS"
    current_project.save()
    return HttpResponseRedirect(reverse('projectdetails', args=[current_project.id]))

@login_required
@company_required
def project_complete(request, id):
    current_project = Project.objects.filter(id=id).first()
    current_project.status = "DONE"
    current_project.save()
    return HttpResponseRedirect(reverse('projectdetails', args=[current_project.id]))

@login_required
@company_required
def project_invalid(request, id):
    current_project = Ticket.objects.filter(id=id).first()
    current_project.status = "INVALID"
    current_project.save()
    return HttpResponseRedirect(reverse('projectdetails', args=[current_project.id]))

@login_required
@employee_required
def ticket_submit(request):
    employee = CustomUser.objects.filter(username=request.user.username).first()
    if request.method == 'POST':
        form = AddTicketForm(request.POST)
        if form.is_valid():
            new_ticket = form.save(commit=False)
            new_ticket.filedBy = Employee.objects.filter(user=employee.id).first()
            new_ticket.company = Company.objects.filter(user=employee.company).first()
            new_ticket.save()
            return HttpResponseRedirect(reverse('homepage'))
    form = AddTicketForm()
    return render(request, 'generic_form.html', {'form': form})

@login_required
@employee_required
def ticket_edit(request, id):
    current_ticket = Ticket.objects.get(id=id)
    if request.method == 'POST':
        form = AddTicketForm(request.POST)
        if form.is_valid():
            new_ticket = form.cleaned_data
            current_ticket.title = new_ticket['title']
            current_ticket.description = new_ticket['description']
            current_ticket.save()
        return HttpResponseRedirect(reverse('ticketdetails', args=[current_ticket.id]))
    form = AddTicketForm(initial={'title' : current_ticket.title, 'description': current_ticket.description})
    return render(request, 'generic_form.html', {'form': form})

@login_required
@employee_required
def ticket_claim(request, id):
    current_ticket = Ticket.objects.get(id=id)
    current_ticket.assignedTo = request.user.username
    current_ticket.status = "IN PROGRESS"
    current_ticket.save()
    return HttpResponseRedirect(reverse('ticketdetails', args=[current_ticket.id]))

@login_required
@employee_required
def ticket_complete(request, id):
    current_ticket = Ticket.objects.get(id=id)
    current_ticket.assignTo = 'NONE'
    current_ticket.completedBy = request.user.username
    current_ticket.status = "DONE"
    current_ticket.save()
    return HttpResponseRedirect(reverse('ticketdetails', args=[current_ticket.id]))

@login_required
@employee_required
def ticket_invalid(request, id):
    current_ticket = Ticket.objects.get(id=id)
    current_ticket.assignTo = 'NONE'
    current_ticket.completedBy = 'NONE'
    current_ticket.status = "INVALID"
    current_ticket.save()
    return HttpResponseRedirect(reverse('ticketdetails', args=[current_ticket.id]))

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