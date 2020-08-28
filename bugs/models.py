from django.db import models
from django.utils import timezone
from custom_users.models import CustomUser


class Ticket(models.Model):
    class Status(models.TextChoices):
        NEW = 'NEW'
        IN_PROGESS = 'IN PROGRESS'
        DONE = 'DONE'
        INVALID = 'INVALID'
    title = models.CharField(max_length=80)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    filedBy = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=200, 
        choices=Status.choices,
        default=Status.NEW)
    assignedTo = models.CharField(max_length=240, default='NONE')
    completedBy = models.CharField(max_length=240, default='NONE')
    markedBy = models.CharField(max_length=240, default='NONE')


    def __str__(self):
        return self.status
    
    @property
    def age(self):
        return int((timezone.now() - self.date).days / 365.25)