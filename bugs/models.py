from django.db import models
from django.utils import timezone
from custom_users.models import Company,Employee

class Project(models.Model):
    class Status(models.TextChoices):
        NEW = 'NEW'
        IN_PROGESS = 'IN PROGRESS'
        DONE = 'DONE'
        INVALID = 'INVALID'
    title = models.CharField(max_length=80)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=200, 
        choices=Status.choices,
        default=Status.NEW)
    developers = models.ManyToManyField(Employee)

    def __str__(self):
        return self.title

class Ticket(models.Model):
    class Status(models.TextChoices):
        NEW = 'NEW'
        IN_PROGESS = 'IN PROGRESS'
        DONE = 'DONE'
        INVALID = 'INVALID'
    title = models.CharField(max_length=80)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    filedBy = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=200, 
        choices=Status.choices,
        default=Status.NEW)
    assignedTo = models.CharField(max_length=240, default='NONE')
    completedBy = models.CharField(max_length=240, default='NONE')

    def __str__(self):
        return self.status


