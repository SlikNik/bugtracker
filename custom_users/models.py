import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
class Role(models.Model):
    class RoleTypes(models.TextChoices):
        COMPANY= 'COMPANY'
        EMPLOYEE= 'EMPLOYEE'
        ADMIN = 'ADMIN'
    
    role_type = models.CharField(
        max_length=8,
        choices=RoleTypes.choices,
    )

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('COMPANY', 'COMPANY'),
        ('EMPLOYEE', 'EMPLOYEE'),
        ('ADMIN', 'ADMIN'),
    )
    role = models.CharField(
        max_length=8,
        choices=ROLE_CHOICES,
        blank=True, 
        null=True
    )
    REQUIRED_FIELDS = ['role']

class Company(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, blank=True, null=True)
    founded = models.IntegerField()
    specialize_in = models.CharField(max_length=120, blank=True, null=True)
    company_code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sign_up_date = models.DateField(default=timezone.now)
    REQUIRED_FIELDS = ['name', 'founded', 'specialize_in']

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=120, blank=True, null=True)
    lastname = models.CharField(max_length=120, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    sign_up_date = models.DateField(default=timezone.now)
    REQUIRED_FIELDS = ['firstname', 'lastname', 'company']


    def __str__(self):
        return f'{self.firstname} {self.lastname}'