from django import forms
from bugs.models import Ticket, Project

class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)


class AddTicketForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('title', 'description')

class AddProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('title', 'description')
    

