from django.contrib import admin
from bugs.models import Ticket, Project

admin.site.register(Ticket)
admin.site.register(Project)

