from django.db import models

# Create your models here.

class UserRegistration(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

from django.db import models
from django.core.exceptions import ValidationError
import datetime

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Example: Employee's email address
    mobile_no = models.CharField(max_length=10)  # Example: Mobile number
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')],
        default='SELECT'  # Set default to 'Male'
    )  # Example: Gender (Male/Female)
    
    designation = models.CharField(
        max_length=100,
        choices=[('HR', 'HR'), ('Manager', 'Manager'), ('Sales', 'Sales')],
        default='SELECT'  # Set default to 'HR'
    )  # Example: Job designation
    
    course = models.CharField(
        max_length=50, 
        choices = [
        ('MCA', 'MCA'),
        ('AIML', 'AIML')],
        default='SELECT'  # Set default to 'MCA'
    )  # Example: Training or course name
    
    image = models.ImageField(upload_to='employee_images/', null=True, blank=True)
    created_date = models.DateTimeField(default=datetime.datetime(2023, 12, 20, 12, 0, 0))  # Example default
    
    def clean(self):
        # Ensure that no employee has a duplicate email
        if Employee.objects.filter(email=self.email).exists():
            raise ValidationError('An employee with this email already exists.')
        super().clean()

    def __str__(self):
        return self.name




